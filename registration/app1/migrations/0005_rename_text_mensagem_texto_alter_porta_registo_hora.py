# Generated by Django 4.1.1 on 2023-08-07 15:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_mensagem_alter_porta_registo_hora'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mensagem',
            old_name='text',
            new_name='texto',
        ),
        migrations.AlterField(
            model_name='porta',
            name='registo_hora',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 7, 16, 21, 30, 867817)),
        ),
    ]