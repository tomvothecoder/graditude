# Generated by Django 2.2.4 on 2019-09-02 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_auto_20190901_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='link',
            field=models.TextField(),
        ),
    ]
