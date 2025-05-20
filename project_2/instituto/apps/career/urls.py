from django.urls import path

from apps.career.views import career_list


urlpatterns = [
    path('', career_list),
]