from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create/$', views.create, name="create"),
    url(r'^(?P<post_id>\d+)/delete/$', views.destroy, name="destroy"),
]