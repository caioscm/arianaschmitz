# Generated by Django 3.0.2 on 2020-06-16 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutri', '0007_auto_20200608_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receitas',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='fotos/%d/%m/%y', verbose_name='imagem'),
        ),
    ]
