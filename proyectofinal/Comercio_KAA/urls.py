from django.urls import path

from Comercio_KAA import views

urlpatterns = [
    path('',views.home, name="Home"),
    path('acerca_de',views.acerca_de, name="Acerca de"),
    path('producto/<slug:slug>',views.producto, name="Producto"),
    path('busqueda/',views.busqueda_cat, name="Busqueda"),
    path('categoria/<slug:slug>',views.categoria, name="Categoria")
]