from django.shortcuts import render

# Create your views here.

def docs_intro(request):
    return render(request,'docs/introduction.html')

# def docs_riser_sizing(request):
#     return render(request,'docs/riser_sizing.html')
