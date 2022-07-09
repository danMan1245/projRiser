
from django import template
from django.views import generic
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from operator import attrgetter
from itertools import chain
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
)


class HomePageView(generic.TemplateView): #0011
    template_name = 'home.html'

class AboutView(generic.TemplateView): #0011
    template_name = 'about.html'

class MyAccountView(LoginRequiredMixin,generic.TemplateView): #0011
    template_name = 'my_account.html'

@login_required
def mymodules(request):
    mygroups = request.user.groups.all()
    return render(request,'my_modules.html',
                    {'mygroups':mygroups})
