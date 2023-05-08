from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from portal.models import Member


def login(request):
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = auth.authenticate(username=username, password=password)

        if user is not None:
    
            member = Member.objects.get(id=user.id)

            if member.is_dean:
                auth.login(request, user)
                return redirect("dean_home")
            
            elif member.is_cfo:
                auth.login(request, user)
                return redirect("cfo_home")
            
            elif member.is_club_mentor:
                auth.login(request, user)
                return redirect("club_home")
    
    return render(request, 'portal/login.html')

def logout(request):
    auth.logout(request)
    return redirect("login")
