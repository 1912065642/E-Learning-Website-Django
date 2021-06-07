# Generated by Django 3.1.7 on 2021-05-04 14:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0002_course_instructor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='instructor',
            field=models.ForeignKey(db_column='instructor', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]