from django.http import HttpResponse

def home(request):
        return HttpResponse('<h1>Hello from Django</h1>')
def about(request):
        return HttpResponse('<h1>This is About Page</h1>')
def contact(request):
        return HttpResponse('<h1>9970364378</h1>')
def Address(request):
        return HttpResponse('<h1>Amch aurangabad</h1>')
def Techology(request):
        return HttpResponse('<h1>about python</h1>')
def Web(request):
        return HttpResponse('<h1>shelara5418@gmail.com</h1>')
def Mobile(request):
        return HttpResponse('<h1>9284429991</h1>')
def Desktop(request):
        return HttpResponse('<h1>hp</h1>')
