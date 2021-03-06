from django.contrib import admin
from accounts.models import UserProfile

# Register your models here.
# admin.site.site_header = "Admin"

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user','user_info','phone','website')

    def user_info(self,userObj):
        return userObj.description

    def get_queryset(self, request):
        queryset = super(UserProfileAdmin,self).get_queryset(request)
        queryset = queryset.order_by("user")
        return queryset

    user_info.short_description = "Info."



admin.site.register(UserProfile,UserProfileAdmin)


