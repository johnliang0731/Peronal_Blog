# Generated by Django 3.0.3 on 2020-05-31 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work_instruction', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='widoc',
            name='doc_date',
            field=models.DateField(auto_now=True),
        ),
    ]
