from django import template
from survey.models import Question

register = template.Library()

def upper(value, n):
	return value.upper()[0:n]

register.filter('upper', upper)

@register.simple_tag
def recent_survey(n=5):
	questions = Question.objects.all().order_by('-created_at')
	return questions[0:n]