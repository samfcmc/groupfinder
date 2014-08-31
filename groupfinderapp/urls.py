from django.conf.urls import patterns, include, url

from groupfinderapp import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'groupfinder.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index'),
    url(r'^logout', views.user_logout, name='logout'),
)
