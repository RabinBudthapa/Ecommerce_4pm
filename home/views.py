from django.shortcuts import render
from .models import *

# Create your views here
from django.views import View
class Base(View):
    views={}

class HomeView(Base):
    def get(self,request):
        self.views['categories']=Category.objects.all()
        self.views['brands']=Brand.objects.all()
        self.views['sliders']=Slider.objects.all()
        self.views['reviews'] = Review.objects.all()
        return render(request,'index.html',self.views)
