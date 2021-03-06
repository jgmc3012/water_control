# Generated by Django 2.2.3 on 2020-04-08 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('houses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FamilyBoss',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('card_id', models.PositiveIntegerField(unique=True)),
                ('active', models.BooleanField(default=True)),
                ('house', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='houses.House')),
            ],
        ),
    ]
