# Generated by Django 4.0 on 2024-03-20 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='risk_assessment',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4),
        ),
    ]
