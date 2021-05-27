from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .forms import *

def ContentView(request):
    email = request.user
    user = User.objects.filter(email=email)[0]
    teacher = Teacher.objects.filter(user=user)[0]
    if request.POST:
        name = request.POST['Name']
        description = request.POST['Description']
        try:
            Content.objects.create(title=name,description=description,teacher=teacher)
            messages.success(request,'Conteúdo criado com sucesso.')
        except:
            messages.error(request,'Erro ao criar conteúdo.')

    contents = Content.objects.filter(teacher=teacher)

    context = {
        'contents': contents
    }

    return render(request, 'content/Content.html',context)
    
@login_required                                        #
def QuestionView(request):
    teacher = Teacher.objects.filter(user=request.user)[0]
    if request.POST:
        title = request.POST['title']
        description = request.POST['Description']
        type_question = request.POST['type_question']
        letter_A = request.POST['a']
        letter_B = request.POST['b']
        letter_C = request.POST['c']
        letter_D = request.POST['d']


    questions = Question.objects.filter(teacher=teacher)
    data = []

    for question in questions:
        if question.is_openQuestion:
            aux = OpenQuestion.objects.filter(question=question.id)[0]
            dirQuestion = {
                "title" : question.title,
                "is_openQuestion" : question.is_openQuestion,
                "description": question.description,
                "link_multimedia": question.link_multimedia,
                "suggestionOfCorrectAnswer": aux.suggestionOfCorrectAnswer
            }
            data.append(dirQuestion)
        else:
            multipleChoices = []
            alternatives = Alternative.objects.filter(question=question.id)
            for alternative in alternatives:
                aux = {
                    "letter": alternative.letter,
                    "description" : alternative.description
                }
                multipleChoices.append(aux)
            dirQuestion = {
                "title" : question.title,
                "is_multipleChoiceQuestion" : question.is_multipleChoiceQuestion,
                "description": question.description,
                "link_multimedia": question.link_multimedia,
                "multipleChoices": multipleChoices
            }
            data.append(dirQuestion)    
    print(data)
    context = {
        'questions': data
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