from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

def ContentView(request):
    if str(request.method) == 'POST':
        form = ContentModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Content salvo com sucesso')
            form = ContentModelForm()
        else:
            messages.error(request, 'Erro ao salvar Content')
    else:
        form = ContentModelForm()

    context = {
        'form': form
    }
    return render(request, 'content/Content.html',context)

def QuestionView(request):
    if str(request.method) == 'POST':
        form = QuestionModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Question salvo com sucesso')
            form = QuestionModelForm()
        else:
            messages.error(request, 'Erro ao salvar Question')
    else:
        form = QuestionModelForm()

    context = {
        'form': form
    }
    return render(request, 'content/Question.html',context)

def OpenQuestionView(request):
    if str(request.method) == 'POST':
        form = OpenQuestionModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'OpenQuestion salvo com sucesso')
            form = OpenQuestionModelForm()
        else:
            messages.error(request, 'Erro ao salvar OpenQuestion')
    else:
        form = OpenQuestionModelForm()

    context = {
        'form': form
    }
    return render(request, 'content/OpenQuestion.html',context)

def AlternativeView(request):
    if str(request.method) == 'POST':
        form = AlternativeModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Alternative salvo com sucesso')
            form = AlternativeModelForm()
        else:
            messages.error(request, 'Erro ao salvar Alternative')
    else:
        form = AlternativeModelForm()

    context = {
        'form': form
    }
    return render(request, 'content/Alternative.html',context)
    
def MultipleChoiceQuestionView(request):
    if str(request.method) == 'POST':
        form = MultipleChoiceQuestionModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'MultipleChoiceQuestion salvo com sucesso')
            form = MultipleChoiceQuestionModelForm()
        else:
            messages.error(request, 'Erro ao salvar MultipleChoiceQuestion')
    else:
        form = MultipleChoiceQuestionModelForm()

    context = {
        'form': form
    }
    return render(request, 'content/MultipleChoiceQuestion.html',context)

def TaskView(request):
    if str(request.method) == 'POST':
        form = TaskModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task salvo com sucesso')
            form = TaskModelForm()
        else:
            messages.error(request, 'Erro ao salvar Task')
    else:
        form = TaskModelForm()

    context = {
        'form': form
    }
    return render(request, 'content/Task.html',context)
    
def ActivityTeacherView(request):
    if str(request.method) == 'POST':
        form = ActivityTeacherModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'ActivityTeacher salvo com sucesso')
            form = ActivityTeacherModelForm()
        else:
            messages.error(request, 'Erro ao salvar ActivityTeacher')
    else:
        form = ActivityTeacherModelForm()

    context = {
        'form': form
    }
    return render(request, 'content/ActivityTeacher.html',context)

def ActivityView(request):
    if str(request.method) == 'POST':
        form = ActivityModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Activity salvo com sucesso')
            form = ActivityModelForm()
        else:
            messages.error(request, 'Erro ao salvar Activity')
    else:
        form = ActivityModelForm()

    context = {
        'form': form
    }
    return render(request, 'content/Activity.html',context)
    
def ActivityRealizationView(request):
    if str(request.method) == 'POST':
        form = ActivityRealizationModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'ActivityRealization salvo com sucesso')
            form = ActivityRealizationModelForm()
        else:
            messages.error(request, 'Erro ao salvar ActivityRealization')
    else:
        form = ActivityRealizationModelForm()

    context = {
        'form': form
    }
    return render(request, 'content/ActivityRealization.html',context)

def ActivityRealizationTeacherView(request):
    if str(request.method) == 'POST':
        form = ActivityRealizationTeacherModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'ActivityRealizationTeacher salvo com sucesso')
            form = ActivityRealizationTeacherModelForm()
        else:
            messages.error(request, 'Erro ao salvar ActivityRealizationTeacher')
    else:
        form = ActivityRealizationTeacherModelForm()

    context = {
        'form': form
    }
    return render(request, 'content/ActivityRealizationTeacher.html',context)
    
def AnswerView(request):
    if str(request.method) == 'POST':
        form = AnswerModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Answer salvo com sucesso')
            form = AnswerModelForm()
        else:
            messages.error(request, 'Erro ao salvar Answer')
    else:
        form = AnswerModelForm()

    context = {
        'form': form
    }
    return render(request, 'content/Answer.html',context)

def AnswerTeacherView(request):
    if str(request.method) == 'POST':
        form = AnswerTeacherModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'AnswerTeacher salvo com sucesso')
            form = AnswerTeacherModelForm()
        else:
            messages.error(request, 'Erro ao salvar AnswerTeacher')
    else:
        form = AnswerTeacherModelForm()

    context = {
        'form': form
    }
    return render(request, 'content/AnswerTeacher.html',context)
    
def AnswerMultipleChoiceView(request):
    if str(request.method) == 'POST':
        form = AnswerMultipleChoiceModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'AnswerMultipleChoice salvo com sucesso')
            form = AnswerMultipleChoiceModelForm()
        else:
            messages.error(request, 'Erro ao salvar AnswerMultipleChoice')
    else:
        form = AnswerMultipleChoiceModelForm()

    context = {
        'form': form
    }
    return render(request, 'content/AnswerMultipleChoice.html',context)

def AnswerTeacherMultipleChoiceView(request):
    if str(request.method) == 'POST':
        form = AnswerTeacherMultipleChoiceModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'AnswerTeacherMultipleChoice salvo com sucesso')
            form = AnswerTeacherMultipleChoiceModelForm()
        else:
            messages.error(request, 'Erro ao salvar AnswerTeacherMultipleChoice')
    else:
        form =AnswerTeacherMultipleChoiceModelForm()

    context = {
        'form': form
    }
    return render(request, 'content/AnswerTeacherMultipleChoice.html',context)