# Generated by Django 3.0.3 on 2020-05-31 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work_instruction', '0002_auto_20200531_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='widoc',
            name='doc_attachment',
            field=models.FileField(upload_to='work_instruction/files/'),
        ),
    ]
