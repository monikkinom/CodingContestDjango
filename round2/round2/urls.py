from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples
    url(r'^questions/', 'acm.views.questions', name='question page'),
    url(r'^mcqquestions/', 'acm.views.mcqquestions', name='mcq question page'),
    url(r'^scoreboard/', 'acm.views.view_ranks', name='ranks page'),
    url(r'^instructions/', 'acm.views.instructions', name='instructions page'),
    url(r'^home/', 'acm.views.home', name='Home page'),
    url(r'^$', 'acm.views.signin', name='Login page'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^logout/', 'acm.views.signout', name='Logout page'),
    url(r'^end/', 'acm.views.end', name='Disable now')
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)