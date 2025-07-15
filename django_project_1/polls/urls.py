from django.urls import path
from polls.views import (
    home_view,
    question_detail_view,
    question_results_view,
    vote_view,
    QuestionListView,
    QuestionDetailView,
    QuestionResultsView
)



urlpatterns = [
    path("", QuestionListView.as_view(), name="home"),
    path("questions/<int:pk>/", QuestionDetailView.as_view(), name="question_detail"),
    path("questions/<int:question_id>/vote/", vote_view, name="vote"),
    path("questions/<int:pk>/results/", QuestionResultsView.as_view(), name="question_results"),
]
