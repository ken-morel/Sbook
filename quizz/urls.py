from django.urls import path

from . import views

urlpatterns = [
    path('', views.do_index),
    path('profiles/quizzes/<int:quizzid>.png', views.profiles.quizzes),
    path('quizzes/<int:quizzid>/preview', views.preview_quizz),
]
