# Generated by Django 3.1.7 on 2021-02-24 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blessing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(default='Count your blessings.')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commenter', models.CharField(max_length=100)),
                ('content', models.TextField(default='Post comment here!')),
                ('blessing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='bless.blessing')),
            ],
        ),
    ]
