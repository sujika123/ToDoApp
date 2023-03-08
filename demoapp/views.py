from django.contrib import messages
from django.contrib.auth import authenticate, login

from django.shortcuts import render, redirect

# Create your views here.
from demoapp.forms import LoginForm, userloginform, eventaddform
from demoapp.models import userlogin, eventadd


def home(request):
    return render(request,'index.html')
# def login(request):
#     return render(request,'signin.html')
def log(request):
    if request.method=='POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user  = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect('admin')
            elif user.is_user:
                print('haii')
                return redirect('userhome')
            else:
                messages.info(request,'Invalid Credentials')

    return render(request,'login.html')

def admin(request):
    return render(request,'Admin/index.html')
def userhome(request):
    return render(request,'userpages/userhome.html')
def register(request):
    form=LoginForm()
    form1=userloginform()
    if request.method=='POST':
        form=LoginForm(request.POST)
        form1=userloginform(request.POST,request.FILES)
        if form.is_valid() and form1.is_valid():
            user=form.save(commit=False)
            user.is_user=True
            user.save()
            c=form1.save(commit=False)
            c.user=user
            c.save()
            return redirect(log)
    return render(request,'registration.html',{'form':form,'form1':form1})



def user(request):
    data=userlogin.objects.all()
    print(data)
    return render(request,'Admin/user.html',{'data':data})
def profile(request):
    u=request.user
    data=user.objects.filter(user=u)
    # return render(request,'Admin/user.html')
    return render(request,'Admin/user.html')

def profileview(request):
    u = request.user
    data = userlogin.objects.filter(user=u)
    print(data)

    return render(request,'userpages/profileview.html',{'data':data})

def profileupdate(request,id):
    profile = userlogin.objects.get(id=id)
    form1 = userloginform(instance=profile)
    if request.method == 'POST':
        form = LoginForm(request.POST or None,instance=profile or None)
        # form1 = userloginform(request.POST or None,request.FILES,instance=profile or None)
        form1 = userloginform(request.POST or None,request.FILES,instance=profile or None)
        if form1.is_valid():
            user = form1.save(commit=True)
            user.is_user = True
            user.save()
        return redirect('profileview')

    return render(request,'userpages/profileupdate.html',{'form1':form1})


# User Event

def addevent(request):
    form = eventaddform()
    u = request.user
    if request.method=='POST':
        form = eventaddform(request.POST,request.FILES)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=u
            obj.save()
        return redirect('viewevent')
    return render(request,'userpages/addevent.html',{'form':form})

# def addevent(request):
#     form = eventaddform()
#     if request.method == 'POST':
#         form = eventaddform(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#     return render(request,'userpages/addevent.html',{'form':form})

def viewevent(request):
    u = request.user
    data = eventadd.objects.filter(user=u)
    return render(request,'userpages/viewevent.html',{'data':data})

def eventupdate(request,id):

    viewevent = eventadd.objects.get(id=id)
    form = eventaddform(instance=viewevent)
    if request.method == 'POST':
        form = eventaddform(request.POST or None,request.FILES or None,instance=viewevent or None)
        if form.is_valid():
            event=form.save(commit=True)
            event.save()
            return redirect('viewevent')

    return render(request, 'userpages/eventupdate.html', {'form': form})

def eventdelete(request,id):
    data=eventadd.objects.get(id=id)
    data.delete()
    return redirect('profileview')




# def viewevent(request):
#     u = request.user
#     data = userlogin.objects.filter(user=u)
#     print(data)
#
#     return render(request, 'userpages/viewevent.html', {'data': data})
#
# def addevent(request,id):
#     profile = userlogin.objects.get(id=id)
#     form = userloginform(instance=profile)
#
#     return render(request, 'userpages/addevent.html', {'form': form})



  # Admin
def update(request,id):
    user=userlogin.objects.get(id=id)
    form=userloginform(instance=user)
    if request.method == "POST":
        form= userloginform(request.POST or None,request.FILES,instance=user or None)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('user')
    return render(request,'Admin/update.html',{'form':form})

def delete(request,id):
    user=userlogin.objects.get(id=id)
    user.delete()
    return redirect('user')
