from django.shortcuts import render


def index(request):
    return render(request, '/Users/seojun/vscode/ssf_django/mainpage/templates/main/index.html')