# Generated by Django 3.2.5 on 2021-07-01 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pic_exchange', '0002_auto_20210701_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='original_picture',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='picture',
            name='sized_picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]