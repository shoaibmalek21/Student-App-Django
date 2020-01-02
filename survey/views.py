from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponse
from survey.models import *
from django.http import Http404, HttpResponseRedirect
from survey.forms import *
from django.urls import reverse
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from student_management.decorators import admin_only
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required(login_url='/login/')
def survey_list(request):
	context = {}
	questions = Question.objects.all()
	context['title'] = 'survey'
	context['questions'] = questions
	return render(request,"survey/index.html",context)

@login_required(login_url='/login/')
def details(request,id=None):
	context = {}
	try:
		question = Question.objects.get(id=id)
	except:
		raise Http404
	context['question'] = question
	return render(request,"survey/details.html",context)

@login_required(login_url='/login/')
def survey(request,id=None):
	if request.method == 'GET':
		context = {}
		try:
			question = Question.objects.get(id=id)
		except:
			raise Http404
		context['question'] = question
		return render(request,"survey/survey.html",context)
	if request.method == 'POST':
		user_id = 1
		print(request.POST)
		data = request.POST
		res = Answer.objects.create(user_id=user_id, choice_id=data['choice'])
		if res:
			return HttpResponse('Your vote is done successfully.')
		else:
			return HttpResponse('Your vote is not done successfully.')

@login_required(login_url='/login/')
def delete(request,id=None):
	question = get_object_or_404(Question,id=id)
	if request.method == 'POST':
		question.delete()
		return HttpResponseRedirect(reverse('survey_list'))
	else:
		context = {}
		context['question'] = question
		return render(request,'survey/delete.html',context)

@login_required(login_url='/login/')
# @role_required(allowed_roles=['Admin','HR'])
# @admin_only
def add(request,id=None):
	context = {}
	if request.method == 'POST':
		survey_form = SurveyForm(request.POST)
		# context['user_form'] = user_form
		if survey_form.is_valid():
			survey_form.save()
			return HttpResponseRedirect(reverse('survey_list'))
		else:
			return render(request,'survey/add.html', {'survey_form':survey_form})
	else:
			survey_form = SurveyForm()
	return render(request,'survey/add.html',{'survey_form':survey_form})

@login_required(login_url="/login/")
def vote_survey(request, question_id):
    context = {}
    try:
        question = Question.objects.get(id=id)
    except:
        raise Http404
    context["question"] = question

    if request.method == "POST":
        user_id = 1
        print(request.POST)
        data = request.POST
        ret = Answer.objects.create(user_id=user_id, choice_id=data['choice'])
        if ret:
            return HttpResponseRedirect(reverse('details', args=[question.id]))
        else:
            context["error"] = "Your vote is not done successfully"
            return render(request, 'survey/survey.html', context)
    else:
        return render(request, 'survey/survey.html', context)


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'survey/results.html', {'question': question})
