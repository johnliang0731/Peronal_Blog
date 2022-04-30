# Generated by Django 3.2.3 on 2022-04-30 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work_instruction', '0004_auto_20200707_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='widoc',
            name='doc_type',
            field=models.IntegerField(choices=[(1, 'Resume'), (2, 'Cover Letter'), (3, 'Self Introduction'), (4, 'Portfolio'), (9, 'Other')], default=9),
        ),
    ]