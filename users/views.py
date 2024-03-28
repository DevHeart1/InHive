from django.shortcuts import render
from django.http import HttpResponse

posts=[
    {
        'author': 'Obasi Peace',
        'title': 'The Inhive Project',
        'content': 'Learning the backend part',
        'date_posted': 'March 28,2024'

    },
    {
        'author': 'Obasi Oluchi',
        'title': 'The Inhive Project cont.',
        'content': 'Learning the backend part 2',
        'date_posted': 'March 29,2024'
    }
]



def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'users/home.html', context)

def signup(request):
    return render(request, 'users/signup.html', {'title': 'Signup'} )
