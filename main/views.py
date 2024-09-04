from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306152121',
        'name': 'Bertrand Gwynfory Iskandar',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)
