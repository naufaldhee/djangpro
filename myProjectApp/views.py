from django.shortcuts import render

def home_view(request):
    return render(request, 'myProjectApp/home.html')

def education_view(request):
    return render(request, 'myProjectApp/education.html')

def experience_view(request):
    return render(request, 'myProjectApp/experiences.html')

def social_view(request):
    return render(request, 'myProjectApp/social.html')