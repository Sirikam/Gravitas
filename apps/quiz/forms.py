from django import forms
from .models import Question, Quiz, Quiz_feedback
from django.contrib.admin.widgets import FilteredSelectMultiple


class QuizAdminForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['title', 'description','category','random_order','answers_at_end']

    questions = forms.ModelMultipleChoiceField(
        queryset=Question.objects.all(),
        required=False,
        widget=FilteredSelectMultiple(verbose_name=('Questions'),
                                      is_stacked=False))

    def __init__(self, *args, **kwargs):
        super(QuizAdminForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['questions'].initial = self.instance.question_set.all()

    def save(self, commit=True):
        quiz = super(QuizAdminForm, self).save(commit=False)
        if commit:
            quiz.save()
        if quiz.pk:
            quiz.question_set = self.cleaned_data['questions']
            self.save_m2m()
        return quiz

class FeedbackForm(forms.ModelForm):
     class Meta:
        model = Quiz_feedback
        fields = ['feedback','quiz','rating']