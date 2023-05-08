from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Event, Member, Club

def is_cfo(user):
    return user.is_cfo

@login_required(login_url='login')
def cfo_home(request):
    
    if is_cfo(request.user.member):
        
        unapproved_events = Event.objects.filter(is_approved_by_dean=True, is_approved_by_cfo=False, is_rejected=False)
        
        parameters = {
            'unapproved_events': unapproved_events,
        }
        
        
        return render(request, 'portal/cfo/home.html', parameters)
    
    return redirect("login")

@login_required(login_url='login')
def events(request):
    
    if is_cfo(request.user.member):
        
        events = Event.objects.all()
        
        parameters = {
            "events": events,
        }
        
        return render(request, 'portal/cfo/events.html', parameters)
    
    return redirect("login")

# =====================================================================================================

@login_required(login_url='login')
def approve_event(request, id):

    if is_cfo(request.user.member):

        event = Event.objects.get(id=id)

        event.is_approved_by_cfo = True

        event.save()

        messages.success(request, 'Event Approved')

        return redirect('cfo_home')

    return redirect("login")


@login_required(login_url='login')
def reject_event(request, id):
    
    if is_cfo(request.user.member):

        event = Event.objects.get(id=id)
        
        reject_text = request.POST.get('reject_text')
        
        event.cfo_reject_msg = reject_text
        
        print(reject_text)

        event.is_rejected = True

        event.save()

        messages.success(request, 'Event Rejected')

        return redirect('cfo_home')

    return redirect("login")