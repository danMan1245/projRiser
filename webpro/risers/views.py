# risers/views.py
from django.http import Http404
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.crypto import get_random_string
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
    UserPassesTestMixin
)

from django.views import generic
from django.urls import reverse_lazy

from . import models
from . import forms

from django import template

from django.contrib.auth import get_user_model
User = get_user_model()

# ***********************************************************************************
# Risersizing views
# ***********************************************************************************
class RisersizingCreateView(generic.CreateView):
    model = models.Risersizing
    form_class = forms.RisersizingForm
    template_name = 'risers/Risersizing_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        category = self.object.pipe_category
        od = self.object.pipe_OD
        tcorr = self.object.pipe_WT_corr
        wd_base = self.object.pipe_base_WD
        den_fd = self.object.fluid_density
        den_hy = self.object.hydro_density
        den_ou = self.object.outer_density
        p_refer = self.object.pressure_refer
        wd_refer = self.object.WD_refer
        p_surf = self.object.pressure_surf
        p_base = self.object.pressure_base
        hy_factor = self.object.hydro_factor
        smys = self.object.SMYS
        smuts = self.object.SMUTS
        E1 = self.object.F_E
        F1 = self.object.F_hoop
        F1_gas = self.object.F_hoop_gas
        F1_hy = self.object.F_hydro
        k1 = self.object.k_burst
        Tp = self.object.Tp
        YM = self.object.E_YM
        poisson = self.object.PR
        F1_c = self.object.F_c
        self.object.save()
        return super().form_valid(form)

class RisersizingUpdateView(generic.UpdateView):
    model = models.Risersizing
    form_class = forms.RisersizingForm
    template_name = 'risers/Risersizing_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        category = self.object.pipe_category
        od = self.object.pipe_OD
        tcorr = self.object.pipe_WT_corr
        wd_base = self.object.pipe_base_WD
        den_fd = self.object.fluid_density
        den_hy = self.object.hydro_density
        den_ou = self.object.outer_density
        p_refer = self.object.pressure_refer
        wd_refer = self.object.WD_refer
        p_surf = self.object.pressure_surf
        p_base = self.object.pressure_base
        hy_factor = self.object.hydro_factor
        smys = self.object.SMYS
        smuts = self.object.SMUTS
        E1 = self.object.F_E
        F1 = self.object.F_hoop
        F1_gas = self.object.F_hoop_gas
        F1_hy = self.object.F_hydro
        k1 = self.object.k_burst
        Tp = self.object.Tp
        YM = self.object.E_YM
        poisson = self.object.PR
        F1_c = self.object.F_c
        self.object.save()
        return super().form_valid(form)

class RisersizingDetailView(generic.DetailView):
    model = models.Risersizing
    template_name = 'risers/Risersizing_detail.html'
    select_related = ("user")

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(
            user__username__iexact=self.kwargs.get("username")
        )
