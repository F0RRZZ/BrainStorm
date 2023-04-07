from django.urls import path

from feedback import views

app_name = 'feedback'
urlpatterns = [
    path('', views.FeedbackFormView.as_view(), name='feedback'),
    path('success/', views.SuccessPageView.as_view(), name='success'),
]
