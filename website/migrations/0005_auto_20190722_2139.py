# Generated by Django 2.2.3 on 2019-07-22 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_student_class_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='class_room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='students', to='website.ClassRoom'),
        ),
    ]
