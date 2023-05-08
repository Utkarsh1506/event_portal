from django.db import models
from django.contrib.auth.models import User


class Member(User):

    year_choices = (
        (1, '1st Year'),
        (2, '2nd Year'),
        (3, '3rd Year'),
        (4, '4th Year'),
    )

    gender_choices = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    )

    roll_no = models.CharField(max_length=10, unique=True)
    year = models.IntegerField(choices=year_choices, default=1)
    
    phone_number = models.CharField(max_length=10, unique=True)
    
    is_dean = models.BooleanField(default=False)
    is_cfo = models.BooleanField(default=False)
    is_club_mentor = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    
    
# ===============================================================================================

# ==================================== CLUBS ==============================================

    
class Club(models.Model):
    name = models.CharField(max_length=100)
    factuly_incharge = models.OneToOneField(Member, on_delete=models.CASCADE)
    president = models.CharField(max_length=100)
    events = models.ManyToManyField('Event', related_name="events_add", blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='activities/')
    
    class Meta:
        verbose_name_plural = 'Club'
    
    def __str__(self):
        return self.name.title()
    
# ========================================= EVENTS ==========================================

class Event(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    organizer = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    # time = models.TimeField()
    venue = models.CharField(max_length=100)
    budget = models.FileField(upload_to='budget/')
    
    event_poster = models.ImageField(upload_to='activities/', null=True, blank=True)
    
    is_approved_by_dean = models.BooleanField(default=False)
    is_approved_by_cfo = models.BooleanField(default=False) 
    
    is_rejected = models.BooleanField(default=False)
    dean_reject_msg = models.TextField(max_length=800, null=True, default="")
    cfo_reject_msg = models.TextField(max_length=800, null=True, default="")
    
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title.title()