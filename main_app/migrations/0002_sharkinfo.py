# Generated by Django 4.2.2 on 2023-07-11 03:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SharkInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('species', models.CharField(max_length=100)),
                ('discovered', models.IntegerField(default=0)),
                ('shark', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='more', to='main_app.shark')),
            ],
            options={
                'ordering': ['species'],
            },
        ),
    ]