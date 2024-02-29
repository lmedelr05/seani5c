from django.db import models

# Create your models here.

class Module(models.Model):
    name = models.CharField( max_length=100, 
                            verbose_name="Nombre" )
    description = models.CharField(max_length=200,
                                   verbose_name="Descripcion")

    @property                               
    def num_questions(self):
        return self.question_set.count()

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'modulo'
        verbose_name_plural = 'modulos'

class Question(models.Model):
    module = models.ForeignKey(
        Module, 
        on_delete = models.CASCADE,
        verbose_name ='Modulo')
    question_text = models.CharField(max_length=200,
                                     verbose_name='Texto de la pregunta', 
                                     null = True,
                                     blank=True)
    question_image= models.ImageField(upload_to='questions',
                                  verbose_name="Imagen de la pregunta",
                                  null=True,
                                  blank=True)
    answer1 = models.CharField(max_length=200,
                               verbose_name = 'Respuesta A')
    answer2 = models.CharField(max_length=200,
                               verbose_name = 'Respuesta B')
    answer3 = models.CharField(max_length=200,
                               verbose_name = 'Respuesta C',
                               null=True,
                               blank=True)
    answer4 = models.CharField(max_length=200,
                               verbose_name = 'Respuesta D',
                               null=True,
                               blank=True)
    correct = models.CharField(max_length=5,
                               verbose_name = 'Respuesta correcta')
    
    def __str__(self) :
        return f"{self.module} - {self.id}"
    
    class Meta:
        verbose_name = 'pregunta'
        verbose_name_plural = 'preguntas'
