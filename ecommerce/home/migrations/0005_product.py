# Generated by Django 5.1.4 on 2025-01-09 08:37

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_maincategory_alter_banner_discount_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, null=True)),
                ('price', models.PositiveBigIntegerField(default=0, null=True)),
                ('discount', models.PositiveBigIntegerField(default=0, null=True)),
                ('featured_image', models.CharField(max_length=250)),
                ('brand', models.CharField(max_length=250, null=True)),
                ('total', models.PositiveBigIntegerField(default=0, null=True)),
                ('available', models.PositiveBigIntegerField(default=0, null=True)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('product_information', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('tags', models.CharField(blank=True, max_length=250)),
                ('slug', models.CharField(blank=True, max_length=250)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='home.category')),
            ],
        ),
    ]
