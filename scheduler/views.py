# Create your views here.
from django.views import generic
from .models import Appointment


class IndexView(generic.CreateView):
    model = Appointment
    template_name = 'scheduler/scheduler_index.html'
    success_url = '/'


class AppointmentDetail(generic.DetailView):
    model = Appointment
    template_name = 'scheduler/appointment_detail.html'


class Ledger(generic.ListView):
    model = Appointment
    template_name = 'scheduler/ledger.html'


class AppointmentDate(generic.WeekArchiveView):
    queryset = Appointment.objects.all()
    date_field = "date_of_departure"
    make_object_list = True
    #week_format = "%W"
    allow_future = True
    allow_empty = True


class AppointmentDay(generic.DayArchiveView):
    queryset = Appointment.objects.all()
    date_field = "date_of_departure"
    make_object_list = True
    allow_future = True
    allow_empty = True