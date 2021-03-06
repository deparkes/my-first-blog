from django.urls import path, include
from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:poll_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:poll_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/up
    path('<int:poll_id>/vote/<str:vote_choice>', views.vote, name='vote'),
]