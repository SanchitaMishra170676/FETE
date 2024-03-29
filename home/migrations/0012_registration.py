# Generated by Django 3.2.3 on 2021-07-10 14:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.CharField(max_length=3)),
                ('email', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=13)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=100)),
                ('occupation', models.CharField(max_length=50)),
                ('college', models.CharField(blank=True, max_length=255)),
                ('course', models.CharField(blank=True, max_length=255)),
                ('experience', models.TextField()),
                ('inspiration', models.TextField()),
                ('proof', models.ImageField(default='', upload_to='media/Home/RegistrationProof')),
                ('answered', models.BooleanField(default=False)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
