# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('lastname', models.CharField(max_length=50, null=True, verbose_name='Apellidos')),
                ('description', models.TextField(verbose_name='Extras', blank=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nameSchool', models.CharField(max_length=50, verbose_name='Nombre de la escuela')),
                ('like', models.CharField(max_length=50, verbose_name='tipo de escuela', choices=[(b'Elementary', b'Elementary'), (b'High School', b'High School'), (b'University', b'University')])),
                ('name', models.ForeignKey(verbose_name=b'Nombre del alumno', to='app.Client')),
            ],
            options={
                'verbose_name': 'School',
                'verbose_name_plural': 'School',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='school',
            unique_together=set([('nameSchool', 'like')]),
        ),
    ]
