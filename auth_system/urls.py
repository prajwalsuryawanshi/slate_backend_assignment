from django.urls import path
from .views import RegisterView, LoginView, ForgotPasswordView , ParentDashboardView , SchoolDashboardView , StudentDashboardView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot_password'),
    path('parent-dashboard/', ParentDashboardView.as_view(), name='parent_dashboard'),
    path('student-dashboard/', StudentDashboardView.as_view(), name='parent_dashboard'),
    path('school-dashboard/', SchoolDashboardView.as_view(), name='parent_dashboard'),

]
