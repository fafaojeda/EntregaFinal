# Generated by Django 2.0 on 2022-09-28 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='borrar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bor', models.CharField(max_length=50)),
            ],
        ),
    ]
