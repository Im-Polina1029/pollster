from django.urls import path
from app.change_settings_of_user import views


url_patterns_of_changes_in_user_profile = [
    path('nickname', views.request_on_change_the_nickname),
    path('number_of_phone', views.request_on_change_the_number_of_phone),
    path('date_of_birth', views.request_on_change_the_date_of_birth),
    path('tags_of_user', views.request_on_change_the_tags),
    path('email', views.request_on_change_the_login)
]