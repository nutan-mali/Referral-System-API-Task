from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from app1.models import Referral_system, Referee_system
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render (request,'home.html')

def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        referral_code = request.POST.get('referral_code')  # Assuming referral_code is submitted in the signup form

        if pass1 != pass2:
            return HttpResponse("Your password and confirm password are not the same!!")
        else:
            # Create the user
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()

            # Check if there's a referral with the provided referral_code
            if referral_code:
                # Update the referral system with the new refree (signup user)
                Referee_system.objects.create(
                refree=my_user,
                referral_code=referral_code
            )

            return redirect('login')

    return render(request, 'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

def get_referee_list(request):
        print("testing.....", request.user.id)
        if request.user.id:
            referral = Referral_system.objects.filter(referrer_id=request.user.id).first()
            print("testing.....ksdbcakjkanckn", referral.referral_code)
            referral_code = referral.referral_code
            referees = referral = Referee_system.objects.filter(referral_code=referral_code).all()
            print("refrees list",referees)
            return {"referees_list": referees}

