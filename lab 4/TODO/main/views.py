from django.shortcuts import render
from main.models import Tasks

# Create your views here.
tasks = Tasks.objects.all()

# tasks = [
#         {'name': 'Task 0',
#          'created': '10/09/2018',
#          'due_on': '12/09/2018',
#          'owner': 'admin',
#          'mark': False
#          },
#         {'name': 'Task 1',
#          'created': '10/09/2018',
#          'due_on': '12/09/2018',
#          'owner': 'admin',
#          'mark': True
#          },
#         {'name': 'Task 2',
#          'created': '10/09/2018',
#          'due_on': '12/09/2018',
#          'owner': 'admin',
#          'mark': True
#          },
#         {'name': 'Task 3',
#          'created': '10/09/2018',
#          'due_on': '12/09/2018',
#          'owner': 'admin',
#          'mark': True
#          },
#         {'name': 'Task 4',
#          'created': '10/09/2018',
#          'due_on': '12/09/2018',
#          'owner': 'admin',
#          'mark': True
#          }
#     ]


def todo_list(request):

    context = {
        'tasks': tasks
    }
    return render(request, 'todo_list.html', context=context)


def completed_todo_list(request):
    context = {
        'tasks': tasks
    }
    return render(request, 'completed_todo_list.html', context=context)
