from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView as AuthLoginView
from django.contrib.auth.views import LogoutView as AuthLogoutView
from django.shortcuts import redirect
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import LoginForm, RegisterForm
from .models import Task, User

# Create your views here.


class CreateTask(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "tasks/create_task.html"
    fields = ["title", "content"]
    success_url = "/tasks/"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class ViewTask(LoginRequiredMixin, ListView):
    model = Task
    template_name = "tasks/view_tasks.html"
    context_object_name = "tasks"
    paginate_by = 4

    def get_queryset(self):
        queryset = Task.objects.filter(created_by=self.request.user)

        search_query = self.request.GET.get("q")
        if search_query:
            queryset = queryset.filter(title__icontains=search_query)

        status = self.request.GET.get("status")
        if status:
            queryset = queryset.filter(status__iexact=status)

        sort_by = self.request.GET.get("sort_by", "title")
        order = self.request.GET.get("sort_order", "asc")
        order_prefix = "-" if order == "desc" else ""
        queryset = queryset.order_by(f"{order_prefix}{sort_by}")

        return queryset


class DeleteTask(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = "tasks/delete_task.html"
    context_object_name = "task"
    success_url = "/tasks/"

    def get_queryset(self):
        return Task.objects.filter(created_by=self.request.user)


class UpdateTask(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = "tasks/update_task.html"
    fields = ["title", "content", "status"]
    context_object_name = "task"
    success_url = "/tasks/"

    def get_queryset(self):
        return Task.objects.filter(created_by=self.request.user)


class RegisterTask(CreateView):
    model = User
    form_class = RegisterForm
    template_name = "auth/register/register.html"
    success_url = "/tasks/login/"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("tasks:view_tasks")
        return super().dispatch(request, *args, **kwargs)


class LoginView(AuthLoginView):
    model = User
    form_class = LoginForm
    template_name = "auth/login/login.html"
    next_page = "/tasks/"
    redirect_authenticated_user = True


class LogoutView(AuthLogoutView):
    next_page = "/tasks/login/"
