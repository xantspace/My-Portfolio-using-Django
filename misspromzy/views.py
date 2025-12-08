from django.shortcuts import render

# Create your views here.
def home(request):
    content ={
        "bio": "Welcome to my portfolio website! I'm excited to share my projects and experiences with you.",
        "status": "Active",
        "is_staff": True
   }
    return render(request, 'Index.html', content)
def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')