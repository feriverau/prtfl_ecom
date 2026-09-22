from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

def profile_image_path(instance, filename):
    ext = filename.split(".")[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return f"users/{filename}"


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile"
    )

    image = models.ImageField(
        upload_to=profile_image_path,
        default="users/default_profile.jpg"
    )

    def __str__(self):
        return self.user.username