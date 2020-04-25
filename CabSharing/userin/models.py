from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    def __str__(self):
        return self.user.username

class LookingCab(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateField(default=now)

class BookedCab(models.Model):
    date = models.DateField(default=now)
    LOCATIONS =( 
        ("1", "IITG_Campus"), 
        ("2", "Guwahati Airport"), 
        ("3", "GHY RLY Station"), 
        ("4", "Kamakhya Junction"),
    )
    source = models.CharField(max_length=50, choices=LOCATIONS)
    dest = models.CharField(max_length=50, choices=LOCATIONS)