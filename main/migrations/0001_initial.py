# Generated by Django 4.1.2 on 2022-10-18 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=70, verbose_name='Name of the task')),
                ('task_info', models.TextField(verbose_name='Description of the task')),
                
            ],
        ),
    ]
