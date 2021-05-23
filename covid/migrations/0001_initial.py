# Generated by Django 3.2.3 on 2021-05-23 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True, verbose_name='name:')),
                ('result', models.CharField(max_length=50, null=True, verbose_name='result:')),
                ('cough', models.IntegerField(null=True, verbose_name='cough:')),
                ('fever', models.IntegerField(null=True, verbose_name='fever:')),
                ('sore', models.IntegerField(null=True, verbose_name='sore:')),
                ('male', models.IntegerField(null=True, verbose_name='male:')),
                ('breath', models.IntegerField(null=True, verbose_name='breath:')),
                ('head', models.IntegerField(null=True, verbose_name='head:')),
                ('older', models.IntegerField(null=True, verbose_name='older:')),
                ('patient', models.IntegerField(null=True, verbose_name='patient:')),
            ],
        ),
    ]
