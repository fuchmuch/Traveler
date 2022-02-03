# Generated by Django 4.0.2 on 2022-02-03 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('traveler', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('photo_url', models.TextField()),
                ('description', models.TextField()),
                ('food', models.CharField(max_length=100)),
                ('landmarks', models.CharField(max_length=100)),
                ('cost', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='country',
            name='photo_url',
            field=models.TextField(),
        ),
        migrations.DeleteModel(
            name='Location',
        ),
        migrations.AddField(
            model_name='destination',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destinations', to='traveler.country'),
        ),
    ]
