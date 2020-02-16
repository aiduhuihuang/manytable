from django.urls import path
from .views import *

urlpatterns = [
        path("index/",index),
        path("add/",add),
        path("gets/",gets),
        path("update/",update),
        path("delete/",delete),
        path("torm/",torm),
    ]