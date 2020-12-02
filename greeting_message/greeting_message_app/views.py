import json
from django.core.exceptions import FieldError
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .models import GreetingTable
from django.views import View


# Create your views here.

def greeting(request):
    """
    :return: render to the html page
    """

    return render(request, 'greeting_app.html')


class GreetingView(View):
    def get(self, request):
        """
        gets data from data base and returns http response in json format
        """
        try:
            greeting_qs = GreetingTable.objects.all()
            data = list(greeting_qs.values('name', 'message'))
            return HttpResponse(json.dumps(data))
        except FieldError:
            return HttpResponse("given field name which is not present in data base")

