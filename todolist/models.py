from django.db import models

# Create your models here.
class Tarefa(models.Model): # Define a model for tasks
    STATUS_CHOICES = [ # Define choices for task status
        ('AF', 'A Fazer'),
        ('FN', 'Finalizado'),
        ('EM', 'Fazendo'),
    ]
    tarefa = models.CharField(max_length=100) # Task description
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='AF') # Task status

    def __str__(self): # String representation of the model
        return self.tarefa # Returns the task description when the model instance is printed