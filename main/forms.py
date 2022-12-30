from .models import Tasks
from django.forms import ModelForm, TextInput, NumberInput,Textarea


class TasksForm(ModelForm):
    class Meta:
        model = Tasks
        fields = ["task_name", "task_info","taskdeadline" ]
        widgets = {
            "task_name":TextInput(attrs={
                'class':'form-control',
                'placeholder':'Enter your title'
        }),
        "task_info":Textarea(attrs={
                'class':'form-control',
                'placeholder':'Enter your description'
        }),
        "taskdeadline":NumberInput(attrs={
                'class':'form-control',
                'placeholder':'Enter number of day'
        }),
        }