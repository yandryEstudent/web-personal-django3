from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name = 'Titulo')
    description = models.TextField(verbose_name = 'Descripcion')
    image = models.ImageField(verbose_name = 'Imagen', upload_to = "projects")
    created = models.DateTimeField(auto_now_add = True, verbose_name = 'Fecha de creacion')
    updated = models.DateTimeField(auto_now = True, verbose_name = 'Fecha de edicion')
    CampoOpcional = models.URLField(max_length = 100, null = True, blank = True, verbose_name = 'Sitio WEB') 


    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ["-created"]
    
    def __str__(self):
        return self.title