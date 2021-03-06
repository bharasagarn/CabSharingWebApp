# Generated by Django 3.0.5 on 2020-07-25 03:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfileInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=13)),
                ('profile_pic', models.ImageField(blank=True, upload_to='profile_pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LookingCab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('source', models.CharField(choices=[('1', 'IITG_Campus'), ('2', 'Guwahati Airport'), ('3', 'GHY RLY Station'), ('4', 'Kamakhya Junction')], max_length=50)),
                ('dest', models.CharField(choices=[('1', 'IITG_Campus'), ('2', 'Guwahati Airport'), ('3', 'GHY RLY Station'), ('4', 'Kamakhya Junction')], max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BookedCab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('source', models.CharField(choices=[('1', 'IITG_Campus'), ('2', 'Guwahati Airport'), ('3', 'GHY RLY Station'), ('4', 'Kamakhya Junction')], max_length=50)),
                ('dest', models.CharField(choices=[('1', 'IITG_Campus'), ('2', 'Guwahati Airport'), ('3', 'GHY RLY Station'), ('4', 'Kamakhya Junction')], max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
