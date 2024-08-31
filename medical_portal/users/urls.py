from django.urls import path
from .views import signup_view, user_type_selection, redirect_to_signup, login_view, patient_dashboard, doctor_dashboard

urlpatterns = [
    path('select/', user_type_selection, name='user_type_selection'),
    path('signup/patient/', signup_view, name='patient_signup'),
    path('signup/doctor/', signup_view, name='doctor_signup'),
    path('signup/redirect/<str:user_type>/', redirect_to_signup, name='redirect_to_signup'),
    path('login/', login_view, name='login'),
    path('dashboard/patient/', patient_dashboard, name='patient_dashboard'),  # Patient dashboard URL
    path('dashboard/doctor/', doctor_dashboard, name='doctor_dashboard'),  # Doctor dashboard URL
]
