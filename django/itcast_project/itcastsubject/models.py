from django.db import models

# Create your models here.


class Subject(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        return self.name


class Page(models.Model):
    Subject = models.ForeignKey(Subject)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __unicode__(self):  # Python2, use __str__ on Python3
        return self.title

from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)


def __unicode__(self):
    return self.user.username
