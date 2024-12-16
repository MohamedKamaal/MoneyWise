from django.shortcuts import render, get_object_or_404, redirect
from users.models import User, Profile
from users.forms import ProfileForm, EmailForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from allauth.account.utils import send_email_confirmation
from django.contrib.auth import logout
from django.contrib.auth.views import redirect_to_login
from django.contrib import messages
# Create your views here.
def home_view(request):
    import os
    from django.conf import settings

    print("MEDIA_ROOT:", settings.MEDIA_ROOT)  # Check this in your Django server log
    return render(request,"home.html")


def profile_view(request,username=None):
    if username:
        profile = get_object_or_404(Profile, user__username=username)
    else:
        profile = get_object_or_404(Profile, user=request.user)
    
    return render(request,"users/profile.html",{"profile":profile})

@login_required
def profile_edit_view(request):
    profile = get_object_or_404(Profile, user=request.user)
    form = ProfileForm(instance=profile,files=request.FILES)
    if request.method == "POST":
        form = ProfileForm(instance=profile,files=request.FILES, data=request.POST )
        if form.is_valid():
            form.save()
            return redirect("profile:profile")
    context = {"form":ProfileForm}
    return render(request,"users/profile-edit.html",context=context)
        
@login_required
def profile_settings_view(request):
    return render(request, 'users/profile-settings.html')


@login_required
def profile_emailchange(request):
    
    if request.htmx:
        form = EmailForm(instance=request.user)
        return render(request, 'partials/email_form.html', {'form':form})
    
    if request.method == 'POST':
        form = EmailForm(request.POST, instance=request.user)

        if form.is_valid():
            
            # Check if the email already exists
            email = form.cleaned_data['email']
            if User.objects.filter(email=email).exclude(id=request.user.id).exists():
                messages.warning(request, f'{email} is already in use.')
                return redirect('profile:profile-settings')
            
            form.save() 
            
            # Then Signal updates emailaddress and set verified to False
            
            # Then send confirmation email 
            send_email_confirmation(request, request.user)
            
            return redirect('profile:profile-settings')
        else:
            messages.warning(request, 'Form not valid')
            return redirect('profile:profile-settings')
        
    return redirect('home')


@login_required
def profile_emailverify(request):
    send_email_confirmation(request, request.user)
    return redirect('profile:profile-settings')


@login_required
def profile_delete_view(request):
    user = request.user
    if request.method == "POST":
        logout(request)
        user.delete()
        messages.success(request, 'Account deleted, what a pity')
        return redirect('home')
    
    return render(request, 'users/profile-delete.html')