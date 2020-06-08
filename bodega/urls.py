from django.conf.urls import url
from bodega import views

urlpatterns=[
    url(r'^api/bodega$',views.bodega_list),
    url(r'^api/bodega/(?P<pk>[0-9]+)$',views.bodega_detail),
    url(r'^api/bodega/(?P<estado>[A-Z])$',views.bodega_list_estado)
]
