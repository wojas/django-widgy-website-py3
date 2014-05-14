from django.conf.urls import patterns, include, url
from .widgy_site import site as widgy_site

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'backend.views.home', name='home'),
    # url(r'^backend/', include('backend.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # widgy admin
    url(r'^admin/widgy/', include(widgy_site.urls)),

    # widgy frontend
    url(r'^widgy/', include('widgy.contrib.widgy_mezzanine.urls')),
    url(r'^', include('mezzanine.urls')),

    # your website
    url(r'^$', 'mezzanine.pages.views.page', {'slug': '/'}, name='home'),
)
