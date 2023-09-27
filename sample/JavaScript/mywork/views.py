from django.shortcuts import render

# Create your views here.
def message(request):
    return render(request, 'mywork/message.html')
def color(request):
    return render(request, 'mywork/color.html')
def counter(request):
    return render(request, 'mywork/counter.html')
def joke(request):
    return render(request, 'mywork/joke.html')
def toggle(request):
    return render(request, 'mywork/toggle.html')
def QA(request):
    return render(request, 'mywork/QA.html')
def age_calculator(request):
    return render(request, 'mywork/age_calculator.html')
def password(request):
    return render(request, 'mywork/password.html')



