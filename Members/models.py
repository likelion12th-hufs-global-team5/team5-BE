from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class MyUserManager(BaseUserManager):
    def create_user(self, memberId, name, studentNumber, password, currentPosition, year, introduction, part, **extra_fields):

        if not memberId:
            raise ValueError('이 필드는 필수입니다.')
        if not name:
            raise ValueError('이 필드는 필수입니다.')
        if not studentNumber:
            raise ValueError('이 필드는 필수입니다.')
        if not password:
            raise ValueError('이 필드는 필수입니다.')
        if not currentPosition:
            raise ValueError('이 필드는 필수입니다.')
        if not year:
            raise ValueError('이 필드는 필수입니다.')
        if not part:
            raise ValueError('이 필드는 필수입니다.')

        user = self.model(
            memberId=memberId,
            name=name,
            studentNumber=studentNumber,
            password=password,
            currentPosition=currentPosition,
            year=year,
            introduction=introduction,
            part=part,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, memberId, name, studentNumber, password, currentPosition, year, introduction, part, **extra_fields):

        user = self.create_user(
            memberId=memberId,
            name=name,
            studentNumber=studentNumber,
            password=password,
            currentPosition=currentPosition,
            year=year,
            introduction=introduction,
            part=part,
            **extra_fields
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    part_type_choices = (
        ('BE', 'BE'),
        ('FE', 'FE'),
        ('공통', '공통')
    )
    memberId = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    studentNumber = models.IntegerField()
    currentPosition = models.CharField(max_length=4)
    userPhoto = models.ImageField(upload_to='member_photos/', default='member_photos/default.png', blank=True, null=True)
    year = models.IntegerField()
    introduction = models.TextField(max_length=100, blank=True, null=True)
    part = models.CharField(max_length=100, choices=part_type_choices)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'memberId' 
    REQUIRED_FIELDS = ['studentNumber', 'name', 'currentPosition', 'year', 'part']

    def __str__(self):
        return self.memberId
    
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

