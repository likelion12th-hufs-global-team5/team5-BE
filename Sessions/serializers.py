from rest_framework import serializers
from .models import Session

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'

class SessionNamePartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ['sessionName', 'part']

class SessionAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ['id', 'sessionName']

class SessionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'
        read_only_fields = ('sessionName', 'part')
    