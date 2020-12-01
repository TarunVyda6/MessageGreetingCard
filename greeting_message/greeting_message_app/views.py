from django.shortcuts import render
from .models import GreetingTable


# Create your views here.

def get(request):
    sample = GreetingTable.objects.all()
    return render(request, 'greeting_app.html', {'mydata_json': sample})
