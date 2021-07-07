from django.db import models
from django.db.models.fields import AutoField
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.

class Categoria (models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=64, help_text="Ingrese el nombre de la categoría:", blank=False)
    descripcion = models.TextField(blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=255)

    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'
            
    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse("Categoria",kwargs={"slug":self.slug})


class Producto (models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=64, help_text="Ingrese el nombre del producto:", blank=False)
    descripcion = models.TextField(blank=False)
    imagen = models.ImageField(upload_to='Comercio_KAA')
    precio = models.FloatField(help_text="Precio en pesos argentinos (AR$)")
    en_stock = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255)

    class Meta:
        verbose_name='producto'
        verbose_name_plural='productos'
    
    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse("Producto",kwargs={"slug":self.slug})