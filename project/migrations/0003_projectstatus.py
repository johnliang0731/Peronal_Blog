# Generated by Django 3.0.3 on 2020-07-08 03:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_project_reference_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_status', models.IntegerField(choices=[(1, 'Po Processing'), (2, 'Material Delivering'), (3, 'In Stock'), (4, 'On Process'), (5, 'Finished'), (6, 'Paused'), (7, 'Cancelled'), (8, 'Other')])),
                ('project_father', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='status', to='project.Project')),
            ],
        ),
    ]
