from django.db import models
from accounts.models import CustomUser

class Speciality(models.Model):
    specialty_description = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.specialty_description
    class Meta:
        verbose_name_plural= "Specialities"


class Doctor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    is_surgeon = models.BooleanField(default=False)
    is_available_online = models.BooleanField(default=False)
    cnic = models.CharField(max_length=15)
    consultation_fee = models.DecimalField(max_digits=8, decimal_places=2,null=True)
    about = models.TextField(null=True)
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE,default=1)
    def __str__(self):
        return self.user.email



class TimeSlot(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='time_slots')
    slot_date = models.DateField(null=True)
    start_time=models.TimeField(null=True)
    end_time = models.TimeField(null=True)
    def __str__(self):
        return f'{self.start_time}'