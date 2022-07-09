# books/models.py #0010
# import uuid
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

# Create your models here.

User = get_user_model()

# ----------------------------------------------------------------
# riser Sizing
# ----------------------------------------------------------------
class Risersizing(models.Model):
    pipeCategory = (
        ('','Choose...'),
        ('DOI','DOI oil or gas pipeline'),
        ('DOT_liquid','DOT liquid pipeline'),
        ('DOT_gas','DOT gas pipeline')
    )
    class_name = models.CharField(max_length=200,default='Riser Sizing')
    user = models.ForeignKey(User, related_name="risersizings",
        on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    project_name =models.CharField(max_length=200)
    project_description = models.CharField(max_length=200,blank=True)
    pipe_category = models.CharField(max_length=200,choices = pipeCategory)
    pipe_OD = models.FloatField(
        verbose_name='riser outer diameter (in)')
    pipe_WT_corr = models.FloatField(
        verbose_name='riser wall thickness corrosion allowance (in)')
    pipe_base_WD = models.FloatField(
        verbose_name='riser base water dpeth (ft)')
    fluid_density = models.FloatField(
        verbose_name='riser content fluid density during operation (lb/ft3)')
    hydro_density = models.FloatField(
        verbose_name='riser hydrotest fluid density, usually seawater (lb/ft3)',default=64.0)
    outer_density = models.FloatField(
        verbose_name='riser surrounding fluid density, usually seawater (lb/ft3)',default=64.0)
    pressure_refer = models.FloatField(
        verbose_name='pressure at the reference location (psi)',
        help_text="This is the reference pressure used to calculate pressures at other locations.\
        The reference pressure can be shut-in tubing pressure at subsea well,\
        or the pressure at BSDV at the surface. If a value of 0.0 is left in this box,\
        the pressure at the surface and at the riser base should be provided.",default=0.0)
    WD_refer = models.FloatField(
        verbose_name='water depth at the reference location (ft)',default=0.0)
    pressure_surf = models.FloatField(
        verbose_name='riser design pressure at the surface (psi)',
        help_text="If a value of 0.0 is left in this box, the pressure will be repalced\
        by a calculated pressure based on the reference pressure.\
        User can also input a value to overide the calculation value.",default=0.0)
    pressure_base = models.FloatField(
        verbose_name='riser internal design pressure at the riser base (psi)',
        help_text="If a value of 0.0 is left in this box, the pressure will be repalced\
        by a calculated pressure based on the reference pressure.\
        User can also input a value to overide the calculation value.",default=0.0)
    hydro_factor = models.FloatField(
        verbose_name='hydrotest factor or the ratio of hydrotest pressure to design pressure')
    SMYS = models.FloatField(
        verbose_name='riser specified minimum yield strength (SMYS, psi)')
    SMUTS = models.FloatField(
        verbose_name='riser specified minimum ultimate tensile strength (SMUTS, psi)')
    F_E = models.FloatField(
        verbose_name='longitudinal/seam joint factor',default=1.0)
    F_hoop = models.FloatField(
        verbose_name='design factor for hoop stress',
        help_text="Applicable to code 30 CFR 250, API 1111, 49 CFR 195, ASME B31.4. \
        do not change the default value unless project requried.",
        default=0.6)
    F_hoop_gas = models.FloatField(
        verbose_name='design factor for hoop stress (49CFR192, B31.8)',default=0.5)
    F_hydro = models.FloatField(
        verbose_name='design factor for hydrotest presssure (API 1111)',default=0.75)
    k_burst = models.FloatField(
        verbose_name='a parameter to account for mechinical properties',
        help_text="Can be inreased to 0.5 for improved mechanical properties and\
        dimenisons control per API RP 1111 Annex B.",
        default=0.45)
    Tp = models.FloatField(
        verbose_name='riser content temperature, deg F')
    E_YM = models.FloatField(
        verbose_name='riser pipe Young\'s Modulus (psi)')
    PR = models.FloatField(
        verbose_name='Poisson\'s ratio (0.3 for steel)',default=0.3)
    F_c = models.FloatField(
        verbose_name='collapse factor',default=0.7)

    designPressure_base = models.FloatField(default=0.)
    designHydroPre_surf = models.FloatField(default=0.)
    designHydroPre_base = models.FloatField(default=0.)
    F_T = models.FloatField(default=1.0)
    WT_30cfr250_1 = models.FloatField(default=0.)
    WT_30cfr250_2 = models.FloatField(default=0.)
    WT_30cfr250 = models.FloatField(default=0.)
    WT_api1111_design_1 = models.FloatField(default=0.)
    WT_api1111_design_2 = models.FloatField(default=0.)
    WT_api1111_design = models.FloatField(default=0.)
    WT_api1111_hydro_1 = models.FloatField(default=0.)
    WT_api1111_hydro_2 = models.FloatField(default=0.)
    WT_api1111_hydro = models.FloatField(default=0.)
    WT_api1111 = models.FloatField(default=0.)
    WT_49cfr195_1 = models.FloatField(default=0.)
    WT_49cfr195_2 = models.FloatField(default=0.)
    WT_49cfr195 = models.FloatField(default=0.)
    WT_b31p4_1 = models.FloatField(default=0.)
    WT_b31p4_2 = models.FloatField(default=0.)
    WT_b31p4 = models.FloatField(default=0.)
    WT_49cfr192_1 = models.FloatField(default=0.)
    WT_49cfr192_2 = models.FloatField(default=0.)
    WT_49cfr192 = models.FloatField(default=0.)
    WT_b31p8_1 = models.FloatField(default=0.)
    WT_b31p8_2 = models.FloatField(default=0.)
    WT_b31p8 = models.FloatField(default=0.)
    WT_collapse_1 = models.FloatField(default=0.)
    WT_collapse_2 = models.FloatField(default=0.)
    WT_collapse = models.FloatField(default=0.)

    class Meta:
        ordering = ["-updated_at"]
        permissions = [
            ('Risersizing_permit', 'user can access Risersizing'),
        ]

    def __str__(self):
        return self.project_name

    def get_absolute_url(self):
        return reverse(
                    'risers:Risersizing_single',
                    kwargs={
                        "username": self.user.username,
                        "pk": str(self.pk)
                    }
                )
