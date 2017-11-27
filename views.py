from django.shortcuts import render, HttpResponse, redirect
from models import *

def index(request):
    return render(request,'crud/index.html',{"users": User.objects.all()})

def new(request):
    return render(request,'crud/new.html')

def edit(request,id):
    return render(request,'crud/edit.html',{ "user": User.objects.get(id = id) })

def create(request):
    User.objects.create(full_name=request.POST['full_name'], email=request.POST['email'])
    return redirect('/users') 


def update(request,id):
    user = User.objects.get(id = id)
    user.full_name = request.POST['full_name']
    user.email = request.POST['email']
    user.save()
    return redirect('/users')

def show(request,id):
    return render(request,'crud/show.html',{"user": User.objects.get(id =id)})

def destroy(request, id):
	User.objects.get(id=id).delete()
	return redirect('/users')