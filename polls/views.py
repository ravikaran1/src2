from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout as logoutt
from .models import Poll, Vote



def index(request):
    if request.method=='POST':
        choice1=request.POST.get('choice1')
        choice2=request.POST.get('choice2')
        question=request.POST.get('question')
        poll=Poll.objects.filter(question=question)[0]
        voter_list=poll.voters
        voter_list+=request.user.username +','
        poll.voters=voter_list
        poll.save()
        print(request.user.username)
        print(poll.voters)
        if choice1!=None:
            vote=Vote(user=request.user,question=question,choice=choice1)
            vote.save()
            poll.choice1_votes+=1
            total=poll.choice1_votes+poll.choice2_votes
            poll.percentage1=(poll.choice1_votes/total)*100
            poll.percentage2=(poll.choice2_votes/total)*100
            poll.save()

        else:
            vote=Vote(user=request.user,question=question,choice=choice2)
            vote.save()
            poll.choice2_votes+=1
            total=poll.choice1_votes+poll.choice2_votes
            poll.percentage2=(poll.choice2_votes/total)*100
            poll.percentage1=(poll.choice1_votes/total)*100
            poll.save()
        return redirect('index')
    polls=Poll.objects.all().order_by('-timest')
    votes=Vote.objects.all()
    context={'polls':polls,'votes':votes}
    return render(request,'polls/index.html',context)

def signup(request):
    if request.method=='POST':
        email=request.POST.get('email')
        username=request.POST.get('username')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')

        if User.objects.filter(username=username).exists():
            messages.error(request,'Username already exists.')
            return redirect('signup')
        if User.objects.filter(email=email).exists():
            messages.error(request,'You already have an account with this email. Please login.')
            return redirect('loginn')
        if len(username)<4:
            messages.error(request,'Username is too short.')
            return redirect('signup')
        if len(pass1)<6:
            messages.error(request,'Password is too short.')
            return redirect('signup')
        if pass1!=pass2:
            messages.error(request,'Passwords do not match.')
            return redirect('signup')


        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=username
        myuser.save()
        messages.success(request,'Signed up successfully, please Log in.')
        return redirect('loginn')

    return render(request,'polls/signup.html')

def loginn(request):
    if request.method=='POST':
        lusername=request.POST['lusername']
        lpassword=request.POST['lpassword']
        user=authenticate(username=lusername,password=lpassword)

        if user is not None:
            login(request, user)
            messages.success(request,'Logged in successfully.')
            return redirect('index')

        else:
            messages.error(request,'Invalid credentials')
            return redirect('loginn')

    return render(request,'polls/login.html')

def logout(request):
    logoutt(request)
    messages.success(request,'Logged out successfully')
    return redirect('index')


def addpoll(request):
    user=request.user
    if not user.is_authenticated:
        messages.error(request,'Please login to add a poll.')
        return redirect('loginn')



    if request.method=='POST':
        question=request.POST['question']
        choice1=request.POST['choice1']
        choice2=request.POST['choice2']
        poll=Poll(user=user,question=question, choice1=choice1, choice2=choice2)
        poll.save()
        messages.success(request,'Poll added.')
        return redirect('index')

    return render(request,'polls/addpoll.html')

def profile(request):
    user=request.user
    username=user.username
    email=user.email

    params={'user':user}
    return render(request, 'profile.html',params)


def editprof(request):
    user=request.user
    params={'user':user}

    if request.method=='POST':
        user=request.user
        email=request.POST.get('email')
        myid=request.POST.get('myid')
        username=request.POST.get('username')

        if username==user.username:
            pass

        elif User.objects.filter(username=username).exists():
            messages.error(request,'Username already exists.')
            return redirect('editprof')

        if email==user.email:
            pass
        elif User.objects.filter(email=email).exists():
            messages.error(request,'This email is already in use with some account.')
            return redirect('editprof')

        User.objects.filter(id=myid).update(email=email)
        User.objects.filter(id=myid).update(username=username)
        return redirect('profile')
    return render(request, 'editprof.html',params)

def yourpolls(request):
    if request.method=='POST':
        choice1=request.POST.get('choice1')
        choice2=request.POST.get('choice2')
        question=request.POST.get('question')
        poll=Poll.objects.filter(question=question)[0]
        voter_list=poll.voters
        voter_list+=request.user.username +','
        poll.voters=voter_list
        poll.save()

        if choice1!=None:
            vote=Vote(user=request.user,question=question,choice=choice1)
            vote.save()
            poll.choice1_votes+=1
            total=poll.choice1_votes+poll.choice2_votes
            poll.percentage1=(poll.choice1_votes/total)*100
            poll.percentage2=(poll.choice2_votes/total)*100
            poll.save()

        else:
            vote=Vote(user=request.user,question=question,choice=choice2)
            vote.save()
            poll.choice2_votes+=1
            total=poll.choice1_votes+poll.choice2_votes
            poll.percentage2=(poll.choice2_votes/total)*100
            poll.percentage1=(poll.choice1_votes/total)*100
            poll.save()
        return redirect('yourpolls')
    polls=Poll.objects.filter(user=request.user).order_by('-timest')
    votes=Vote.objects.all()
    context={'polls':polls,'votes':votes}

    return render(request,'polls/yourpolls.html',context)

# Create your views here.
