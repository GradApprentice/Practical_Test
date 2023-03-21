# Generated by Django 2.1.5 on 2023-03-21 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pTest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newsTitle', models.CharField(max_length=128)),
                ('newsAuthor', models.CharField(max_length=128)),
                ('newsDate', models.CharField(max_length=128)),
                ('newsDescription', models.CharField(max_length=128)),
            ],
        ),
        migrations.RemoveField(
            model_name='page',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Page',
        ),
    ]