from django.db import models
from django.contrib.auth.models import User
from enum import Enum
import datetime

class Gender(Enum):
    Male = "Male"
    Female = "Female"
    Secret  = "Secret"


class person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #pw = models.CharField(max_length=25)
    f_name = models.CharField(max_length=25)
    l_name = models.CharField(max_length=25, blank=True)
    phone = models.CharField(max_length=11, blank=True)
    dob = models.DateField()
    gender = models.CharField(max_length=10, choices=[(tag.name, tag.value) for tag in Gender],default=Gender.Male)
    height = models.CharField(max_length=3, blank=True)
    weight = models.CharField(max_length=3, blank=True)
    emer_name = models.CharField(max_length=25, blank=True)
    emer_email = models.EmailField(max_length = 254, blank=True)
    emer_phone = models.CharField(max_length=11, blank=True)
    emer_relation = models.CharField(max_length=25, blank=True)


    #photo = models.FileField(upload_to='profile_pic/', blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.f_name


class goals(models.Model):
    prsn = models.OneToOneField(person, on_delete=models.CASCADE)
    goal1 = models.BooleanField(default=True)
    goal2 = models.BooleanField(default=True)
    goal3 = models.BooleanField(default=True)
    goal4 = models.BooleanField(default=False)
    goal5 = models.BooleanField(default=False)
    goal6 = models.BooleanField(default=False)
    goal7 = models.BooleanField(default=False)

    def __str__(self):
        return self.prsn.f_name


class bp_track(models.Model):
    prsn = models.ForeignKey(person, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    sys = models.IntegerField(default=-1)
    dia = models.IntegerField(default=-1)
    #photo = models.FileField(upload_to='profile_pic/', blank=True)

    def __str__(self):
        return self.prsn.f_name + "-" + str(self.date)


class badge(models.Model):
    prsn = models.OneToOneField(person, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    badge_name = models.CharField(max_length=25)

    def __str__(self):
        return self.prsn.f_name + "-" + str(self.date)




