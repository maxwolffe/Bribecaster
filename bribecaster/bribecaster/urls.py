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
    url(r'^$', views.index, name='index'),
    url(r'^cases/new_form$', views.user_lookup, name='user_lookup'),
    url(r'^cases/obc_form/$', views.obc_form, name='obc_form')
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
