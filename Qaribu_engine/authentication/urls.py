from django.urls import re_path
from .views import UserRegisterView, UserLoginView
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'authorization'

# Define your views
user_register_list = UserRegisterView.as_view({
    'get': 'list',
    'post': 'create',
})

user_register_detail = UserRegisterView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy',
})

user_login_list = UserLoginView.as_view({
    'get': 'list',
    'post': 'create',
})

user_login_detail = UserLoginView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy',
})



urlpatterns = [
    re_path(r'^register/$', user_register_list, name='userregister-list'),
    re_path(r'^register/(?P<pk>[0-9]+)/$', user_register_detail, name='userregister-detail'),
    
    re_path(r'^login/$', user_login_list, name='userlogin-list'),
    re_path(r'^login/(?P<pk>[0-9]+)/$', user_login_detail, name='userlogin-detail'),
    
    
]

# Optional: You can add format suffix patterns if you need them
urlpatterns = format_suffix_patterns(urlpatterns)