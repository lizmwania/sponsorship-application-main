# Generated by Django 3.2.7 on 2022-10-16 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicationDetails', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='applications',
            old_name='academic_level',
            new_name='academicLevel',
        ),
        migrations.RenameField(
            model_name='applications',
            old_name='year_of_completion',
            new_name='completionYear',
        ),
        migrations.RenameField(
            model_name='applications',
            old_name='address',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='applications',
            old_name='first_name',
            new_name='firstName',
        ),
        migrations.RenameField(
            model_name='applications',
            old_name='last_name',
            new_name='homeAddress',
        ),
        migrations.RenameField(
            model_name='applications',
            old_name='phone_number',
            new_name='lastName',
        ),
        migrations.RenameField(
            model_name='applications',
            old_name='reason_sponsorship',
            new_name='reason',
        ),
        migrations.RemoveField(
            model_name='applications',
            name='birth_certificate',
        ),
        migrations.RemoveField(
            model_name='applications',
            name='id_certificate',
        ),
        migrations.RemoveField(
            model_name='applications',
            name='recommendation_letter',
        ),
        migrations.AddField(
            model_name='applications',
            name='certFile',
            field=models.FileField(blank=True, upload_to='Documents'),
        ),
        migrations.AddField(
            model_name='applications',
            name='idFile',
            field=models.FileField(blank=True, upload_to='Documents'),
        ),
        migrations.AddField(
            model_name='applications',
            name='phone',
            field=models.IntegerField(default=241554411),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='applications',
            name='schoolAddress',
            field=models.CharField(default=5545, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='applications',
            name='schoolName',
            field=models.CharField(default=5, max_length=100),
            preserve_default=False,
        ),
    ]
