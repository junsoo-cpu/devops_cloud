# Generated by Django 3.2.9 on 2021-12-08 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(db_index=True, max_length=50)),
            ],
            options={
                'verbose_name': '태그',
                'verbose_name_plural': '태그 목록',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(db_index=True, max_length=20)),
                ('author_name', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('photo', models.ImageField(upload_to='carol/%Y/%m/%d')),
                ('tag_set', models.ManyToManyField(to='carol.Tag')),
            ],
            options={
                'verbose_name': '캐롤',
                'verbose_name_plural': '캐롤 목록',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=20)),
                ('message', models.TextField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carol.post')),
            ],
            options={
                'verbose_name': '댓글',
                'verbose_name_plural': '댓글 목록',
            },
        ),
    ]