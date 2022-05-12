from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView
from rest_framework import viewsets
from .models import Movies
# Create your views here.
# class MovieListView(viewsets.ModelViewSet):

def index(request):
    try:
        mov = Movies.objects.all()
        print("============MOV=============")
        print(mov.__dict__)
        print("============MOV=============")
        data_list = []
        for index in mov:
            data_list.append({
                'id' : index.id,
                'name' : index.name,
                'image' : index.image,
            })
    except Exception as e:
        print("------------------------")
        print(e)
        print("------------------------")

    return render(request, 'index.html', {'data': data_list})

# @csrf_exempt
def detail(request, pk):
    print("---------------------------")
    print("Inside Movie Detail Page")
    print("---------------------------")
    try:
        mov = Movies.objects.get(id=pk)
        print("==========Single==============")
        print(pk)
        print("==========Single==============")
        context = {
				"name": mov.name,
				"description": mov.description,
				"image" : mov.image,
                'duration' : mov.duration,
                'genre' : mov.genre,
                'language' : mov.language,
                'type' : mov.type,
                'label' : mov.label,
                'userrating' : mov.userRating 
        }
        print(context)

    except Exception as e:
        print("=====================")
        print(e)
        print("=====================")

    return render(request, 'single.html', {'data': context})

    

        



