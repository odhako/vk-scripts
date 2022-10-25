from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .forms import UserLoginForm, AddGroup
from .models import Group
from django.views.decorators.http import require_http_methods
from django.shortcuts import render, redirect
from django.db.utils import IntegrityError
from apscheduler.schedulers.base import STATE_RUNNING


@require_http_methods(["GET"])
def index(request):
    print(request.user.is_authenticated)
    if not request.user.is_authenticated:
        return redirect('/login/')
    groups = [(group.id, group.url, group.active)
              for group
              in Group.objects.all().order_by('id')]
    state_running = STATE_RUNNING
    print('State: ', state_running)
    return render(
        request,
        'welcome.html',
        context={
            "groups": groups,
            'add_group_form': AddGroup,
            'state_running': state_running,
        }
    )


@require_http_methods(["POST"])
def add_group(request):
    form = request.POST
    group_url = form['url']
    print(group_url)
    print("\n")

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
    if group_url.endswith('/'):
        group_url = group_url[:-1]
    try:
        group = Group()
        group.url = group_url
        group.save()
    except IntegrityError:
        messages.error(request, 'Эта группа уже добавлена!')
        return redirect('/')

    messages.success(request, f'Добавлена группа: {group_url}')

    return redirect('/')


class DeleteGroup(SuccessMessageMixin, DeleteView):
    model = Group
    template_name = ''
    success_url = '/'
    success_message = 'Группа удалена'


@require_http_methods(["POST"])
def toggle(request, pk):
    form = request.POST
    print(form)
    print(pk)
    group = Group.objects.filter(id=pk)[0]
    if group.active:
        group.active = False
    else:
        group.active = True
    group.save()
    print(group.url)
    return redirect('/')


@require_http_methods(["POST"])
def toggle_scheduler(request):
    # from apscheduler.schedulers.background import BackgroundScheduler
    # scheduler = BackgroundScheduler()
    # if STATE_RUNNING:
    #     scheduler.shutdown()
    # else:
    #     scheduler.start()
    return redirect('/')


class Login(SuccessMessageMixin, LoginView):
    template_name = 'login.html'
    authentication_form = UserLoginForm
    next_page = '/'
    redirect_authenticated_user = False
    success_message = 'Успешный вход.'
    extra_context = {
        'header': 'Войти в аккаунт',
        'button': 'Войти',
    }


class Logout(LogoutView):
    next_page = '/'
