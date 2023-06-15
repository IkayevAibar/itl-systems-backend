import uuid

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class SimpleUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Email address must be provided")
        
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class SimpleUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    
    objects = SimpleUserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
    
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Lead(TimeStampedModel):
    id = models.CharField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("Полное Имя", max_length=255, null=True, blank=True)
    email = models.EmailField("Почта", null=True, blank=True)
    phone = models.CharField("Телефон", max_length=255, null=True, blank=True)
    args = models.JSONField("JSON", null=True, blank=True)
    

    class Meta:
        verbose_name = "Лид"
        verbose_name_plural = "Лиды"

    def __str__(self):
        return self.name

class TextContent(TimeStampedModel):
    key = models.CharField(unique=True, max_length=255, null=True, blank=True)
    content = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Текстовый контент"
        verbose_name_plural = "Текстовые контенты"

class ImageContent(TimeStampedModel):
    key = models.CharField(unique=True, max_length=255, null=True, blank=True)
    content = models.ImageField(null=True, blank=True, upload_to='content/images/')

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"