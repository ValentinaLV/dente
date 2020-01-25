from time import time

from django.db import models
from django.urls import reverse
from django.utils.text import slugify


def get_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))


class DoctorProfile(models.Model):
    profile_name = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ('profile_name',)
        verbose_name = 'Doctor Profile'
        verbose_name_plural = 'Doctor Profiles'

    def __str__(self):
        return f'{self.profile_name}'


class Doctor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    profile = models.ForeignKey(DoctorProfile, on_delete=models.SET_NULL, null=True)
    specializations = models.ManyToManyField('Specialization', related_name='doctors')
    image = models.ImageField(upload_to='doctors/', null=True, blank=True)
    interesting_facts = models.CharField(max_length=250)
    work_experience = models.CharField(max_length=50)
    hobbies = models.CharField(max_length=100)
    quote = models.TextField(null=True)
    slug = models.SlugField(max_length=250, unique=True, blank=True)
    facebook_link = models.CharField(max_length=100, blank=True)
    instagram_link = models.CharField(max_length=100, blank=True)
    linkedin_link = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = ('last_name',)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = get_slug(f'{self.first_name}-{self.last_name}')
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('about:doctor_details_url', kwargs={'slug': self.slug})

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Specialization(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, blank=True)

    class Meta:
        ordering = ['title']

    def get_absolute_url(self):
        return reverse('about:specialization_details_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}"
