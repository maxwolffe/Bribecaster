fom cases import views
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bribecaster.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index.html/', views.index, name='index'),
    url(r'^datatables/$', views.table, name='table'),
    url(r'^datatables/sms-only$', views.SMSOnlyTable, name='smstable'),
    url(r'^datatables/robo-only$', views.RobocallOnlyTable, name='robotable'),
    url(r'^datatables/(?P<case_id>\d+)/$', views.detail, name='detail'),
    url(r'^$', views.index, name='index'),
    url(r'^reports/$', views.casesView, name='casesView'),
    url(r'^charts/pieCharts.html/$', views.pieCharts, name='pieCharts'),
    url(r'^cases/new_form/aadhaar_lookup/$', views.aadhaar_lookup, name='aadhaar_lookup'),
    url(r'^cases/obc_form/ci-(?P<citizen_id>\d+)$', views.obc_form, name='obc_form_ci'),
    url(r'^cases/obc_form/an-(?P<aadhaar_number>\d+)$', views.obc_form, name='obc_form_an'),
    url(r'^cases/obc_form/$', views.obc_form, name='obc_form'),
    url(r'^cases/office-charts/$', views.office_chart, name='office-charts'),
    url(r'^cases/office-charts/(?P<office_id>\d+)$', views.office_chart, name='office-charts'),
    url(r'^cases/per_office$', views.office_num_cases, name='test')
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()

