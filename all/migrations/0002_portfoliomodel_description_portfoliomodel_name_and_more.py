# Generated by Django 4.1.4 on 2022-12-28 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('all', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfoliomodel',
            name='description',
            field=models.CharField(blank=True, max_length=55, null=True),
        ),
        migrations.AddField(
            model_name='portfoliomodel',
            name='name',
            field=models.CharField(blank=True, max_length=55, null=True),
        ),
        migrations.AlterField(
            model_name='contactmodel',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='contactmodel',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contactmodel',
            name='name',
            field=models.CharField(blank=True, max_length=155, null=True),
        ),
    ]
