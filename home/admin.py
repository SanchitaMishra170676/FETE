from django.contrib import admin
from .models import CarouselImg, AboutFete, CampaignDescription, Campaign, PostDescription, Head, Achievement, Gallery, Team, Message, Registration
from import_export.admin import ImportExportModelAdmin
# Register your models here.


class CarouselImgAdmin(ImportExportModelAdmin):
    """ Admin Panel for  CarouselImg Model """

    list_display = ('id','name','active')
    search_fields = ('name','active')
    list_display_links = ('name','active')
    list_filter = ('active',)
    list_per_page= 20


    ordering = ('date',)

admin.site.register(CarouselImg,CarouselImgAdmin)

class AboutFeteAdmin(ImportExportModelAdmin):
    """ Admin Panel for About """
    list_display= ('id','updatedOn')
    list_display_links=('id','updatedOn')

admin.site.register(AboutFete,AboutFeteAdmin)

class CampaignDescriptionAdmin(ImportExportModelAdmin):
    """ Admin Panel for Campaign description """
    list_display= ('id','updatedOn')
    list_display_links=('id','updatedOn')

admin.site.register(CampaignDescription,CampaignDescriptionAdmin)

class CampaignAdmin(ImportExportModelAdmin):
    """ Admin Panel for Campaigns """
    list_display=('id','title','date','active')
    list_display_links=('title','date')
    list_filter=('active',)
    search_fields = ('title','active')
    ordering = ('date',)

admin.site.register(Campaign,CampaignAdmin)

class PostDescriptionAdmin(ImportExportModelAdmin):
    """ Admin Panel for Post description """
    list_display= ('id','updatedOn')
    list_display_links=('id','updatedOn')

admin.site.register(PostDescription,PostDescriptionAdmin)

class HeadAdmin(ImportExportModelAdmin):
    """ Admin Pannel for heads """
    list_display=('id','name','active')
    list_display_links=('name',)
    list_filter=('active',)
    search_fields=('active','name')
    ordering=('date',)

admin.site.register(Head,HeadAdmin)

class AchievementAdmin(ImportExportModelAdmin):
    """ Admin Panel for Achievements """
    list_display=('id','title','date','active')
    list_display_links=('title','date')
    list_filter=('active',)
    search_fields = ('title','active')
    ordering = ('date',)

admin.site.register(Achievement,AchievementAdmin)

class GalleryAdmin(ImportExportModelAdmin):
    """ Admin Panel for Gallery """
    list_display=('id','title','date','active')
    list_display_links=('title','date')
    list_filter=('active',)
    search_fields = ('title','active')
    ordering = ('date',)

admin.site.register(Gallery,GalleryAdmin)

class TeamAdmin(ImportExportModelAdmin):
    """ Admin Panel for Team """
    list_display=('id','name','post','date','active')
    list_display_links=('name','date','post')
    list_filter=('active','post')
    search_fields = ('name','active','post')
    ordering = ('date',)

admin.site.register(Team,TeamAdmin)

class MessageAdmin(ImportExportModelAdmin):
    """ Admin Panel for Message """
    list_display=('id','name','email','subject','date','answered')
    list_display_links=('name','email','subject','date','answered')
    list_filter=('answered',)
    search_fields = ('name','email','subject','date','answered')
    list_per_page= 30
    ordering = ('-date',)

admin.site.register(Message,MessageAdmin)


class RegistrationAdmin(ImportExportModelAdmin):
    """ Admin Panel for Registration """
    list_display =('id', 'name', 'email', 'answered')
    list_display_links=('name','email')
    list_filter=('answered',)
    search_fields=('name', 'email', 'answered', 'contact')
    ordering=('-date',)

admin.site.register(Registration,RegistrationAdmin)