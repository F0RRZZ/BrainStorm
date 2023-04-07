from django.urls import path
from tags import views

app_name = 'tags'
urlpatterns = [path('list/', views.TagsListView.as_view(), name='list')]
