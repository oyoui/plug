# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-13 09:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0004_auto_20170913_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='m2m',
            field=models.ManyToManyField(null=True, to='app01.Role', verbose_name='角色'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='ug',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app01.UserGroup', verbose_name='用户组'),
        ),
    ]
