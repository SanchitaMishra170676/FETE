from django.shortcuts import render, redirect 
from django.contrib import messages
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .models import CarouselImg, AboutFete, CampaignDescription, Campaign, PostDescription, Head, Achievement, Gallery, Team, Message, Registration 

def home(request):
    carouselImg = CarouselImg.objects.filter(active=True)
    aboutFete= AboutFete.objects.order_by('-updatedOn').all()[:1]
    campaignDescription = CampaignDescription.objects.order_by('-updatedOn').all()[:1]
    campaigns = Campaign.objects.filter(active=True)
    postDescription = PostDescription.objects.order_by('-updatedOn').all()[:1]
    heads = Head.objects.filter(active=True)
    achievements= Achievement.objects.filter(active=True)

    context = {'carouselImgs': carouselImg,'aboutFete':aboutFete,'campaignDescription': campaignDescription,'campaigns':campaigns, 'postDescription':postDescription, 'heads': heads,'achievements': achievements}
    return render(request,'index.html',context)

def gallery(request):
    gallery = Gallery.objects.order_by('-date').filter(active=True)[:12]
    context= {'gallery': gallery} 
    return render(request,'gallery.html',context)

def contact(request):
    if request.method == "POST":
        try:
            name = request.POST['name']
            email = request.POST['email']
            contact = request.POST['contact']
            subject = request.POST['subject']
            context = request.POST['context']
            message = Message(name = name, email = email, contact = contact, subject = subject, context = context)
            message.save()
            messages.success(request,'Message Received! We will contact you soon.')
            return redirect ('contact')
        except:
            messages.error(request,"Failed to send message. Kindly contact Yash- 9760055129 / Meghna- 7900995990")
    return render(request,'contact.html')

def team(request):
    team = Team.objects.order_by('-date').filter(active=True)[:20]
    context = {'team': team}
    return render(request,'team.html', context)

def donation(request):
    if request.method == "POST":
        try:
            name = request.POST['name']
            age = request.POST["age"]
            email = request.POST['email']
            number = request.POST['number']
            address = request.POST['address']
            city = request.POST['city']
            occupation = request.POST['occupation']
            college = request.POST['college']
            course = request.POST['course']
            experience = request.POST['prevexp']
            inspiration = request.POST['inspiration']
            proof = request.FILES['image']
            registration = Registration(name= name, age=age, email=email, contact=number, address=address, city=city, occupation=occupation, college=college, course=course, experience=experience, inspiration=inspiration, proof=proof)
            registration.save()
            messages.success(request,'Registration confirmed! Will contact you soon')
            return redirect('donation')
        except:
            messages.error(request,"Failed to send message. Kindly contact Yash- 9760055129 / Meghna- 7900995990")
    return render(request,'donationform.html')

# Create your views here.
