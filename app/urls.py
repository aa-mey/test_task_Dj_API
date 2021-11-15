from django.urls import path
from .views import WorkerAllView, WorkerSelectedLevelView

app_name = "workers"
urlpatterns = [
    path('', WorkerAllView.as_view()),
    path('level0', WorkerSelectedLevelView.as_view()),
]