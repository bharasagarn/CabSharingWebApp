from django.shortcuts import render
from userin.forms import UserForm,UserProfileInfoForm,LookingCabForm,BookedCabForm
from userin.models import BookedCab, UserProfileInfo
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.forms.models import model_to_dict
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import datetime


def index(request):
    data = BookedCab.objects.filter(date__gte=datetime.datetime.now()).order_by('-date')
    userdata = 0
    if request.user.is_authenticated:
        userdata = UserProfileInfo.objects.get_or_create(user=request.user)
    db = {
        "cabs": data,
        "userdata": userdata
    }
    return render(request,'userin/index.html',db)

@login_required
def special(request):
    return HttpResponse("You are logged in !")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('dp found')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'userin/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account inactive.")
        else:
            print("Login failed")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login credentials.")
    else:
        return render(request, 'userin/login.html', {})

@login_required
def look_cab(request):
    cabbed = False
    if request.method == 'POST':
        looking_cab_form = LookingCabForm(data=request.POST)
        if looking_cab_form.is_valid():
            user = request.user
            cab = looking_cab_form.save(commit=False)
            cab.user = user
            cabres = ""
            cabres1 = []
            if(BookedCab.objects.filter(date=cab.date).filter(source=cab.source).filter(dest=cab.dest).exists()):
                cabres = BookedCab.objects.filter(date=cab.date).filter(source=cab.source).filter(dest=cab.dest)
                cabbed = True
            if(cabbed):
                for c in cabres:
                    cb = {}
                    cb['name']=UserProfileInfo.objects.get(user=c.user).name
                    cb['mobile']=UserProfileInfo.objects.get(user=c.user).mobile
                    cb['date']=c.date
                    cb['source']=c.get_source_display
                    cb['dest']=c.get_dest_display
                    cabres1.append(cb)
            return render(request,'userin/search_results.html',
                                {'cabres':cabres1,
                                'filled':cabbed})
        else:
            print(looking_cab_form.errors)
            return HttpResponse("Error in form input")
    else:
        looking_cab_form = LookingCabForm()
        return render(request,'userin/lookingcab.html',
                          {'looking_cab_form':looking_cab_form,
                           'cabbed':cabbed})

@login_required
def booked_cab(request):
    booked = False
    if request.method == 'POST':
        booked_cab_form = BookedCabForm(data=request.POST)
        if booked_cab_form.is_valid():
            user = request.user
            book = booked_cab_form.save(commit=False)
            book.user = user
            book.save()
            booked = True
            return HttpResponseRedirect(reverse('index'))
        else:
            print(booked_cab_form.errors)
            return HttpResponse("Error in form input")
    else:
        booked_cab_form = BookedCabForm()
        return render(request,'userin/bookedcab.html',
                          {'booked_cab_form':booked_cab_form,
                           'booked':booked})

@login_required
def edit_profile(request):
    user = request.user
    edited = False
    profile = UserProfileInfo.objects.get(user=user)
    if request.method=='POST':
        editProfileForm = UserProfileInfoForm(data=request.POST)
        if editProfileForm.is_valid():
            edit = editProfileForm.save(commit=False)
            if 'profile_pic' in request.FILES:
                print('dp found')
                edit.profile_pic = request.FILES['profile_pic']
            UserProfileInfo.objects.filter(user=user).update(name=edit.name,mobile=edit.mobile,profile_pic=edit.profile_pic)
            edited = True
            return HttpResponseRedirect(reverse('index'))
        else:
            print(editProfileForm.errors)
            return HttpResponse("Form input error")
    else:
        editProfileForm = UserProfileInfoForm(initial=model_to_dict(profile))
        return render(request,'userin/editprofile.html',
                            {'editProfileForm':editProfileForm,
                            'edited':edited,
                            'profile':profile})