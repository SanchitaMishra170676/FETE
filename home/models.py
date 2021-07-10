from django.db import models
from django.utils import timezone

# Create your models here.
""" Model for home carousel """
class CarouselImg(models.Model):
    name = models.CharField(max_length=40)
    image = models.ImageField(upload_to="media/Home/CarouselImgs",default="")
    active = models.BooleanField(default=False)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class AboutFete(models.Model):
    description = models.TextField()
    updatedOn = models.DateTimeField(default= timezone.now)

class CampaignDescription(models.Model):
    description= models.TextField()
    updatedOn = models.DateTimeField(default= timezone.now)

class Campaign(models.Model):
    title = models.CharField(max_length= 20)
    description = models.CharField(max_length=110)
    active= models.BooleanField(default=False)
    date = models.DateTimeField(default= timezone.now)
    
    def __str__(self):
        return self.title

class PostDescription(models.Model):
    description= models.TextField()
    updatedOn= models.DateTimeField(default= timezone.now)

class Head(models.Model):
    name = models.CharField(max_length=40)
    post = models.CharField(max_length=40)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to="media/Home/Heads",default="")
    facebook_account_link = models.CharField(max_length=250, blank=True)
    instagram_account_link = models.CharField(max_length=250, blank=True)
    linkedin_account_link = models.CharField(max_length=250, blank=True)
    active = models.BooleanField(default= False)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Achievement(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to="media/Home/Achievements",default="")
    active = models.BooleanField(default= False)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Gallery(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="media/Home/Gallery",default="")
    active = models.BooleanField(default=False)
    date = models.DateTimeField(default= timezone.now)

    def __str__(self):
        return self.title

class Team(models.Model):
    name = models.CharField(max_length=25)
    post = models.CharField(max_length=15)
    image = models.ImageField(upload_to="media/Home/Team",default="")
    date = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    contact = models.CharField(max_length=13)
    subject = models.CharField(max_length=255)
    context = models.TextField()
    answered = models.BooleanField(default=False)
    date= models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email

class Registration(models.Model):
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=3)
    email = models.CharField(max_length=255)
    contact = models.CharField(max_length=13)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    occupation = models.CharField(max_length=50)
    college = models.CharField(max_length=255, blank=True)
    course = models.CharField(max_length=255, blank=True)
    experience = models.TextField()
    inspiration = models.TextField()
    proof = models.ImageField(upload_to="media/Home/RegistrationProof",default="")
    answered = models.BooleanField(default=False)
    date = models.DateTimeField(default= timezone.now)

    def __str__(self):
        return self.email

