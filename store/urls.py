from django.urls import path
from . import views
urlpatterns=[
    path('login',views.login),
    path('log',views.log),
    path('dap',views.dap),
    path('anp',views.anp),
    path('ins',views.ins),
    path('showuser',views.showuser),
    path('dele/<int:id>',views.dele),
    path('home',views.home),
    path('edit_stock',views.edit_stock),
    path('edit/<int:id>',views.edit),
    path('upd/<int:id>',views.upd),
    path('delete_stock',views.delete_stock),
    path('delete/<int:id>',views.delete),
    path('admin_panel',views.admin_panel),
    path('aprv_pro',views.aprv_pro),
    path('apt/<int:id>',views.apt),
    path('dapt/<int:id>',views.dapt),
    path('only_aprp',views.only_arpp),
]