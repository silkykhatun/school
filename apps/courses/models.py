from django.db import models

from django.contrib.auth import get_user_model
User = get_user_model()


class Course(models.Model):
    course_name = models.CharField(max_length=50)
    is_available = models.BooleanField(default=True)
    student_count = models.IntegerField(default=0)
    topic = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self, *args, **kwargs):
        return self.course_name


class UserCourse(models.Model):
    user = models.OneToOneField(User)
    course = models.ManyToManyField(Course)

    def save(self, *args, **kwargs):
        print (args)
        print(kwargs)
        super(UserCourse, self).save(*args, **kwargs)

    def __str__(self, *args, **kwargs):
        return "<UserCourse for {0}>".format(self.user.username)
