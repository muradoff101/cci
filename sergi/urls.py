"""sergi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('tpp@dmin$/', admin.site.urls),
    path('', include('main.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    # path('media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, 'show_indexes': settings.DEBUG}),
    # path('static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT, 'show_indexes': settings.DEBUG}),
]
              # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,}),]


urlpatterns += i18n_patterns(
    path('', include('main.urls')),
)

# if settings.DEBUG:
    # import debug_toolbar
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
