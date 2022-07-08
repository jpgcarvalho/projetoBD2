# Generated by Django 4.0.5 on 2022-07-02 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_alter_testemesa_data_teste_mesa'),
    ]

    operations = [
        migrations.CreateModel(
            name='DicionarioParametros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linha', models.IntegerField()),
                ('fk_teste', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.testemesa')),
            ],
        ),
        migrations.CreateModel(
            name='ValorParametro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parametro', models.CharField(db_index=True, max_length=240)),
                ('valor', models.CharField(db_index=True, max_length=240)),
                ('container', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.dicionarioparametros')),
            ],
        ),
    ]
