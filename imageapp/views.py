from django.http.response import HttpResponse
from django.shortcuts import render
from django.http.response import HttpResponse
from .models import imageModel
from .forms import ImageForms

# Create your views here.

def index(request):
    if request.method=='POST':
        form=ImageForms(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    form=ImageForms()
    uploaded_img=imageModel.objects.all().order_by('-id')
    return render(request,'imageapp/home.html',{'form':form,'uploaded_img':uploaded_img})