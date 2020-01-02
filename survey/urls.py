from django.urls import path
from survey.views import *

urlpatterns = [
	path('', survey_list, name='survey_list'),
	path('<int:id>/details/', details, name='survey_details'),
	path('<int:id>/delete/', delete, name='survey_delete'),
	path('add/', add, name='add'),
    path('<int:question_id>/', vote_survey, name="vote_survey"),
	path('<int:pk>/results/', ResultsView.as_view(), name='results'),


]