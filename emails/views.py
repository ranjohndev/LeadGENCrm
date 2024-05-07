from django.shortcuts import render

# Create your views here.


# emails/views.py

from django.shortcuts import render

def test_view(request):
    return render(request, 'emails/test.html')

