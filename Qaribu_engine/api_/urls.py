from django.urls import path
from .views import FileInquiryView

urlpatterns = [
    path('file-inquiry/', FileInquiryView.as_view(), name='file-inquiry'),
]


