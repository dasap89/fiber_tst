"""fibertst URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings

from pages.views import IndexPage

from pages.views import AboutTechersPage

from pages.views import SearchList

urlpatterns = [
    # Examples:
    # url(r'^$', 'testproject.views.home', name='home'),
    # url(r'^testproject/', include('testproject.foo.urls')),

    url(r'^api/v2/', include('fiber.rest_api.urls')),
    url(r'^admin/fiber/', include('fiber.admin_urls')),
    url(r'^jsi18n/$', 'django.views.i18n.javascript_catalog', {'packages': ('fiber',),}),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^comments/', include('pinax.comments.urls')),

    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),
    
    # url(r'^search/', 'pages.views.search'),
    url(r'^search/', SearchList.as_view()),
    
    url(r'^contact-me/$', 'pages.views.contact_me'),

    url(r'^$', IndexPage.as_view()),  # this should always be placed last

    url(r'^about-us/$', AboutTechersPage.as_view(template_name="about-us.html")),  # this should always be placed last

    url(r'', 'fiber.views.page'),  # this should always be placed last
]

# Fix for show static on dev env
if settings.DEBUG:
    urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + urlpatterns
