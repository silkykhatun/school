"""Serializers for UserManager."""
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Course, UserCourse
User = get_user_model()


class CourseSerializer(serializers.ModelSerializer):
    """Main Serializer for Course Model."""

    class Meta:
        """Meta class for the serializer."""

        model = Course
        fields = ('id', 'course_name', 'is_available', 'student_count',
                  'topic', 'created_at')


class UserCourseSerializer(serializers.ModelSerializer):
    """Main Serializer for UserCourse Model."""

    course = CourseSerializer(read_only=True, many=True)

    class Meta:
        """Meta class for the serializer."""

        model = UserCourse
        fields = ('id', 'course', 'user')
