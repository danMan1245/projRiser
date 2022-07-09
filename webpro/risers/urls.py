# books/urls.py
from django.urls import path
from . import views
# from . import plot

app_name='risers'

urlpatterns = [

    path("risers/Risersizing/new", views.RisersizingCreateView.as_view(),
        name="Risersizing_create"),
    path("risers/Risersizing/<username>/<int:pk>/",
        views.RisersizingDetailView.as_view(),name="Risersizing_single"),
    path('risers/Risersizing/<username>/<int:pk>/edit/',
        views.RisersizingUpdateView.as_view(), name='Risersizing_edit'),

]
