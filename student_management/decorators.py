from django.http import HttpResponseRedirect
from django.core.exceptions import PermissionDenied
from django.urls import reverse
from django.contrib.auth.models import User


def admin_only(view_func):
	def wrap(request, *args, **kwargs):
		if request.User.username == 'shoaib':
			return view_func(request,*args, **kwargs)
		else:
			return HttpResponseRedirect(reverse('student_list'))
	return wrap
