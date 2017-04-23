# -*- coding: utf-8 -*-
# import random
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import render, get_object_or_404
from apps.quiz.models import Category, Quiz, Sitting, Question, Answer
from apps.quiz.forms import FeedbackForm, QuizAdminForm
from apps.courses.models import *
from apps.documents.models import Document
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    return render(request, 'quiz/quiz_categories.html', {
        'categories': Category.objects.all(),
        'Course':Course.objects.all(),
        'Quiz': Quiz.objects.all(),
        'documents': Document.objects.all(),
    })


@login_required
def view_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    quizzes = Quiz.objects.filter(category=category)
    return render(request, 'quiz/quiz_category.html', {
        'category': category,
        'quizzes': quizzes,
        'Course':Course.objects.all(),
        'Quiz': Quiz.objects.all(),
        'documents': Document.objects.all(),
    })


@login_required
def quiz_take(request, quiz_id):
    # TODO:
    #   * Can there really be more than one sitting? Is that good?
    #   * If there can be several, use filter immediately.
    #   * If there can be only one, use get and do not catch
    #     Sitting.MultipleObjectsReturned since it will never occur

    quiz = Quiz.objects.get(id=quiz_id)


    try:
        previous_sitting = Sitting.objects.get(
            user=request.user,
            quiz=quiz,
            complete=False)

    except Sitting.DoesNotExist:
        #  start new quiz
        sitting = Sitting.objects.new_sitting(request.user, quiz)
        return load_next_question(request, sitting, quiz)

    except Sitting.MultipleObjectsReturned:
        #  if more than one sitting found
        previous_sitting = Sitting.objects.filter(
            user=request.user,
            quiz=quiz,
            complete=False)[0]  # use the first
        return load_next_question(request, previous_sitting, quiz)

    else:
        #  use existing quiz
        return load_next_question(request, previous_sitting, quiz)


@login_required
def load_next_question(request, sitting, quiz):
    """
    Load the next question, including outcome of
    previous question, using the sitting
    """
    progress = sitting.get_current_progress()
    max_score = quiz.question_set.all().count()
    previous = {}

    if 'guess' in request.GET and request.GET['guess']:
        #  if there has been a previous question
        #  returns a dictionary with previous question details
        previous = question_check(request, quiz, sitting)
        sitting.remove_first_question()  # remove the first question
    question_ID = sitting.get_next_question()

    if not question_ID:
        #  no questions left
        return final_result(request, sitting, previous)

    next_question = Question.objects.get(id=question_ID)



    return render_to_response('quiz/question.html',
                              {'quiz': quiz,
                               'question': next_question,
                               'previous': previous,
                               'max_score': max_score,
                               'Quiz': Quiz.objects.all(),
                               'Course': Course.objects.all(),
                               'documents': Document.objects.all(),
                               'progress': progress
                               },
                              #context_instance=RequestContext(request)
                              )


@login_required
def question_check(request, quiz, sitting):
    """
    Check if a question is correct, adds to score if needed
    and return the previous questions details
    """
    # quiz_id = str(quiz.id)
    guess = request.GET['guess']  # id of the guessed answer
    answer = Answer.objects.get(id=guess)
    # question object (only question related to an answer)
    question = answer.question

    if answer.correct:
        outcome = "correct"
        sitting.add_to_score(1)  # add 1 to sitting score.
        sitting.add_to_progress(1)

    else:
        outcome = "incorrect"
        sitting.add_incorrect_question(question)
        sitting.add_to_progress(1)


    if not quiz.answers_at_end:  # display answer after each question
        return {'previous_answer': answer,
                'previous_outcome': outcome, 'previous_question': question, }
    else:  # display all answers at end
        return {}


@login_required
def final_result(request, sitting, previous):
    """
    The result page for a logged in user
    """
    quiz = sitting.quiz
    score = sitting.get_current_score()
    progress = sitting.get_current_progress()
    incorrect = sitting.get_incorrect_questions()
    max_score = quiz.question_set.all().count()
    percent = sitting.get_percent_correct()
    sitting.mark_quiz_complete()  # mark as complete

    if not quiz.exam_paper:  # if we do not plan to store the outcome
        sitting.delete()  # delete the sitting to free up DB space

    if not quiz.answers_at_end:  # answer was shown after each question
        return render_to_response('quiz/result.html', {
            'quiz': quiz,
            'score': score,
            'max_score': max_score,
            'progress': progress,
            'percent': percent,
            'previous': previous,
            'Quiz': Quiz.objects.all(),
            'Course':Course.objects.all(),
            'documents':Document.objects.all()
        },
          #  context_instance=RequestContext(request)
                                  )
    else:  # show all questions and answers
        questions = quiz.question_set.all()
        return render_to_response('quiz/result.html', {
            'quiz': quiz,
            'score': score,
            'max_score': max_score,
            'percent': percent,
            'questions': questions,
            'incorrect_questions': incorrect,
            'Quiz': Quiz.objects.all(),
            'Course': Course.objects.all(),
            'documents': Document.objects.all(),
            'progress': progress
        },
          # context_instance=RequestContext(request)
         )


# for posting a comment
@login_required()
def FeedbackView(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            newfeed = form.save(commit=False)
            newfeed.user = request.user
            newfeed.save()

            #redirect after prossing
            return render(request, 'staticpages/post_succesful.html', {
                'quiz': Quiz.objects.all(),
                'Course': Course.objects.all(),
                'documents': Document.objects.all()
            })

    else:
        form = FeedbackForm() #empty unbound form

        return render(request, 'quiz/quiz_feedback.html', {
            'quiz': Quiz.objects.all(),
            'Course': Course.objects.all(),
            'documents': Document.objects.all(),
            'form': form,
        })