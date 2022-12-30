from django.db import models

# Create your models here.
class Tasks(models.Model):#here you can add new class modules in data base
    task_name = models.CharField("Name of the task", max_length =70)  
    task_info = models.TextField("Description of the task")
    taskdeadline = models.IntegerField("Dead line")


    def __str__(self):
        return self.task_name
    
    #class Meta:         to change the name of a class 
    #   verbose_name = ""  
    #   verbose_name_plural =""