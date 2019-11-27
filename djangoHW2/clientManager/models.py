from django.db import models
from django.utils import timezone
from django.forms import ModelForm


# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    sexual = models.CharField(max_length=20)
    birthday = models.CharField(max_length=20)
    email = models.CharField(max_length=64)
    phone = models.CharField(max_length=10)
    description = models.CharField(max_length=5000, null=True, blank=True)  # encoded as a json array
    department = models.CharField(max_length=40, null=True)

    create_time = models.DateTimeField(editable=False)
    update_time = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.create_time:
            self.create_time = timezone.now()
        self.update_time = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Manager(models.Model):
    username = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=20)
    department = models.CharField(max_length=40)

    create_time = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        if not self.create_time:
            self.create_time = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username


class ManagerForm(ModelForm):
    class Meta:
        model = Manager
        fields = ['username', 'password', 'department']


