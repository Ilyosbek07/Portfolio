# Generated by Django 4.1.4 on 2023-01-02 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('all', '0003_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='year_in_school',
        ),
        migrations.AddField(
            model_name='student',
            name='javobi',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default='1', max_length=2),
        ),
    ]
