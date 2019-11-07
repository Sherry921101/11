from django.urls import path
from . import views

urlpatterns = [
   #path('poll/',views.poll_list),
   path('poll/', views.PollList.as_view()),
   path('poll/<int:pk>/',views.PollDetail.as_view()),
   path('poll/vote/<int:oid>/',views.PollVote.as_view()),
   path('<int:pk>/update/', views.PollUpdate.as_view()),
]