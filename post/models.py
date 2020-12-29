from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    caption = models.CharField(max_length=120)
    image= models.ImageField(upload_to='post_pics')
    date_posted=models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})