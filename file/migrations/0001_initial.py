# Generated by Django 5.0.6 on 2024-05-15 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('video', models.FileField(upload_to='videos/')),
                ('pdf', models.FileField(blank=True, null=True, upload_to='pdfs/')),
                ('description', models.TextField(blank=True)),
            ],
        ),
    ]
