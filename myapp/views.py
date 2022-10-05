from django.shortcuts import render
from .models import DemoModel
# Create your views here.
def HomeView(request):
    data = DemoModel.objects.get(id=1)
    context = {
      'data':data
    }
    return render(request,'index.html',context)


