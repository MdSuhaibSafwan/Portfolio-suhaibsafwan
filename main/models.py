from django.db import models
from django.contrib.auth.models import User


# class UserImages(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="profile_images")
#     image = models.ImageField(upload_to="profile/user/picture")

#     def __str__(self):
#         return self.user.username + " image"
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # image = models.ImageField(upload_to="profile/user/picture", null=True)
    github_url = models.URLField()
    facebook_url = models.URLField()
    upwork_url = models.URLField()
    fiverr_url = models.URLField()


class WorkExperience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="experiences")
    description = models.TextField()
