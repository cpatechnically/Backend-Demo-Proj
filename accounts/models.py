from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
STATIC_IMG_SUBDIR_NAME="profile_pics"
DEFAULT_PROFILE_IMG="default.jpg"
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #directory a users picture gets uploaded to
    image = models.ImageField(default=f"{STATIC_IMG_SUBDIR_NAME}/{DEFAULT_PROFILE_IMG}", upload_to=STATIC_IMG_SUBDIR_NAME)
    #Could add as many additional fields as desired

    def __str__(self):
        return f'{self.user.username} Profile'

    #method for reducing image size upon save
    # def save(self):
    #     super().save()

    #     #create the image variable
    #     img = Image.open(self.image.path)

    #     #if stmt to check image size
    #     if img.height > 300 or img.width > 300:
    #         #max size of new image
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         #save the newly resized image
    #         img.save(self.image.path)
