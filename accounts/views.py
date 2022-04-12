from django.shortcuts import render, redirect
#Flash messages to the user
from django.contrib import messages
from .models import Profile
#login require decorator
from django.contrib.auth.decorators import login_required
#import built in forms
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm



# Create your views here.

def register(request):
    template_name="apps/users/register.html"
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account {username} has been created! You may now login')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,template_name, {'form': form})

@login_required
def profile(request):
    template_name="apps/users/profile.html"
    return render(request,template_name)


@login_required
def profile(request):
    template_name="apps/accounts/profile.html"
    user = request.user
    profile,new = Profile.objects.get_or_create(user=user)
    if request.method == 'POST':
        # u_form = the user form
        #request.user = the current logged in user
        u_form = UserUpdateForm(request.POST, instance=user)
        # p_form = the user profile form
        p_form = ProfileUpdateForm(
            request.POST,
            #request.FILES = the FILE/image file the user is attempting to update
            request.FILES,
            #request.user.profile = the PROFILE of the current logged in user
            instance=profile
        )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request,template_name, context)