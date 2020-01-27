from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class PatientFeedback(models.Model):
    MARK = [
        ('Horribly', '1 -> Horribly'),
        ('Badly', '2 -> Badly'),
        ('Normally', '3 -> Normally'),
        ('Good', '4 -> Good'),
        ('Great', '5 -> Great'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    mark = models.CharField(max_length=30, choices=MARK, blank=False)
    created_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='patients/', null=True, blank=True)

    class Meta:
        ordering = ['-created_date']
