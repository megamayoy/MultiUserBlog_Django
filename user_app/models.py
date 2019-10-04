from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='default.jpg', upload_to="profile_pics")

    def __str__(self):
        return self.user.username + " profile"

    def save(self):

        super().save()
        img = Image.open(self.profile_pic.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_pic.path)
