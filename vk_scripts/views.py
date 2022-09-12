from django.shortcuts import render, redirect
from django.contrib import messages
import os
from .forms import GroupForm
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def index(request):
    # get current directory
    module_dir = os.path.dirname(__file__)
    file_path = module_dir + '/static/groups.txt'

    with open(file_path, 'r') as file:
        groups = file.readlines()
    return render(
        request,
        'index.html',
        context={
            "groups": groups,
            'form': GroupForm
        }
    )


@require_http_methods(["POST"])
def add_group(request):
    form = request.POST
    group_url = form['group_url']
    print(group_url)
    print("\n")

    # get current directory
    module_dir = os.path.dirname(__file__)
    file_path = module_dir + '/static/groups.txt'

    with open(file_path, 'a') as file:
        if group_url.endswith('vk.com') or group_url.endswith('vk.com/'):
            messages.error(request, 'Неправильный адрес!')
            return redirect('/')
        if group_url.startswith('https://vk.com'):
            pass
        elif group_url.startswith('vk.com'):
            group_url = 'https://' + group_url
        else:
            messages.error(request, 'Неправильный адрес!')
            return redirect('/')
        file.write(group_url + '\n')
    return redirect('/')
