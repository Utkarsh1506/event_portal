from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Club, Event, Member
from django.contrib import messages


def is_dean(user):
    return user.is_dean


@login_required(login_url='login')
def dean_home(request):

    if is_dean(request.user.member):

        unapproved_events = Event.objects.filter(is_approved_by_dean=False, is_rejected=False)

        parameters = {
            'unapproved_events': unapproved_events,
        }

        return render(request, 'portal/dean/home.html', parameters)

    return redirect("login")



@login_required(login_url='login')
def events(request):
    if is_dean(request.user.member):

        events = Event.objects.all()

        parameters = {
            "events": events,
        }

        return render(request, 'portal/dean/events.html', parameters)

    return redirect("login")

# ===============================================================================================


@login_required(login_url='login')
def approve_event(request, id):

    if is_dean(request.user.member):

        event = Event.objects.get(id=id)

        event.is_approved_by_dean = True

        event.save()

        messages.success(request, 'Event Approved')

        return redirect('dean_home')

    return redirect("login")


@login_required(login_url='login')
def reject_event(request, id):
    
    if is_dean(request.user.member):

        event = Event.objects.get(id=id)
        
        reject_text = request.POST.get('reject_text')
        
        event.dean_reject_msg = reject_text

        event.is_rejected = True

        event.save()

        messages.success(request, 'Event Rejected')

        return redirect('dean_home')

    return redirect("login")