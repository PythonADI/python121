from django.contrib import admin


from polls.models import Question, Choice


admin.site.register([Question, Choice])
