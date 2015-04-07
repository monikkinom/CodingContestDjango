from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Questions(models.Model):
    marks = models.IntegerField(default=0)
    notes = models.TextField(max_length=5000000)
    test_input = models.TextField(max_length=5000000)
    correct_test_output = models.TextField(max_length=5000000)

    def __unicode__(self):
        return "question"

    class Meta:
        verbose_name_plural = 'Questions'


class Examples(models.Model):
    input = models.TextField(max_length=1000)
    output = models.TextField(max_length=1000)
    question = models.ForeignKey(Questions)

    def __unicode__(self):
        return "example"


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    #round_one_score = models.IntegerField(default=0)
    #round_two_score = models.IntegerField(default=0)
    score = models.IntegerField(default=0)
    start_time = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return self.user.username


class Submissions(models.Model):
    user = models.ForeignKey(UserProfile)
    question = models.ForeignKey(Questions)
    submitted_output = models.TextField(default="")
    result = models.NullBooleanField(default=None, null=True)

    def __unicode__(self):
        return "submissions"


class McqQuestions(models.Model):
    marks = models.IntegerField(default=0)
    notes = models.TextField(max_length=100000)
    optiona = models.TextField(max_length=100000)
    optionb = models.TextField(max_length=100000)
    optionc = models.TextField(max_length=100000)
    optiond = models.TextField(max_length=100000)
    correct_ans = models.IntegerField(default=0)

    def __unicode__(self):
        return "mcqquestion"


class McqSubmissions(models.Model):
    user = models.ForeignKey(UserProfile)
    question = models.ForeignKey(McqQuestions)
    submitted_output = models.IntegerField(default=0)
    result = models.NullBooleanField(default=None, null=True)

    def __unicode__(self):
        return "mcqsubmissions"