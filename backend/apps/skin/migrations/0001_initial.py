# Generated by Django 3.0.8 on 2020-08-28 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125)),
                ('description', models.TextField()),
                ('avatar', models.URLField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('model_file', models.URLField()),
                ('texture_file', models.URLField()),
                ('voiceline_file', models.URLField()),
            ],
        ),
    ]
