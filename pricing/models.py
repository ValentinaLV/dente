from django.db import models

from news.utils import get_slug


class ServiceProductCategory(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Service Category'
        verbose_name_plural = 'Service Categories'

    def __str__(self):
        return f'{self.name}'


class ServiceProduct(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    category = models.ForeignKey(ServiceProductCategory, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=150, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Service Product'
        verbose_name_plural = 'Service Products'

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = get_slug(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'
