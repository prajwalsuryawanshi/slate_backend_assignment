from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from auth_system.models import StudentAchievement
from .permissions import CanAccessStudentAchievements
from .serializers import StudentAchievementSerializer  


class StudentAchievementView(APIView):
    permission_classes = [IsAuthenticated, CanAccessStudentAchievements]

    def get(self, request, student_id):
        try:
            achievements = StudentAchievement.objects.filter(student_id=student_id)
            
            if not achievements.exists():
                return Response({'error': 'Student achievements not found'}, status=404)
            
            serializer = StudentAchievementSerializer(achievements, many=True)
            return Response(serializer.data)
            
        except Exception as e:
            return Response({'error': str(e)}, status=400)

from .permissions import CanManageStudentAchievements

class AddStudentAchievementView(APIView):
    permission_classes = [IsAuthenticated, CanManageStudentAchievements]

    def post(self, request):
        student_id = request.data.get('student_id')
        name = request.data.get('name')
        school_name = request.data.get('school_name')
        achievement = request.data.get('achievement')

        if not all([student_id, name, school_name, achievement]):
            return Response({'error': 'All fields are required'}, status=400)

        new_achievement = StudentAchievement.objects.create(
            student_id=student_id,
            name=name,
            school_name=school_name,
            achievements=achievement
        )

        return Response({
            'message': 'Achievement added successfully',
            'achievement_id': new_achievement.id
        }, status=201)
