from django.conf.urls import patterns, include, url

from .views import *

urlpatterns = patterns(
    '',
    (r'^login/', login),
    (r'^auth/', auth_view),
    (r'^loggedin/', loggedin),
    (r'^logout/', logout),
    (r'^invalid/', invalid),
)
