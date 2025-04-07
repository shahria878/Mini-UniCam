from django.urls import path, include
from .views import authView, home
from .views import evolution_view
from .views import admit_view
from .views import result_view
from .views import student_info_view
from .views import course_registration_view, registration_success

urlpatterns = [
 path("", home, name="home"),
 path('admit/', admit_view, name='admit'),
 path("signup/", authView, name="authView"),
 path('result/', result_view, name='result'),
 path('evolution/', evolution_view, name='evolution'),
 path('student-info/', student_info_view, name='student_info'),
 path("accounts/", include("django.contrib.auth.urls")),
 path('course-registration/', course_registration_view, name='course_registration'),
 path('registration-success/', registration_success, name='registration_success'),
]