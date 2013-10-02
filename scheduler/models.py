from django.db import models

# Create your models here.


class Pilot(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    passport = models.BooleanField(default=False)

    def __unicode__(self):
        return self.first_name


class Aircraft(models.Model):
    short_name = models.CharField(max_length=30)
    tail_number = models.CharField(max_length=15)
    hours_before_inspection = models.IntegerField()
    cruise_speed = models.IntegerField()

    def __unicode__(self):
        return self.short_name


class Appointment(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    date_of_departure = models.DateField(verbose_name='Day of departure')
    time_of_departure = models.TimeField(verbose_name='Take off time')
    pilot = models.ForeignKey(Pilot)
    aircraft = models.ForeignKey(Aircraft)
    booked_on = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name


