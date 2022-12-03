# Generated by Django 4.1.3 on 2022-12-03 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_dashboard', '0002_student_proctor_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='CGPA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('USN', models.CharField(max_length=10)),
                ('total_credits_registered', models.DecimalField(decimal_places=0, max_digits=2)),
                ('total_credits_earned', models.DecimalField(blank=True, decimal_places=0, max_digits=2)),
                ('cgpa', models.DecimalField(decimal_places=0, max_digits=1)),
                ('sem', models.DecimalField(decimal_places=0, max_digits=1)),
            ],
            options={
                'ordering': ['USN'],
            },
        ),
        migrations.CreateModel(
            name='FastTrack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('USN', models.CharField(max_length=10)),
                ('courseName', models.TextField()),
                ('courseCode', models.TextField()),
                ('credit', models.DecimalField(decimal_places=2, max_digits=3)),
                ('registration', models.TextField()),
                ('attemptNumber', models.DecimalField(blank=True, decimal_places=2, max_digits=2)),
                ('attendance', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('CIE', models.DecimalField(blank=True, decimal_places=2, max_digits=2)),
                ('SEE', models.CharField(max_length=1)),
                ('GradePoints', models.DecimalField(decimal_places=2, max_digits=2)),
            ],
        ),
        migrations.CreateModel(
            name='Sem1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('USN', models.CharField(max_length=10)),
                ('courseName', models.TextField()),
                ('courseCode', models.TextField()),
                ('credit', models.DecimalField(decimal_places=2, max_digits=3)),
                ('registration', models.TextField()),
                ('attemptNumber', models.DecimalField(blank=True, decimal_places=2, max_digits=2)),
                ('attendance', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('CIE', models.DecimalField(blank=True, decimal_places=2, max_digits=2)),
                ('SEE', models.CharField(max_length=1)),
                ('GradePoints', models.DecimalField(decimal_places=2, max_digits=2)),
            ],
        ),
        migrations.CreateModel(
            name='Sem2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('USN', models.CharField(max_length=10)),
                ('courseName', models.TextField()),
                ('courseCode', models.TextField()),
                ('credit', models.DecimalField(decimal_places=2, max_digits=3)),
                ('registration', models.TextField()),
                ('attemptNumber', models.DecimalField(blank=True, decimal_places=2, max_digits=2)),
                ('attendance', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('CIE', models.DecimalField(blank=True, decimal_places=2, max_digits=2)),
                ('SEE', models.CharField(max_length=1)),
                ('GradePoints', models.DecimalField(decimal_places=2, max_digits=2)),
            ],
        ),
        migrations.CreateModel(
            name='Sem3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('USN', models.CharField(max_length=10)),
                ('courseName', models.TextField()),
                ('courseCode', models.TextField()),
                ('credit', models.DecimalField(decimal_places=2, max_digits=3)),
                ('registration', models.TextField()),
                ('attemptNumber', models.DecimalField(blank=True, decimal_places=2, max_digits=2)),
                ('attendance', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('CIE', models.DecimalField(blank=True, decimal_places=2, max_digits=2)),
                ('SEE', models.CharField(max_length=1)),
                ('GradePoints', models.DecimalField(decimal_places=2, max_digits=2)),
            ],
        ),
        migrations.CreateModel(
            name='Sem4',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('USN', models.CharField(max_length=10)),
                ('courseName', models.TextField()),
                ('courseCode', models.TextField()),
                ('credit', models.DecimalField(decimal_places=2, max_digits=3)),
                ('registration', models.TextField()),
                ('attemptNumber', models.DecimalField(blank=True, decimal_places=2, max_digits=2)),
                ('attendance', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('CIE', models.DecimalField(blank=True, decimal_places=2, max_digits=2)),
                ('SEE', models.CharField(max_length=1)),
                ('GradePoints', models.DecimalField(decimal_places=2, max_digits=2)),
            ],
        ),
        migrations.CreateModel(
            name='Sem5',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('USN', models.CharField(max_length=10)),
                ('courseName', models.TextField()),
                ('courseCode', models.TextField()),
                ('credit', models.DecimalField(decimal_places=2, max_digits=3)),
                ('registration', models.TextField()),
                ('attemptNumber', models.DecimalField(blank=True, decimal_places=2, max_digits=2)),
                ('attendance', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('CIE', models.DecimalField(blank=True, decimal_places=2, max_digits=2)),
                ('SEE', models.CharField(max_length=1)),
                ('GradePoints', models.DecimalField(decimal_places=2, max_digits=2)),
            ],
        ),
        migrations.CreateModel(
            name='Sem6',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('USN', models.CharField(max_length=10)),
                ('courseName', models.TextField()),
                ('courseCode', models.TextField()),
                ('credit', models.DecimalField(decimal_places=2, max_digits=3)),
                ('registration', models.TextField()),
                ('attemptNumber', models.DecimalField(blank=True, decimal_places=2, max_digits=2)),
                ('attendance', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('CIE', models.DecimalField(blank=True, decimal_places=2, max_digits=2)),
                ('SEE', models.CharField(max_length=1)),
                ('GradePoints', models.DecimalField(decimal_places=2, max_digits=2)),
            ],
        ),
        migrations.CreateModel(
            name='Sem7',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('USN', models.CharField(max_length=10)),
                ('courseName', models.TextField()),
                ('courseCode', models.TextField()),
                ('credit', models.DecimalField(decimal_places=2, max_digits=3)),
                ('registration', models.TextField()),
                ('attemptNumber', models.DecimalField(blank=True, decimal_places=2, max_digits=2)),
                ('attendance', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('CIE', models.DecimalField(blank=True, decimal_places=2, max_digits=2)),
                ('SEE', models.CharField(max_length=1)),
                ('GradePoints', models.DecimalField(decimal_places=2, max_digits=2)),
            ],
        ),
        migrations.CreateModel(
            name='Sem8',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('USN', models.CharField(max_length=10)),
                ('courseName', models.TextField()),
                ('courseCode', models.TextField()),
                ('credit', models.DecimalField(decimal_places=2, max_digits=3)),
                ('registration', models.TextField()),
                ('attemptNumber', models.DecimalField(blank=True, decimal_places=2, max_digits=2)),
                ('attendance', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('CIE', models.DecimalField(blank=True, decimal_places=2, max_digits=2)),
                ('SEE', models.CharField(max_length=1)),
                ('GradePoints', models.DecimalField(decimal_places=2, max_digits=2)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='current_sem',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=1),
            preserve_default=False,
        ),
    ]