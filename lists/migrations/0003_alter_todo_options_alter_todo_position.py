# Generated by Django 4.0.4 on 2022-05-22 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0002_todo_position'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'ordering': ('position', 'created_at')},
        ),
        migrations.AlterField(
            model_name='todo',
            name='position',
            field=models.FloatField(null=True),
        ),
    ]
