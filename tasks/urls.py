from django.urls import path

from . import views

app_name = "tasks"

urlpatterns = [
    path("", views.ViewTask.as_view(), name="view_tasks"),
    path("delete/<int:pk>", views.DeleteTask.as_view(), name="delete_task"),
    path("create/", views.CreateTask.as_view(), name="create_task"),
    path("update/<int:pk>", views.UpdateTask.as_view(), name="update_task"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("register/", views.RegisterTask.as_view(), name="register"),
]
