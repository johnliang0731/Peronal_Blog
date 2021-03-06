# Generated by Django 3.0.3 on 2020-05-27 03:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus_type', models.IntegerField(choices=[(1, 'K7M'), (2, 'K8M'), (3, 'K9M')])),
                ('project_name', models.CharField(max_length=255)),
                ('module_type', models.IntegerField(choices=[(1, 'Traditional'), (2, 'Liquidcooling'), (3, 'Standardized')])),
                ('bus_number', models.IntegerField()),
            ],
            options={
                'ordering': ['bus_type'],
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255)),
                ('document', models.FileField(upload_to='project/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('project_father', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='docu', to='project.Project')),
            ],
        ),
    ]
