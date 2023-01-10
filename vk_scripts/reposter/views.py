from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import DeleteView, CreateView
from django.views.generic import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .forms import UserLoginForm, AddGroup, AddSchedule
from .models import Group, CrontabHours
from django.views.decorators.http import require_http_methods
from django.shortcuts import render, redirect
from django.db.utils import IntegrityError
from .modules.vk_api_code import get_random_post


@login_required()
@require_http_methods(["GET"])
def index(request):
    groups = [(group.id, group.url, group.active)
              for group
              in Group.objects.all().order_by('id')]
    return render(
        request,
        'welcome.html',
        context={
            "groups": groups,
            'add_group_form': AddGroup,
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


class DeleteGroup(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
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


def random_post(request):
    post = get_random_post()
    return redirect(post)


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


class ScheduleView(LoginRequiredMixin, CreateView):
    template_name = 'schedule.html'
    model = CrontabHours
    form_class = AddSchedule
    success_url = '/schedule/'

    extra_context = {
        'hours': CrontabHours.objects.all()
    }

    def get(self, *args, **kwargs):
        print(self.get_context_data())
        return super().get(*args, **kwargs)


# @require_http_methods(["POST"])
# def change_job(request):
#     form = request.POST
#     job = DjangoJob.objects.all()[0]
#     print('Job: ', job.__dict__)
#
#     return redirect('/schedule/')
