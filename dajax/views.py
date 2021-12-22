from django.shortcuts import render
from .models import DajaxModel
from django.views.generic import ListView, View,CreateView
from django.http import JsonResponse
# Create your views here.

class DajaxHome(ListView):
    model = DajaxModel
    template_name= 'home.html'
    context_object_name = 'userdata'


class UserCreate(View):
    template_name= 'home.html'
    def get(self, request):
        username = request.GET.get('name')
        email = request.GET.get('email')
        phone = request.GET.get('phone')
        address = request.GET.get('address')

        # print(username, email, phone, address)
        userobj = DajaxModel.objects.create(name=username, email=email, phone=phone, address=address)

        data = {
            'id':userobj.id,
            'name':userobj.name,
            'email':userobj.email,
            'phone':userobj.phone,
            'address':userobj.address,
        }
        return JsonResponse(data)