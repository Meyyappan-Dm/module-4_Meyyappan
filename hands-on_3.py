from rest_framework import serializers
from .models import Department, Course, Student, Enrollment


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Course
from .serializers import CourseSerializer


class CourseListView(APIView):

    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

from django.urls import path
from .views import CourseListView, CourseDetailView

urlpatterns = [
    path(
        'courses/',
        CourseListView.as_view(),
        name='course-list'
    ),

    path(
        'courses/<int:pk>/',
        CourseDetailView.as_view(),
        name='course-detail'
    ),
]