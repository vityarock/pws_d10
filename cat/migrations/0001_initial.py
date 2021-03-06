# Generated by Django 4.0 on 2021-12-13 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor', models.CharField(max_length=64)),
                ('name', models.CharField(max_length=64)),
                ('year', models.PositiveIntegerField()),
                ('transmission', models.SmallIntegerField(choices=[(1, 'Автоматическая'), (2, 'Роботизированная'), (3, 'Механическая'), (4, 'Вариатор')])),
                ('color', models.CharField(max_length=64)),
            ],
        ),
    ]
