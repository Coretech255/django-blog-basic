from django.urls import path 
from . views import all_post, post_detail

urlpatterns = [
	path('', all_post, name="all_post"),
	path('post/<int:id>/', post_detail, name="post_detail")
]