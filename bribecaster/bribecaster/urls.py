from cases import views
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bribecaster.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^form-showcase.html/', views.form, name='form'),
    url(r'^index.html/', views.index, name='index'),
    url(r'^data-table.html/', views.table, name='table'),
    url(r'^$', views.index, name='index'),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
