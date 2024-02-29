from django.db import models
from career.models import Career
from django.contrib.auth.models import User
from library.models import Module

# Create your models here.
class Stage(models.Model):
    stage = models.IntegerField(
        verbose_name =  "Etapa",
        max_length=2
        )
    application_date = models.DateField(
        verbose_name = "Fecha de aplicacion"
    )
    
    @property
    def year(self):
        return self.application_date.year
    
    @property
    def month(self):
        months = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio' , 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']

        return months[self.application_date.month - 1]
    
    def __str__(self):
        return f"{ self.stage } - {self.month } - { self.year }"
    
    class Meta:
        verbose_name = "Etapa"
        verbose_name_plural = "Etapas"

class Exam(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, verbose_name = 'Usuarios')
    stage = models.ForeignKey(Stage, on_delete = models.CASCADE, verbose_name = 'Etapa')
    career = models.ForeignKey(Career, on_delete = models.CASCADE, verbose_name = 'Carrera')
    modules = models.ManyToManyField(Module, through='ExamModule', verbose_name = 'Modulos')
    score = models.FloatField(verbose_name = 'Calidicacion', default = 0.0)

class ExamModule(models.Model):
    exam = models.ForeignKey(Exam, on_delete = models.CASCADE, verbose_name = 'Examen')
    module = models.ForeignKey(Module, on_delete = models.CASCADE, verbose_name = 'Modulo')
    active = models.BooleanField(verbose_name = 'Activo', default = True)
    score = models.FloatField(verbose_name = 'Calificacion', default = 0.0)


