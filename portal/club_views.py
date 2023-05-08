from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Event, Club

def is_club(user):
    return user.is_club_mentor

@login_required(login_url='login')
def club_home(request):
    
    if is_club(request.user.member):
        
        club = Club.objects.get(factuly_incharge = request.user.member)
        unapproved_events = Event.objects.filter(club = club, is_approved_by_cfo=False)
        
        approved_events = Event.objects.filter(club = club, is_approved_by_cfo=True)
        
        parameters = {
            "club": club,
            "unapproved_events": unapproved_events,
            "approved_events": approved_events,
        }
        
        return render(request, 'portal/club/home.html', parameters)
    
    return redirect("login")

@login_required(login_url='login')
def events(request):
    
    if is_club(request.user.member):
        club = Club.objects.get(factuly_incharge = request.user.member)
        events = Event.objects.filter(club = club)
        
        
        parameters = {
            "club": club,
            "events": events,
        }
        
        return render(request, 'portal/club/events.html', parameters)
    
    return redirect("login")


#===================================================================================================

@login_required(login_url="login")
def delete_event(request, id):
    
    if is_club(request.user.member):
    
        event = Event.objects.get(id = id)
        event.delete()
        
        print("Event deleted successfuly!")
        
        return redirect("club_home")
    
    else:
        return redirect("login")
    
@login_required(login_url="login")
def add_event(request):
    
    if is_club(request.user.member):
        
        club = Club.objects.get(factuly_incharge = request.user.member)
            
        parameters = {
            "club": club,
        }
    
        if request.method == "POST":
            
            title = request.POST.get('event_title')
            organizer = request.POST.get('organizer')
            description = request.POST.get('description')
            date = request.POST.get('date')
            venue = request.POST.get('venue')
            budget = request.FILES.get('budget_file')
            event_poster = request.FILES.get('event_poster')
            
            event = Event(
                club = club,
                title = title,
                organizer = organizer,
                description = description,
                date = date,
                venue = venue,
                budget = budget,
                event_poster = event_poster,
            )
            
            event.save()
            
            print("Event added successfuly!")
            
            return redirect("club_home")
        
        return render(request, 'portal/club/add_event.html', parameters)
    
    else:
        return redirect("login")