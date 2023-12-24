from django.shortcuts import render,redirect
from .forms import Resgitation_Form,ChangeUserData
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
# Create your views here.
def home(request):
    return render(request, 'home.html')

def singup(request):
    if request.method =='POST':
        form = Resgitation_Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created Successfully')
            print(form.cleaned_data)
        
           
    else:
        form = Resgitation_Form()
    return render(request, 'singup.html',{'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            
            name = form.cleaned_data['username']
            userpass = form.cleaned_data['password']
            
            
            user = authenticate(username=name, password=userpass)
            if user is not None:
                messages.success(request, 'Logged In Successfully')
                login(request, user)
                return redirect('profile')
          
          
            
    else:
        form = AuthenticationForm()
    return render(request, './login.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.success(request, 'Logged Out Successfully')
    return redirect('homepage')

def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ChangeUserData(request.POST, instance=request.user)
            if form.is_valid():
                messages.success(request, 'Account updated successfully')
                form.save()
        else:
            form = ChangeUserData(instance=request.user)
        return render(request, './profile.html', {'form': form})
    else:
        return redirect('signup')
    
def pass_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data = request.POST)
        if  form .is_valid():
            form .save()
            messages.success(request, 'Password Change Successfully')
            update_session_auth_hash(request,form.user)
            return redirect('profile')
    
    else:
         form  = PasswordChangeForm(user= request.user)
    return render(request, 'pass_change.html', {'form' : form})


def pass_change2(request):
    if request.method == 'POST':
        form = SetPasswordForm(request.user, data = request.POST)
        if  form .is_valid():
            form .save()
            messages.success(request, 'Password Change Successfully')
            update_session_auth_hash(request,form.user)
            return redirect('profile')
    
    else:
         form  = SetPasswordForm(user= request.user)
    return render(request, 'pass_change.html', {'form' : form})