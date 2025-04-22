from django.shortcuts import render

# Create your views here.

def login_view(request):
    return render(request, 'authentication/login.html')
def check_login(request):
    if(request.POST.name=="pratik" and request.POST.password=="12345"):
        return render(request, 'authentication/home.html')
    else:
        return render(request, 'authentication/login.html')