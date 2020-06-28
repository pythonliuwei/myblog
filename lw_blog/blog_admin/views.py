from django.shortcuts import render
from rest_framework.response import Response
# Create your views here.
from utils.basic_views import MyAPIView


class RegisterView(MyAPIView):
    def get(self,request,*args,**kwargs):
        return render(request,'admin/register.html')
