from django.contrib import admin


from polls.models import Question, Choice


admin.site.register([Choice])


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2
    fields = ["text"]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ["text", "publication_date", "was_published_recently"]
    search_fields = ["text", "choice__text"]
    list_filter = ["publication_date"]
    inlines = [ChoiceInline]

    fieldsets = (
        ("Extra", {
            "fields": ["text"],
        }),
        ("Date Information", {
            "fields": ["publication_date"],
            "classes": ["collapse"],
            "description": "When to display this question.",
        }),
    )
