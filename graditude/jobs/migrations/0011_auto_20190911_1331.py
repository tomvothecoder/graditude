# Generated by Django 2.2.5 on 2019-09-11 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0010_post_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('Software Engineer', 'Software Engineer'), ('Full Stack Engineer', 'Full Stack Engineer'), ('Front End Engineer', 'Back End Engineer'), ('Back End Engineer', 'Back End Engineer')], max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='position',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='jobs.Position'),
        ),
    ]