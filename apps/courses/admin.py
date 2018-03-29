from django.contrib import admin
from django import forms
from .models import Course, UserCourse
from django.forms import TextInput
from django.db import models

from django.contrib.auth import get_user_model
User = get_user_model()


class CourseForm(forms.ModelForm):

    user = forms.CharField()

    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)
        if 'instance' in kwargs:
            course = kwargs['instance']
            self.fields['user'].initial = ', '.join([uc.user.username for uc in UserCourse.objects.filter(course=course)])
        
        self.fields['user'].widget.attrs['readonly'] = True
        self.fields['user'].widget.attrs['style'] = 'width:500px'
        self.fields['user'].required = False

    def save(self, commit=True, *args, **kwargs):
        return super(CourseForm, self).save(commit=commit, *args, **kwargs)

    class Meta:
        model = Course
        fields = ('course_name', 'is_available', 'topic', 'student_count', 'user')


class CourseAdmin(admin.ModelAdmin):
    fields = ('course_name', 'is_available', 'topic', 'student_count', 'user')
    readonly_fields = ('is_available',)

    form = CourseForm


class UserCourseAdmin(admin.ModelAdmin):
    readonly_fields = ('user',)
    fields = ('course', 'user')

# admin.site.register(Course)
admin.site.register(Course, CourseAdmin)
admin.site.register(UserCourse, UserCourseAdmin)
