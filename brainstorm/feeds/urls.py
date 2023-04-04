from django.urls import path

from feeds import views

app_name = 'feeds'
urlpatterns = [
    path('new/', views.NewProjectsView.as_view(), name='new'),
    path('best/', views.BestProjectsView.as_view(), name='best'),
    path('speaked/', views.SpeakedProjectsView.as_view(), name='speaked'),
    path('archive/', views.ArchiveProjectsView.as_view(), name='archive/'),
]
