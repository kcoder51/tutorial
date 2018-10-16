from django.shortcuts import render, HttpResponse

#from django.contrib.auth.views import auth.views
# Create your views here.
def home(request):
    #return HttpResponse('Home Page!')
    # Now we render a template
    return render(request, 'accounts/login.html')
