# Generated by Django 5.1.4 on 2025-01-02 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='Images/sliderjpg')),
                ('deal', models.CharField(choices=[('New Deal', 'New Deal'), ('New Arrivals', 'New Arrivals'), ('Hot Deals', 'Hot Deals'), ('Best Seller', 'Best Seller')], max_length=250)),
                ('discount', models.PositiveBigIntegerField(default=0, null=True)),
            ],
        ),
    ]