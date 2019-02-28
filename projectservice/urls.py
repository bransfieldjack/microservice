from django.conf.urls import patterns, include, url
from django.contrib import admin
from api.api import hours_router

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(hours_router.urls)),
)
