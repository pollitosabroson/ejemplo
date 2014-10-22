from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'app.views.principal', name='principal'),
    # url(r'^foraneas/$', 'app.views.foreaneas', name='foreaneas'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
