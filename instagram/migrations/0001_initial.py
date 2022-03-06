# Generated by Django 4.0.3 on 2022-03-06 18:28

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='photos')),
                ('img_name', models.CharField(blank=True, max_length=30)),
                ('img_caption', models.TextField()),
                ('img_likes', models.IntegerField(default=0)),
                ('post_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prof_image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='photos')),
                ('bio', models.CharField(blank=True, max_length=30, null=True)),
                ('name', models.CharField(blank=True, max_length=30)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instagram.image')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='instagram.profile'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=30)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instagram.image')),
                ('user', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
