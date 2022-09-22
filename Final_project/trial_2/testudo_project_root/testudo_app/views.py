
from select import select
from django.shortcuts import render,redirect
from django.db import models
from .models import CourseList, CourseInfo, Professors
import requests,json
from testudo_app.models import CourseInfo, UserSavedCourses
from django.db.models import Q
import itertools
import webbrowser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages, auth



def homepage(request):

    user=None
    dept=CourseInfo.objects.values_list('dept_id', 'department').order_by('course_id')    
    department_list=[]
    dept_id_list={}
    for i in dept:
        if i not in department_list:
            department_list.append(i)
        if i not in dept_id_list and i[0]!='USLT':
            dept_id_list[i[0]]= i[1]

    dept_list_1=department_list[:93]
    dept_id_list_1=[]
    dept_id_dict_1=dict(itertools.islice(dept_id_list.items(),93))
    for key, value in dept_id_dict_1.items():
        string= key +" "+" "+ value
        dept_id_list_1.append(string)

    dept_list_2=department_list[93:]
    dept_id_list_2=[]

    dept_id_dict_2=dict(itertools.islice(dept_id_list.items(),94,185 ))


    for key, value in dept_id_dict_2.items():
        string= key +" "+" "+ value
        dept_id_list_2.append(string)


    from .choices import term_choices, credit_choices

    context={'user':user,
             'dept_list_1':dept_list_1,
             'dept_list_2':dept_list_2,
             'dept_id_list_1':dept_id_list_1,
             'dept_id_list_2':dept_id_list_2,
             'term_choices': term_choices,
             'credit_choices':credit_choices}

    return render(request,'homepage.html',context)

def search(request,user):

    queryset_list=CourseInfo.objects.all().order_by('course_id')

    if 'department' in request.GET:
        dept_id= request.GET['department']
        if dept_id:
            queryset_list=queryset_list.filter(course_id__icontains=dept_id)
    
    if 'course_no' in request.GET:
        course_no= request.GET['course_no']
        if course_no:
            queryset_list=queryset_list.filter(course_id__icontains=course_no)


    if 'credits' in request.GET:
        credit=request.GET['credits']
        if credit:
            queryset_list=queryset_list.filter(credits=credit)

    from .choices import term_choices, credit_choices
    context={
        'user':user,
        'courses':queryset_list,
        'values':request.GET,
        'term_choices': term_choices,
        'credit_choices':credit_choices
    }

    return render(request,'search.html',context)

def search_no_user(request):
    user=None
    queryset_list=CourseInfo.objects.all().order_by('course_id')

    if 'department' in request.GET:
        dept_id= request.GET['department']
        if dept_id:
            queryset_list=queryset_list.filter(course_id__icontains=dept_id)
    
    if 'course_no' in request.GET:
        course_no= request.GET['course_no']
        if course_no:
            queryset_list=queryset_list.filter(course_id__icontains=course_no)


    if 'credits' in request.GET:
        credit=request.GET['credits']
        if credit:
            queryset_list=queryset_list.filter(credits=credit)

    from .choices import term_choices, credit_choices
    context={
        'user':user,
        'courses':queryset_list,
        'values':request.GET,
        'term_choices': term_choices,
        'credit_choices':credit_choices
    }

    return render(request,'search.html',context)
def search_gen_ed(request,user):
    queryset_list=CourseInfo.objects.all().order_by('course_id')

    querylist_1=queryset_list.filter(Q(gen_ed__icontains='FSAW')| Q(gen_ed__icontains='DVUP')| Q(gen_ed__icontains='FSAR')| Q(gen_ed__icontains='FSMA')| Q(gen_ed__icontains='FSOC')| Q(gen_ed__icontains='FSPW')| Q(gen_ed__icontains='DSHU')| Q(gen_ed__icontains='DSNS')| Q(gen_ed__icontains='DSNL')| Q(gen_ed__icontains='DSSP')| Q(gen_ed__icontains='DVCC')| Q(gen_ed__icontains='DVUP')| Q(gen_ed__icontains='SCIS'))
    if 'department' in request.GET:
        dept_id= request.GET['department']
        if dept_id:
            querylist_1=querylist_1.filter(course_id__icontains=dept_id)
    
    if 'course_no' in request.GET:
        course_no= request.GET['course_no']
        if course_no:
            querylist_1=querylist_1.filter(course_id__icontains=course_no)

    if 'credits' in request.GET:
        credit=request.GET['credits']
        if credit:
            querylist_1=querylist_1.filter(credits=credit)

    if 'gen_ed' in request.GET:
        gen_ed_choice=request.GET['gen_ed']
        if gen_ed_choice:
            querylist_1=querylist_1.filter(gen_ed__icontains=gen_ed_choice)

    from .choices import term_choices, credit_choices, gen_ed_choices

    context={
        'user':user,
        'courses':querylist_1,
        'values':request.GET,
        'term_choices': term_choices,
        'credit_choices':credit_choices,
        'gen_ed_choices':gen_ed_choices,
    }
    return render(request, 'gen_ed_search.html',context)

def search_gen_ed_no_user(request):
    user=None
    queryset_list=CourseInfo.objects.all().order_by('course_id')

    querylist_1=queryset_list.filter(Q(gen_ed__icontains='FSAW')| Q(gen_ed__icontains='DVUP')| Q(gen_ed__icontains='FSAR')| Q(gen_ed__icontains='FSMA')| Q(gen_ed__icontains='FSOC')| Q(gen_ed__icontains='FSPW')| Q(gen_ed__icontains='DSHU')| Q(gen_ed__icontains='DSNS')| Q(gen_ed__icontains='DSNL')| Q(gen_ed__icontains='DSSP')| Q(gen_ed__icontains='DVCC')| Q(gen_ed__icontains='DVUP')| Q(gen_ed__icontains='SCIS'))
    if 'department' in request.GET:
        dept_id= request.GET['department']
        if dept_id:
            querylist_1=querylist_1.filter(course_id__icontains=dept_id)
    
    if 'course_no' in request.GET:
        course_no= request.GET['course_no']
        if course_no:
            querylist_1=querylist_1.filter(course_id__icontains=course_no)

    if 'credits' in request.GET:
        credit=request.GET['credits']
        if credit:
            querylist_1=querylist_1.filter(credits=credit)

    if 'gen_ed' in request.GET:
        gen_ed_choice=request.GET['gen_ed']
        if gen_ed_choice:
            querylist_1=querylist_1.filter(gen_ed__icontains=gen_ed_choice)

    from .choices import term_choices, credit_choices, gen_ed_choices

    context={
        'user':user,
        'courses':querylist_1,
        'values':request.GET,
        'term_choices': term_choices,
        'credit_choices':credit_choices,
        'gen_ed_choices':gen_ed_choices,
    }
    return render(request, 'gen_ed_search.html',context)
def search_core(request,user):
    queryset_list=CourseInfo.objects.all().order_by('course_id')

    querylist_1=queryset_list.filter(Q(core='D')| Q(core='CS')| Q(core='LL')| Q(core='PL')| Q(core='HA')| Q(core='HL')| Q(core='HO')| Q(core='LS')| Q(core='MS')| Q(core='PS')| Q(core='IE')| Q(core='SB')| Q(core='SH'))
    if 'department' in request.GET:
        dept_id= request.GET['department']
        if dept_id:
            querylist_1=querylist_1.filter(course_id__icontains=dept_id)
    
    if 'course_no' in request.GET:
        course_no= request.GET['course_no']
        if course_no:
            querylist_1=querylist_1.filter(course_id__icontains=course_no)

    if 'credits' in request.GET:
        credit=request.GET['credits']
        if credit:
            querylist_1=querylist_1.filter(credits=credit)

    if 'core_choices' in request.GET:
        core_choice=request.GET['core_choices']
        if core_choice:
            querylist_1=querylist_1.filter(core__icontains=core_choice)
    
    from .choices import term_choices, credit_choices, gen_ed_choices, core_choices

    context={
        'user':user,
        'courses':querylist_1,
        'values':request.GET,
        'term_choices': term_choices,
        'credit_choices':credit_choices,
        'core_choices':core_choices,}

    return render(request, 'core_search.html',context)

def search_core_no_user(request):
    user=None
    queryset_list=CourseInfo.objects.all().order_by('course_id')

    querylist_1=queryset_list.filter(Q(core='D')| Q(core='CS')| Q(core='LL')| Q(core='PL')| Q(core='HA')| Q(core='HL')| Q(core='HO')| Q(core='LS')| Q(core='MS')| Q(core='PS')| Q(core='IE')| Q(core='SB')| Q(core='SH'))
    if 'department' in request.GET:
        dept_id= request.GET['department']
        if dept_id:
            querylist_1=querylist_1.filter(course_id__icontains=dept_id)
    
    if 'course_no' in request.GET:
        course_no= request.GET['course_no']
        if course_no:
            querylist_1=querylist_1.filter(course_id__icontains=course_no)

    if 'credits' in request.GET:
        credit=request.GET['credits']
        if credit:
            querylist_1=querylist_1.filter(credits=credit)

    if 'core_choices' in request.GET:
        core_choice=request.GET['core_choices']
        if core_choice:
            querylist_1=querylist_1.filter(core__icontains=core_choice)
    
    from .choices import term_choices, credit_choices, gen_ed_choices, core_choices

    context={
        'user':user,
        'courses':querylist_1,
        'values':request.GET,
        'term_choices': term_choices,
        'credit_choices':credit_choices,
        'core_choices':core_choices,}

    return render(request, 'core_search.html',context)
def department_link(request,dept_id,user):

    dept_id=dept_id[0:4]
    queryset_list=CourseInfo.objects.all().filter(dept_id=dept_id)
    from .choices import term_choices, credit_choices

    context={'user':user,
            'courses':queryset_list,
            'term_choices': term_choices,
            'credit_choices':credit_choices,}


    return render (request, 'search.html', context)

def list_professors(request, course_id, user):
    queryset_list=Professors.objects.all().filter(course_id__icontains=course_id)

    context={'professors': queryset_list,
            'course':course_id,
            'user':user}

    return render(request, 'professors.html', context)

def google_search(request,name):
    url= f"https://www.google.com/search?q={name}+teacher+reviews&oq=ed+f&aqs=chrome.0.69i59j69i57j0i67j0i512l3j69i60l2.3956j0j4&sourceid=chrome&ie=UTF-8"
    
    return redirect(url)

def register(request):
    if request.method=="POST":

        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email= request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,'That username is Taken')
                message="That Username is Taken"
                context={'message':message}
                return render(request,'register.html', context)

            if User.objects.filter(email=email).exists():
                messages.error(request,'That email is taken')
                message='That email is taken'
                context={'message':message}
                return render(request,'register.html', context)
            
            else:
                user=User.objects.create_user(
                    username=username,
                    password=password,
                    email=email,
                    first_name=first_name,
                    last_name=last_name)
                
                user.save()
                messages.success(request,'You are now registered')
                message='You Are Now Registered!'
                return redirect('homepage_with_message',message)

        else:
            messages.error(request, 'Passwords do not match')
            message='Passwords do not match'
            context={'message':message}
            return render(request,'register.html',context)

    else:
        return render(request,'register.html')

def homepage_after_register(request,message):

    dept=CourseInfo.objects.values_list('dept_id', 'department').order_by('course_id')    
    department_list=[]
    dept_id_list={}
    for i in dept:
        if i not in department_list:
            department_list.append(i)
        if i not in dept_id_list and i[0]!='USLT':
            dept_id_list[i[0]]= i[1]

    dept_list_1=department_list[:93]
    dept_id_list_1=[]
    dept_id_dict_1=dict(itertools.islice(dept_id_list.items(),93))
    for key, value in dept_id_dict_1.items():
        string= key +" "+" "+ value
        dept_id_list_1.append(string)


    dept_list_2=department_list[93:]
    dept_id_list_2=[]

    dept_id_dict_2=dict(itertools.islice(dept_id_list.items(),94,185 ))


    for key, value in dept_id_dict_2.items():
        string= key +" "+" "+ value
        dept_id_list_2.append(string)


    from .choices import term_choices, credit_choices

    if message=='':
        message= 'You are now registered!'
    context={'message':message,
            'dept_list_1':dept_list_1,
             'dept_list_2':dept_list_2,
             'dept_id_list_1':dept_id_list_1,
             'dept_id_list_2':dept_id_list_2,
             'term_choices': term_choices,
             'credit_choices':credit_choices}

    return render(request,'homepage.html',context)

def login(request):
    print("Test")
    if request.method=="POST":
        print("Test_2")
        username=request.POST['username']
        password=request.POST['password']

        user1=auth.authenticate(username=username, password=password)

        print(f"user:{user1}")
        if user1 is not None:
            auth.login(request, user1)
            messages.success(request, 'Logged in')

            return redirect('homepage_after_login',user1)

        else:
            messages.error(request,'Invalid')
            message="Username and/or Password do not match. Please try again"
            context={'message':message}
            return render(request,'login.html', context)

    else:
        return render(request,'login.html')


def homepage_after_login(request,user):

    dept=CourseInfo.objects.values_list('dept_id', 'department').order_by('course_id')    
    department_list=[]
    dept_id_list={}
    for i in dept:
        if i not in department_list:
            department_list.append(i)
        if i not in dept_id_list and i[0]!='USLT':
            dept_id_list[i[0]]= i[1]

    dept_list_1=department_list[:93]
    dept_id_list_1=[]
    dept_id_dict_1=dict(itertools.islice(dept_id_list.items(),93))
    for key, value in dept_id_dict_1.items():
        string= key +" "+" "+ value
        dept_id_list_1.append(string)


    dept_list_2=department_list[93:]
    dept_id_list_2=[]

    dept_id_dict_2=dict(itertools.islice(dept_id_list.items(),94,185 ))


    for key, value in dept_id_dict_2.items():
        string= key +" "+" "+ value
        dept_id_list_2.append(string)


    from .choices import term_choices, credit_choices

    message=f"Hello {user}, you have succesfully logged in!"
    context={'message':message,
            'user':user,
            'dept_list_1':dept_list_1,
             'dept_list_2':dept_list_2,
             'dept_id_list_1':dept_id_list_1,
             'dept_id_list_2':dept_id_list_2,
             'term_choices': term_choices,
             'credit_choices':credit_choices}

    return render(request,'homepage.html',context)

def save_to_list(request,user, course_id):

    if user =='None':
        return redirect('login')
    else:

        selected_course=CourseInfo.objects.get(course_id=course_id)

        username=user
        course_id= selected_course.course_id
        name=selected_course.name
        dept_id=selected_course.dept_id
        department= selected_course.department
        credits=selected_course.credits
        description=selected_course.description
        grading_method=selected_course.grading_method
        gen_ed=selected_course.gen_ed
        core=selected_course.core
        relationships=selected_course.relationships
        sections=selected_course.sections

        saved_course=UserSavedCourses(
            username=username,
            course_id=course_id,
            name=name,
            dept_id=dept_id,
            department=department,
            credits=credits,
            description=description,
            grading_method=grading_method,
            gen_ed=gen_ed,
            core=core,
            relationships=relationships,
            sections=sections
            )
        saved_course.save()

        message=f"{course_id} added to your saved list"

        return redirect('homepage_with_message', message)

def show_saved_courses(request, user):

    saved_courses= UserSavedCourses.objects.all().filter(username=user)

    context={'saved_courses':saved_courses}

    return render(request, 'saved_list.html',context)


