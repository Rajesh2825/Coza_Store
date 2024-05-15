# Generated by Django 5.0.2 on 2024-03-16 09:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_cart'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Wish',
            fields=[
                ('cid', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('p_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
                ('u_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]