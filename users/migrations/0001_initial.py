# Generated by Django 3.1.6 on 2021-02-06 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('level', models.IntegerField()),
                ('class_held', models.CharField(choices=[('Jss1', 'Jss1'), ('Jss2', 'Jss2'), ('Jss3', 'Jss3'), ('Sss1', 'Sss1'), ('Sss2', 'Sss2'), ('Sss3', 'Sss3')], max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('class_in', models.CharField(max_length=5)),
                ('teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='students', to='users.teacher')),
            ],
            options={
                'ordering': ['-class_in'],
            },
        ),
    ]
