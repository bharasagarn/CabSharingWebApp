from django.contrib import admin
from userin.models import UserProfileInfo, User, LookingCab, BookedCab

# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(LookingCab)
admin.site.register(BookedCab)