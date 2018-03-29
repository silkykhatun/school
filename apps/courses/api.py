from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserCourse, Course
from .serializers import UserCourseSerializer
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import status

from django.contrib.auth import get_user_model
User = get_user_model()


class EnrollCourseView(APIView, LoginRequiredMixin):
    """Enroll into a course."""

    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def post(self, request, format=None):
        """To enroll a course."""
        course_id = request.POST.get('id')
        course = Course.objects.get(id=course_id)
        if course.student_count > 4 or course.student_count < 0:
            response = {'success': False, 'message': 'Course full.'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        user_course, created = UserCourse.objects.get_or_create(user=request.user)

        if course in user_course.course.all():
            response = {'success': False, 'message': 'You are already enrolled.'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        try:
            user_course.course = [course]
            user_course.save()
            course.student_count += 1
            if course.student_count > 4:
                course.is_available = False
            course.save()
            response = {
                'success': True, 'message': 'Course Enrolled',
                'data': {
                    'count': course.student_count,
                    'available': 'Yes' if course.is_available else 'No'
                }
            }
            return Response(response, status=status.HTTP_201_CREATED)
        except:
            return Response(
                {'success': False, 'message': 'Failed to enroll Course'},
                status=status.HTTP_400_BAD_REQUEST
            )


class QuitCourseView(APIView, LoginRequiredMixin):
    """Quit course."""

    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def post(self, request, format=None):
        """Post to quit course."""
        course_id = request.POST.get('id')
        course = Course.objects.get(id=course_id)

        user_course, created = UserCourse.objects.get_or_create(user=request.user)
        if course in user_course.course.all():
            try:
                user_course.course.remove(course)
                user_course.save()
                course.student_count -= 1
                if course.student_count < 5:
                    course.is_available = True
                course.save()
                response = {
                    'success': True, 'message': 'Succesfully quit course',
                    'data': {
                        'count': course.student_count,
                        'available': 'Yes' if course.is_available else 'No'
                    }
                }
                return Response(response, status=status.HTTP_201_CREATED)
            except:
                return Response(
                    {'success': False, 'message': 'Failed to quit Course'},
                    status=status.HTTP_400_BAD_REQUEST
                )
        else:
            response = {'success': False, 'message': 'You need to be in the course to quit it'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
