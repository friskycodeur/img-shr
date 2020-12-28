from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm


@login_required
def profile(request):
    if request.method=="POST":
        p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            p_form.save()
            messages.success(request,f'You account has been updated.')
            return redirect('profile')


    else:
        p_form=ProfileUpdateForm(instance=request.user.profile)
        

    context={
        'p_form':p_form,
    }
    return render(request,'profile.html',context)