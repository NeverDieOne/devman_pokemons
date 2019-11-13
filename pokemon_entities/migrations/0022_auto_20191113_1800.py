# Generated by Django 2.2.6 on 2019-11-13 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0021_auto_20191113_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='previous_evolution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='next_evolutions', to='pokemon_entities.Pokemon', verbose_name='Предыдущая эволюция'),
        ),
    ]