from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_all_posts, name="home"),
    path("post/<int:post_id>", views.show_post, name="show_post"),
    path("admin/create-post/", views.create_post, name="create_post"),
    path("admin/edit-post/<int:post_id>", views.edit_post, name="edit_post"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]
