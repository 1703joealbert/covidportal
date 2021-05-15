# Generated by Django 3.2.1 on 2021-05-15 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beds', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='category',
            field=models.CharField(choices=[('C', 'Covid'), ('I', 'ICU'), ('V', 'Ventilator'), ('N', 'Normal')], max_length=4),
        ),
    ]
