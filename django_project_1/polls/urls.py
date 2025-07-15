from django.urls import path
from polls.views import home_view, question_detail_view, question_results_view, vote_view



urlpatterns = [
    path("", home_view, name="home"),
    path("question/<int:question_id>/", question_detail_view, name="question_detail"),
    path("question/<int:question_id>/vote/", vote_view, name="vote"),
    path("question/<int:question_id>/results/", question_results_view, name="question_results"),
]
