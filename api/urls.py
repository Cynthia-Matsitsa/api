from django.urls import path
from views import StudentListView
urlpatterns = [
    path("students/",StudentListViews.as_view(),
         name="student_list_views")
    
]
school/urls.py
from django.urls import pat, include
