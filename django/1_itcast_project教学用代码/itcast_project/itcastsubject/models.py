#coding=utf-8
from django.db import models

# Create your models here.
from django.template.defaultfilters import slugify

class Subject(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
            self.slug = slugify(self.name)
            super(Subject, self).save(*args, **kwargs)

    def __unicode__(self):
            return self.name

class Page(models.Model):
    subject = models.ForeignKey(Subject)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __unicode__(self):      #Python2, use __str__ on Python3
        return self.title

