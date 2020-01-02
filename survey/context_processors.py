from survey.models import Question
def survey_count(request):
	count = Question.objects.count()
	return {"survey_count": count}