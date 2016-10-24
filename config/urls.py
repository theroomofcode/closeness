# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, division

from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.views import defaults as default_views
from django.utils.translation import ugettext_lazy as _


urlpatterns = [
]

# Django Admin, use {% url 'admin:index' %}
admin.site.site_header = _('{} Admin'.format(settings.PROJECT_NAME))
urlpatterns += [
    url(settings.ADMIN_URL, admin.site.urls),
]

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
        url(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception('Permission Denied')}),
        url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')}),
        url(r'^500/$', default_views.server_error),
    ]

    # If is installed debug_toolbar, add its urls
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns += [
            url(r'^__debug__/', include(debug_toolbar.urls)),
        ]

    # Only access directly to MEDIA when DEBUG is True
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
