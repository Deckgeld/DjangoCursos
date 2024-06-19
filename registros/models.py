from django.db import models

# Create your models here.
class Cursos(models.Model): #Define la estructura de nuestra tabla
    id = models.PositiveIntegerField(primary_key=True) #Número entero positivo
    nombre = models.TextField() #Texto largo
    categoria = models.TextField()
    autor = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2,) #Número con decimales
    likes = models.PositiveIntegerField()
    imagen = models.ImageField(null=True,upload_to="fotos",verbose_name="Fotografía")
    created = models.DateTimeField(auto_now_add=True) #Fecha y tiempo
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ["created"]
        #el menos indica que se ordenara del más reciente al mas viejo
    
    def __str__(self):
        return self.nombre
        #Indica que se mostrára el nombre como valor en la tabla