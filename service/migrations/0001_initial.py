# Generated by Django 2.2.4 on 2019-08-10 12:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ColorBoard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('players_count', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)], verbose_name='Number of players')),
                ('board', models.TextField(verbose_name='Sequence of characters on the board')),
                ('cards', models.TextField(verbose_name='Cards in the deck')),
                ('winner', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)], verbose_name='Winner of game')),
                ('last_move', models.PositiveIntegerField(verbose_name='Number of last move in game')),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'ColorBoard Game',
                'verbose_name_plural': 'ColorBoard Games',
                'db_table': 'service_game_color_board',
            },
        ),
    ]