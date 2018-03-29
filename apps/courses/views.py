from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Course, UserCourse
# Create your views here.


class CourseView(TemplateView):
    """List all courses."""

    template_name = 'all_courses.html'

    def render_to_response(self, context, **response_kwargs):
        """Render method for the view."""
        context['entries'] = Course.objects.all()
        try:
            user_course = UserCourse.objects.get(user=self.request.user)
            context['enrolled_courses'] = user_course.course.all()
        except:
            context['enrolled_courses'] = []
        response_kwargs.setdefault('content_type', self.content_type)
        return self.response_class(
            request=self.request,
            template=self.get_template_names(),
            context=context,
            **response_kwargs
        )
