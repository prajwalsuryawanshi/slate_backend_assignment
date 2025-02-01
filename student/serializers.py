from rest_framework import serializers
from auth_system.models import StudentAchievement

class StudentAchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAchievement
        fields = ['student_id', 'name', 'school_name', 'achievements']
