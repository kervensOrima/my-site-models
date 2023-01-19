# Generated by Django 4.1.5 on 2023-01-18 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musique', '0006_place_restaurant'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('article_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'Article',
                'ordering': ['article_id'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'Book',
                'ordering': ['book_id'],
            },
        ),
        migrations.CreateModel(
            name='BookReview',
            fields=[
                ('book_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='musique.book')),
                ('article_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='musique.article')),
                ('registered_date', models.DateField()),
            ],
            options={
                'db_table': 'BookReview',
                'ordering': ['registered_date'],
            },
            bases=('musique.article', 'musique.book'),
        ),
    ]