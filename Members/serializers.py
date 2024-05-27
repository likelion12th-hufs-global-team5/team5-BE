from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import MyUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['name', 'year', 'part', 'introduction', 'userPhoto']

class LoginSerializer(serializers.Serializer):
    memberId = serializers.CharField(required=False)
    password = serializers.CharField(required=False)

    def validate(self, data):
        memberId = data.get('memberId')
        password = data.get('password')

        if not memberId:
            raise serializers.ValidationError({"memberId": "ID를 입력해야합니다."})
        if not password:
            raise serializers.ValidationError({"password": "비밀번호를 입력해야합니다."})

        try:
            user = MyUser.objects.get(memberId=memberId)
        except MyUser.DoesNotExist:
            raise serializers.ValidationError({"memberId": "회원이 아닙니다."})

        user = authenticate(memberId=memberId, password=password)

        if not user:
            raise serializers.ValidationError({"password": "비밀번호가 틀렸습니다."})

        data['user'] = user
        return data

class JoinSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = MyUser
        fields = ['memberId', 'name', 'studentNumber', 'currentPosition', 'year', 'introduction', 'part', 'password1', 'password2']
        extra_kwargs = {
            'memberId': {'error_messages': {'required': '이 필드는 필수입니다.'}},
            'name': {'error_messages': {'required': '이 필드는 필수입니다.'}},
            'studentNumber': {'error_messages': {'required': '이 필드는 필수입니다.'}},
            'password1': {'error_messages': {'required': '이 필드는 필수입니다.'}},
            'password2': {'error_messages': {'required': '이 필드는 필수입니다.'}},
            'currentPosition': {'error_messages': {'required': '이 필드는 필수입니다.'}},
            'introduction': {'error_messages': {'required': '이 필드는 필수입니다.'}},
            'part': {'error_messages': {'required': '이 필드는 필수입니다.'}},
            'password1': {'write_only': True},
            'password2': {'write_only': True},
            'memberId': {'validators': []}
        }

    def create(self, validated_data):
        password = validated_data.pop('password1')
        validated_data.pop('password2')
        user = MyUser(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError({"password": "위 비밀번호와 일치하지 않습니다."})
        if MyUser.objects.filter(memberId=data['memberId']).exists():
            raise serializers.ValidationError({"memberId": "해당 id를 가진 사용자가 존재합니다."})
        return data

class UserUpdateSerializer(serializers.ModelSerializer):
    currentPassword = serializers.CharField(write_only=True, required=False)
    newPassword = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = MyUser
        fields = ['part', 'introduction', 'currentPassword', 'newPassword', 'userPhoto']

    def validate(self, data):
        user = self.instance
        
        if 'new_password' in data:
            if not data.get('currentPassword'):
                raise serializers.ValidationError({"password":"현재 비밀번호를 입력해야 합니다."})
            if not user.check_password(data.get('currentPassword')):
                raise serializers.ValidationError({"password":"현재 비밀번호가 맞지 않습니다."})
        
        return data

    def update(self, instance, validated_data):
        if 'newPassword' in validated_data:
            instance.set_password(validated_data['newPassword'])
            validated_data.pop('newPassword')
            validated_data.pop('currentPassword', None)

        instance.userPhoto = validated_data.get('userPhoto', instance.userPhoto)

        return super().update(instance, validated_data)