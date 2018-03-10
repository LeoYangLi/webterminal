# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-05 13:14
from __future__ import unicode_literals

from django.db import migrations, models
import elfinder.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='YawdElfinderTestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('anyfile', elfinder.fields.ElfinderField(help_text=b'This is the default configuration', max_length=100)),
                ('image', elfinder.fields.ElfinderField(help_text=b'This field uses the "image" optionset', max_length=100)),
                ('pdf', elfinder.fields.ElfinderField(blank=True, help_text=b'This field uses the "pdf" custom optionset, set in the project settings file', max_length=100, null=True)),
            ],
        ),
    ]
