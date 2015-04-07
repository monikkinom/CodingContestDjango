from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import user_passes_test
from acm.models import *
from django.contrib.auth import logout
import hashlib
import datetime
import logging
from django.utils import timezone
from django.core.exceptions import *
import random
import string
TIMEOUTTIME = 60

@user_passes_test(lambda u: u.is_superuser)
def registerteam(request):
    if request.POST:
        teamname = request.POST.get('teamname')
        password = request.POST.get('randompass')
    else:
        randompass = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(10)])
        return render(request, 'register.html', {'randompass': randompass})


def timedout(user):
    up = UserProfile.objects.get(user=user)
    if up.start_time is not None:
        st = up.start_time + datetime.timedelta(minutes=TIMEOUTTIME)
        now = timezone.make_aware(datetime.datetime.now(), timezone.get_default_timezone())
        if now > st:
            return True
        else:
            return False
    else:
        return False


@csrf_exempt
def signin(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/home/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                if timedout(user):
                    return HttpResponseRedirect('/end/')
                return HttpResponseRedirect('/instructions/')
            else:
                return render(request, 'login.html', {'account_disabled': True})
        else:
            return render(request, 'login.html', {'wrong_details': True})
    else:
        return render(request, 'login.html', {'wrong_details': False})


@login_required(login_url='/')
def instructions(request):
    return render(request, 'instructions.html')


@login_required(login_url='/')
def home(request):
    request.session['timeout'] = TIMEOUTTIME
    username = request.user.username
    if timedout(request.user):
        return HttpResponseRedirect('/end/')
    user = UserProfile.objects.get(user=User.objects.get(username=username))
    if not user.start_time:
        user.start_time = str(datetime.datetime.now())
        user.save()
    if request.session.get('starttime') is None:
        request.session['starttime'] = str(user.start_time)
    solved_list = []
    mcq_solved_list = []
    mcq_questions_list = McqQuestions.objects.all()
    questions_list = Questions.objects.all()
    for question in questions_list:
        try:
            submissions = Submissions.objects.get_or_create(user=user, question=question)
        except MultipleObjectsReturned:
            submissions = Submissions.objects.get(user=user, question=question)
        solved_list.append(submissions[0].result)
    questions_list = zip(questions_list, solved_list)
    for question in mcq_questions_list:
        try:
            submissions = McqSubmissions.objects.get_or_create(user=user, question=question)
        except MultipleObjectsReturned:
            submissions = McqSubmissions.objects.get(user=user, question=question)
        mcq_solved_list.append(submissions[0].result)
    mcq_questions_list = zip(mcq_questions_list, mcq_solved_list)
    return render(request, 'home.html', {'username': username, 'questions_list': questions_list, 'mcq_questions_list': mcq_questions_list})


@login_required(login_url='/')
@csrf_exempt
def questions(request):
    request.session['timeout'] = TIMEOUTTIME
    if request.POST:
        q_no = request.POST.get('no')
    else:
        q_no = request.GET.get('no')
    try:
        question = Questions.objects.get(pk=q_no)
    except:
        return render_to_response(request, 'error.html')
    if request.POST:
        submitted_ans = request.POST.get('answer', '').strip()
        correct_ans = question.correct_test_output.strip()
        username = request.user.username
        user = UserProfile.objects.get(user=User.objects.get(username=username))
        try:
            submissions = Submissions.objects.get_or_create(user=user, question=question)
        except MultipleObjectsReturned:
            submissions = Submissions.objects.get(user=user, question=question)
        submissions[0].submitted_output = submitted_ans
        if hashlib.md5(submitted_ans).hexdigest() == hashlib.md5(correct_ans).hexdigest():
            submissions[0].result = True
        else:
            submissions[0].result = False
        submissions[0].save()
        #return HttpResponse(hashlib.md5(correct_ans).hexdigest()+"<br>"+hashlib.md5(submitted_ans).hexdigest())
        return HttpResponseRedirect('/home/')
    user = request.user
    examples = Examples.objects.filter(question=question)
    return render(request, 'question_view.html', {'question': question, 'examples': examples, 'user': user})


@login_required(login_url='/')
@csrf_exempt
def mcqquestions(request):
    request.session['timeout'] = TIMEOUTTIME
    if request.POST:
        q_no = request.POST.get('no')
    else:
        q_no = request.GET.get('no')
    try:
        question = McqQuestions.objects.get(pk=q_no)
    except:
        return render_to_response(request, 'error.html')
    if request.POST:
        submitted_ans = request.POST.get('answer', '').strip()
        correct_ans = str(question.correct_ans).strip()
        username = request.user.username
        user = UserProfile.objects.get(user=User.objects.get(username=username))
        try:
            submissions = McqSubmissions.objects.get_or_create(user=user, question=question)
        except MultipleObjectsReturned:
            submissions = McqSubmissions.objects.get(user=user, question=question)
        submissions[0].submitted_output = submitted_ans
        if hashlib.md5(submitted_ans).hexdigest() == hashlib.md5(correct_ans).hexdigest():
            submissions[0].result = True
        else:
            submissions[0].result = False
        submissions[0].save()
        return HttpResponseRedirect('/home/')
    user = request.user
    return render(request, 'mcq_question_view.html', {'question': question, 'user': user})


def calc_ranks(request):
    participants = UserProfile.objects.all()
    for participant in participants:
        submissions = Submissions.objects.filter(user=participant)
        participant.score = 0
        for submission in submissions:
            participant.score += submission.question.marks if submission.result is True else 0
        submissions = McqSubmissions.objects.filter(user=participant)
        for submission in submissions:
            participant.score += submission.question.marks if submission.result is True else 0
        participant.save()


def view_ranks(request):
    request.session['timeout'] = TIMEOUTTIME
    calc_ranks(request)
    ranks = UserProfile.objects.order_by('-score')[:]
    return render(request, 'view_ranks.html', {'rank_list': ranks})


@login_required(login_url='/')
def signout(request):
    logout(request)
    return HttpResponseRedirect("/")


@login_required(login_url='/')
def end(request):
    if request.user.is_authenticated() and not request.user.is_superuser:
        request.user.is_active = False
        request.user.save()
    return HttpResponseRedirect('/logout/')