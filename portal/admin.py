from django.contrib import admin
from .models import Member, Event, Club

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ("username", "roll_no", "year", "phone_number", "is_dean", "is_cfo", "is_club_mentor")
    exclude = ('is_active', 'groups', 'user_permissions', 'password', 'is_staff', 'is_superuser', 'date_joined')

@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ('name', 'factuly_incharge', 'president', 'description')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'club', 'organizer', 'date', 'venue', 'is_approved_by_dean', 'is_approved_by_cfo')
    