from django.urls import path
from . import views

app_name = "website"


from django.conf.urls.static import static

urlpatterns = [
    path("home/", views.home, name="home"),
    path("", views.blogs, name="blogs"),
    path("about/", views.about, name="about"),
    path("blogs/", views.blogs, name="blogs"),
    path("partner/", views.partner, name="partner"),
    path("image/<int:pk>/", views.serve_image, name="image"),
    path("profile/", views.profile, name="profile"),

]


