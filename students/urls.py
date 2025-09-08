from django.urls import path, include
from . import views
from rest_framework import routers
from .views import StudentViewSet

app_name = 'students'

router = routers.DefaultRouter()
router.register(r'students', StudentViewSet, basename='student')

urlpatterns = [
    # HTML routes
    path('', views.student_list_html, name='list_html'),
    path('add/', views.add_student, name='add'),
    # API routes under api/
    path('api/', include(router.urls)),
]
