# Generated by Django 4.1.7 on 2023-03-28 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ForoApp', '0005_remove_profile_instagram'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='nombre',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]