from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from .models import *
from .forms import *

@login_required                                        #
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

    contents = Content.objects.filter(teacher=teacher).order_by('-id')

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
        suggestionOfCorrectAnswer = request.POST['suggestionOfCorrectAnswer']
        letter_A = request.POST['a']
        letter_B = request.POST['b']
        letter_C = request.POST['c']
        letter_D = request.POST['d']

        if type_question == 'is_openQuestion':
            question = Question.objects.create(title=title,description=description,is_openQuestion=True,is_multipleChoiceQuestion=False,teacher=teacher)
            OpenQuestion.objects.create(question=question,suggestionOfCorrectAnswer=suggestionOfCorrectAnswer)
        else:
            question = Question.objects.create(title=title,description=description,is_openQuestion=False,is_multipleChoiceQuestion=True,teacher=teacher)
            Alternative.objects.create(question=question,letter='A',description=letter_A)
            Alternative.objects.create(question=question,letter='B',description=letter_B)
            Alternative.objects.create(question=question,letter='C',description=letter_C)
            Alternative.objects.create(question=question,letter='D',description=letter_D)

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
    #print(data)
    context = {
        'questions': data
    }
    return render(request, 'content/Question.html',context)

@login_required                                        #
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

@login_required                                        #
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
    
@login_required                                        #
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

@login_required                                        #
def TaskView(request):
    teacher = Teacher.objects.filter(user=request.user)[0]
    if request.POST:
        title = request.POST['title']
        description = request.POST['description']
        type_question = request.POST['type_question']
        type_question2 = request.POST['type_question2']
        type_question3 = request.POST['type_question3']
        type_location = request.POST['type_location']
        location = Location.objects.filter(pk=type_location)[0]
        task =  Task.objects.create(title=title,description=description,location=location,teacher=teacher)
        if type_question != '':
            question = Question.objects.filter(pk=type_question)[0]
            task.questions.add(question)
        if type_question2 != '':
            question = Question.objects.filter(pk=type_question2)[0]
            task.questions.add(question)
        if type_question3 != '':
            question = Question.objects.filter(pk=type_question3)[0]
            task.questions.add(question)        


    locations = Location.objects.filter(teacher=teacher)
    questions = Question.objects.filter(teacher=teacher)
    tasks = Task.objects.filter(teacher=teacher).order_by('-id')
    print(tasks[0].questions.all())

    context = {
        'teacher': teacher,
        'locations': locations,
        'questions': questions,
        'tasks': tasks
    }
    return render(request, 'content/Task.html',context)

@login_required      
def ActivityTeacherView(request):
    teacher = Teacher.objects.filter(user=request.user)[0]
    if request.POST:
        title = request.POST['title']
        description = request.POST['description']

        type_course = request.POST['type_course']
        course = CourseTeacher.objects.filter(pk=type_course)[0]

        type_classe = request.POST['type_classe']
        classe = ClassTeacher.objects.filter(pk=type_classe)[0]

        type_content = request.POST['type_content']
        content = Content.objects.filter(pk=type_content)[0]

        type_task = request.POST['type_task']
        type_task2 = request.POST['type_task2']
        type_task3 = request.POST['type_task3']
        type_task4 = request.POST['type_task4']
        type_task5 = request.POST['type_task5']
        type_task6 = request.POST['type_task6']
        type_task7 = request.POST['type_task7']
        type_task8 = request.POST['type_task8']
        type_task9 = request.POST['type_task9']
        type_task10 = request.POST['type_task10']

        activity = ActivityTeacher.objects.create(title=title,description=description,course=course,class_id=classe,content=content,teacher=teacher)

        if type_task != '':
            task = Task.objects.filter(pk=type_task)[0]
            activity.tasks.add(task)
        if type_task2 != '':
            task = Task.objects.filter(pk=type_task2)[0]
            activity.tasks.add(task)
        if type_task3 != '':
            task = Task.objects.filter(pk=type_task3)[0]
            activity.tasks.add(task)
        if type_task4 != '':
            task = Task.objects.filter(pk=type_task4)[0]
            activity.tasks.add(task)                                    
        if type_task5 != '':
            task = Task.objects.filter(pk=type_task5)[0]
            activity.tasks.add(task)
        if type_task6 != '':
            task = Task.objects.filter(pk=type_task6)[0]
            activity.tasks.add(task)
        if type_task7 != '':
            task = Task.objects.filter(pk=type_task7)[0]
            activity.tasks.add(task)
        if type_task8 != '':
            task = Task.objects.filter(pk=type_task8)[0]
            activity.tasks.add(task)
        if type_task9 != '':
            task = Task.objects.filter(pk=type_task9)[0]
            activity.tasks.add(task)
        if type_task10 != '':
            task = Task.objects.filter(pk=type_task10)[0]
            activity.tasks.add(task)

    contents =  Content.objects.filter(teacher=teacher).order_by('-id')
    course = CourseTeacher.objects.filter(teacher=teacher).order_by('-id')
    classes = ClassTeacher.objects.filter(teacher=teacher).order_by('-id')
    tasks = Task.objects.filter(teacher=teacher).order_by('-id')
    activities = ActivityTeacher.objects.filter(teacher=teacher).order_by('-id')

    context = {
        'teacher': teacher,
        'tasks': tasks,
        'contents': contents,
        'classes': classes,
        'courses': course,
        'activities': activities
    }

    return render(request, 'content/ActivityTeacher.html',context)

@login_required  
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

@login_required      
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

@login_required  
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

@login_required      
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

@login_required  
def AnswerTeacherView(request):

    teacher = Teacher.objects.filter(user=request.user)[0]
    data = []
    activity_data = []
    activities = ActivityTeacher.objects.filter(teacher=teacher).order_by('-id')

    for activity in activities:
        activity_data = []
        realizations = ActivityRealizationTeacher.objects.filter(activity=activity.id)  
        for actRealization in realizations:
            student = actRealization.student
            activity = ActivityTeacher.objects.filter(pk=actRealization.activity_id)[0]
            tasks = activity.tasks.all()
            print('///////////////////////////////\n')
            print(tasks)
            print('///////////////////////////////\n')
            for task in tasks:
                questions = task.questions.all()
                for question in questions:
                    if question.is_openQuestion:
 
                        answer = AnswerTeacher.objects.filter(question=question.id,activityRealization=actRealization.id)
                        try: 
                            answer_aux = answer[0].answer
                        except:
                            answer_aux = ''
                        aux = {
                            'student' : student,
                            'task' : task,
                            'question' : question,
                            'answer': answer_aux,
                            'activity': activity
                        }
                        activity_data.append(aux)
                    if question.is_multipleChoiceQuestion:
                    	try:
                            answer = AnswerTeacherMultipleChoice.objects.filter(question=question.id,activityRealization=actRealization.id)[0]
                            print("\n\n\n\n")
                            print(answer.alternative)
                            print("\n\n\n\n")
                            aux = {
                                'student' : student,
                                'task' : task,
                                'question' : question,
                                'answer': answer.alternative,
                                'activity': activity
                            }
                            activity_data.append(aux)
                        except:
                            aux = {
                                        'student' : student,
                                        'task' : task,
                                        'question' : question,
                                        'answer': "",
                                        'activity': activity
                            }
                            activity_data.append(aux)

		        
        data.append(activity_data)

    print(data)
    context = {
        'data': data,
        'activities': activities
    }

    #print("\n\n\n\n\n\n\n\n\n\n")
    #print(context)
    return render(request, 'content/AnswerTeacher.html',context)

@login_required      
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

@login_required  
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
