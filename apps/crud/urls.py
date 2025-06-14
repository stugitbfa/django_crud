from django.urls import path
from .views import *

urlpatterns = [
    # path('', index_inner, name="index_inner"),
    # path('outer/', index_outer, name="index_outer"),

    path('', show, name='show'),
    path('insert/', insert, name='insert'),
    path('update-post/<int:post_id>', update_post, name='update_post'),
    path('delete-post/<int:post_id>', delete_post, name='delete_post'),
]
