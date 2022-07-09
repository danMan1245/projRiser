from django import forms

from . import models
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit
from crispy_forms.bootstrap import Accordion, AccordionGroup
class RisersizingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RisersizingForm, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
       Accordion(
    AccordionGroup('First Group',
        'project_name','project_description','pipe_category','pipe_OD',
                'pipe_WT_corr','pipe_base_WD','fluid_density','hydro_density',
                'outer_density','pressure_refer',
        active=False,
    ),
    AccordionGroup('Second Group',
        'WD_refer','pressure_surf',
                'pressure_base','hydro_factor','SMYS','SMUTS','F_E','F_hoop',
                'F_hoop_gas','F_hydro','k_burst','Tp','E_YM','PR','F_c',
        active=False,
    )
       )
        #  Fieldset('project_name','project_description','pipe_category','pipe_OD',
          #    'pipe_WT_corr','pipe_base_WD','fluid_density','hydro_density',
          #      'outer_density','pressure_refer','WD_refer','pressure_surf',
          #      'pressure_base','hydro_factor','SMYS','SMUTS','F_E','F_hoop',
           #     'F_hoop_gas','F_hydro','k_burst','Tp','E_YM','PR','F_c')
        )
        # You can dynamically adjust your layout
        
    class Meta:
        model = models.Risersizing
        fields = '__all__'
    #