# books/urls.py
from django.urls import path
from . import views
# from . import plot

app_name='docs'

urlpatterns = [

    path("docs/introduction/", views.docs_intro, name="docs_intro"),

    # path("docs/risers/riser_sizing/", views.docs_riser_sizing,
    #     name="docs_riser_sizing"),

]
