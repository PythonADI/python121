from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from polls.models import Question

def home_view(request):
    latest_questions = Question.objects.all().order_by("-created_at")[:5]
    return render(
        request, 
        "home.html",
        {"latest_questions": latest_questions}
        )


def question_detail_view(request, question_id):
    # try:
    #     question = Question.objects.get(id=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question not found")
    
    question = get_object_or_404(Question, id=question_id)
    return render(
        request, 
        "question_details.html", 
        {"question": question}
    )


def question_results_view(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    return render(
        request, 
        "question_results.html",
        {"question": question}
    )


def vote_view(request, question_id):
    return HttpResponse(f"Vote for question {question_id} received")
