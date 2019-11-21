from django.urls import path
from .views import *

urlpatterns = [
   #path('poll/',views.poll_list),
   path('',PollList.as_view(), name='poll_list'),
   path('<int:pk>/',PollDetail.as_view(), name="poll_view"), 
   path('vote/<int:pid>/',PollVote.as_view(), name='poll_vote'),
   path('create/',PollCreate.as_view(), name='poll_create'),
   path('<int:pk>/update/',PollUpdate.as_view(), name="poll_edit"),
   path('<int:pid>/create/' ,OptionCreate.as_view(), name='option_create'),
   path('option/<int:pk>/' ,OptionEdit.as_view(), name='option_edit'),
   path('option/<int:pk>/delete/',OptionDelete.as_view(), name='option_delete'),
   path('<int:pk>/delete/',PollDelete.as_view(), name='poll_delete'),
]