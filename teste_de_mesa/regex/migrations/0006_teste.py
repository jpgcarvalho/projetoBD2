# Generated by Django 4.0.5 on 2022-07-03 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regex', '0005_testemesa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linha', models.IntegerField()),
                ('index', models.IntegerField()),
                ('variavel_o', models.CharField(max_length=50)),
                ('variavel_p', models.CharField(max_length=50)),
                ('codigo_linha', models.CharField(max_length=1000)),
            ],
        ),
    ]
