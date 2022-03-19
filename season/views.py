from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from django.views.generic import CreateView
from .forms import RegisterCalendarForm
from .models import Season 

# Create your views here.
class CalendarCreateView(CreateView):
    model = Season
    form_class = RegisterCalendarForm
    template_name = 'season/calendar.html'
    success_url = reverse_lazy('destiny:destiny_create')


    def create_calendar(request):
        # add the calendar during initialization
        form = RegisterCalendarForm(request.POST or None)
        if form.is_valid():
            form.save()
	
Calendar_register = CalendarCreateView.as_view()