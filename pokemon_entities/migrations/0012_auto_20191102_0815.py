# Generated by Django 2.2.6 on 2019-11-02 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0011_auto_20191102_0815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='evolution',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pokemon_entities.Pokemon'),
        ),
    ]