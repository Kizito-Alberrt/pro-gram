from gram.settings import TIME_ZONE
from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.user'),on_delete=models.CASCADE
    image = models.ImageField(blank=True, null=True)
    caption = models.TextField()
    created_date = models.DateTimeField(default= timezone.new)


    def _str_(self):
        return self.caption