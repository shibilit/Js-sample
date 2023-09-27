from django.urls import path
from .import views
urlpatterns = [
    path('message', views.message, name="message"),
    path('color', views.color, name="color"),
    path('counter', views.counter, name="counter"),
    path('joke', views.joke, name="joke"),
    path('toggle', views.toggle, name="toggle"),
    path('QA', views.QA, name="QA"),
    path('age_calculator', views.age_calculator, name="age_calculator"),
    path('password', views.password, name="password"),
]

