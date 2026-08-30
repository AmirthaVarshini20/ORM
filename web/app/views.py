from django.shortcuts import HttpResponse,render
def home(request):
    return HttpResponse('<h1>Good Afternoon!!!</h1>')
def about(resquest):
    return HttpResponse('<h1>Good Evening!!!</h1>')
def fashion(request):
    return HttpResponse('<h1>I love fashion designing!!</h1>')
def hobby(request):
    return render(request,'varshini.html',{'name':"nandhini"})

# Create your views here.
