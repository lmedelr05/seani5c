from django.db import models

# Create your models here.
class Career(models.Model):
    LEVELS=[
        ('Ing', 'Ingenieria'),
        ('TSU', 'Tecnico Superios Universitario'),
        ('M', 'Maestria')
    ]
    name = models.CharField(max_length=200,
                            verbose_name = 'Nombre')
    short_name = models.CharField(max_length= 20,
                                  verbose_name = 'Abreviatura')
    level = models.CharField(max_length = 30,
                             verbose_name = 'Nivel',
                             choices= LEVELS)
    
    def __str__(self) :
        return f"{ self.level } - { self.short_name }"

    class Meta:
        verbose_name = 'Carrera'
        verbose_name_plural = 'Carreras' 