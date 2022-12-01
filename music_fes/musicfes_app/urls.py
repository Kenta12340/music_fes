from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('',views.index,name='index'),
    path('form',views.form,name='form'),
    path('end',views.end,name='end'),
    path('tiket',views.tiket,name='tiket'),
    path('info',views.info,name='info'),
    path('access',views.access,name='access'),
        path('Orderlist/',views.orderlist,name="Orderlist"),
    path('Orderlist/<int:page>',views.orderlist,name="Orderlist"),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,
document_root=settings.MEDIA_ROOT)