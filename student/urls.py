from django.urls import path
from .views import StudentAchievementView, AddStudentAchievementView

urlpatterns = [
    path('achievements/<int:student_id>/', StudentAchievementView.as_view(), name='student_achievements'),
    path('achievements/add/', AddStudentAchievementView.as_view(), name='add_student_achievement'),
]
