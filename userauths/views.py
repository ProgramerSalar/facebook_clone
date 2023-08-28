from django.shortcuts import render, redirect, HttpResponse
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate,login
from userauths.models import Profile



# Create your views here.


def RegisterView(request):
    if request.user.is_authenticated:
        messages.warning(request, 'You are registered!')
        return redirect('core:feed')
    
    form = UserRegisterForm(request.POST or None)
    # print("form", form)
    
    if form.is_valid():
        # return HttpResponse("valid")
        # print("valid")
        form.save()



        full_name = form.cleaned_data['full_name']
        # print("full_name", full_name)
        phone = form.cleaned_data['phone']
        email = form.cleaned_data['email']
        password1 = form.cleaned_data['password1']
        password2  = form.cleaned_data['password2']
        
        
        # id = form.cleaned_data()

        user = authenticate(email=email, password1=password1, password2=password2)
        print(user)
        login(request, user)

        messages.success(request, f"Hi {full_name}.you account was created successfully.")

        profile = Profile.objects.get(user=request.user)
        profile.full_name = full_name
        profile.phone = phone
        
        profile.save()





    context = {
        'form':form,
    }



    return render(request, 'userauths/sign-up.html',context)



