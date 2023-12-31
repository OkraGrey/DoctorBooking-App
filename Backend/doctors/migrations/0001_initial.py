# Generated by Django 4.2.3 on 2023-08-07 04:10

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
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_surgeon', models.BooleanField(default=False)),
                ('is_available_online', models.BooleanField(default=False)),
                ('cnic', models.CharField(max_length=15)),
                ('consultation_fee', models.DecimalField(decimal_places=2, max_digits=8, null=True)),
                ('about', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialty_description', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Specialities',
            },
        ),
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot_date', models.DateField(null=True)),
                ('start_time', models.TimeField(null=True)),
                ('end_time', models.TimeField(null=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='time_slots', to='doctors.doctor')),
            ],
        ),
        migrations.AddField(
            model_name='doctor',
            name='speciality',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='doctors.speciality'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
