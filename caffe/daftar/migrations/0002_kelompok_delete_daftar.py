# Generated by Django 4.2.1 on 2023-06-13 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daftar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='kelompok',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=12)),
                ('keterangan', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='daftar',
        ),
    ]
