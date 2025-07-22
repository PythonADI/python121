from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from polls.models import Question, Choice
from django.db.models import F
from django.views import generic

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


def vote_view(request, question_id): # 8:57:05
    question = get_object_or_404(Question, id=question_id)
    try:
        selected_choice = question.choice_set.get(id=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "question_details.html", 
            {
                "question": question,
                "error_message": "Please selected correct choice."
            }
        )

    selected_choice.votes = F("votes") + 1
    selected_choice.save()

    return redirect("question_results", question_id=question.id)


class QuestionListView(generic.ListView):
    template_name = "home.html"
    context_object_name = "latest_questions"

    def get_queryset(self):
        return Question.objects.all().order_by("-created_at")[:5]


class QuestionDetailView(generic.DetailView):
    model = Question
    template_name = "question_details.html"
    

class QuestionResultsView(generic.DetailView):
    model = Question
    template_name = "question_results.html"
