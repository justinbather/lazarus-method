# Generated by Django 4.1.7 on 2023-05-23 19:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('program', models.CharField(choices=[('Empowered Explorer', 'Empowered Explorer'), ('Tailored Trailblazer', 'Tailored Trailblazer'), ('Personalized Pathfinder', 'Personalized Pathfinder')], max_length=28)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('is_admin', models.BooleanField(default=False)),
                ('onboarding_complete', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Belt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('belt_colour', models.CharField(choices=[('White', 'White'), ('Yellow', 'Yellow'), ('Green', 'Green'), ('Blue', 'Blue'), ('Orange', 'Orange'), ('Purple', 'Purple')], default='White', max_length=32)),
                ('completed', models.BooleanField(blank=True, default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_type', models.CharField(choices=[('Nourish', 'Nourish'), ('Move', 'Move'), ('Rest', 'Rest'), ('Connect', 'Connect'), ('Learn', 'Learn'), ('Spark', 'Spark'), ('Challenge', 'Challenge')], max_length=20)),
                ('completed', models.BooleanField(blank=True, default=False)),
                ('belt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.belt')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserEntryPatientTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_date', models.DateField(default=django.utils.timezone.now)),
                ('exam_number', models.IntegerField(choices=[(1, '1'), (2, '2')], default=1, verbose_name='Exam Number')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Weight (lbs)')),
                ('age', models.IntegerField()),
                ('height', models.IntegerField(blank=True, null=True, verbose_name='Height (inches)')),
                ('fasting_glucose', models.IntegerField(verbose_name='Fasting Glucose')),
                ('hga1c', models.IntegerField(verbose_name='HgA1c')),
                ('cprotein', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='C Reactive Protein')),
                ('homocysteine', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Homocysteine')),
                ('fasting_insulin', models.IntegerField(verbose_name='Fasting Insulin')),
                ('ldl_particle', models.IntegerField(verbose_name='LDL Particle Number')),
                ('ldl_size', models.IntegerField(verbose_name='LDL Size')),
                ('insulin_resistance', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Insulin Resistance Score')),
                ('testosterone', models.IntegerField(choices=[(10, '10'), (7, '7'), (5, '5'), (3, '3'), (1, '1')], verbose_name='Testosterone')),
                ('thyroid', models.IntegerField(choices=[(10, '10'), (7, '7'), (5, '5'), (3, '3'), (1, '1')], verbose_name='Thyroid Stimulating Hormone')),
                ('vitamin_d3', models.IntegerField(verbose_name='Vitamin D3')),
                ('vitamin_b12', models.IntegerField(verbose_name='Vitamin B12')),
                ('zinc_rbc', models.IntegerField(verbose_name='Zinc RBC')),
                ('magnesium_rbc', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Magnesium RBC')),
                ('omega3_index', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Omega 3 Index')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=200)),
                ('completed', models.BooleanField(blank=True, default=False)),
                ('belt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.belt')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('belt', models.CharField(choices=[('White', 'White'), ('Yellow', 'Yellow'), ('Green', 'Green'), ('Blue', 'Blue'), ('Orange', 'Orange'), ('Purple', 'Purple'), ('None', 'None')], max_length=10)),
                ('category', models.CharField(choices=[('Nourish', 'Nourish'), ('Move', 'Move'), ('Rest', 'Rest'), ('Connect', 'Connect'), ('Learn', 'Learn'), ('Spark', 'Spark'), ('Challenge', 'Challenge')], max_length=15)),
                ('score', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PatientTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_date', models.DateField(default=django.utils.timezone.now)),
                ('exam_number', models.IntegerField(choices=[(1, '1'), (2, '2')], default=1, verbose_name='Exam Number')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Weight (lbs)')),
                ('age', models.IntegerField()),
                ('height', models.IntegerField(blank=True, null=True, verbose_name='Height (inches)')),
                ('fasting_glucose', models.IntegerField(blank=True, verbose_name='Fasting Glucose')),
                ('hga1c', models.IntegerField(blank=True, verbose_name='HgA1c')),
                ('cprotein', models.DecimalField(blank=True, decimal_places=2, max_digits=5, verbose_name='C Reactive Protein')),
                ('homocysteine', models.DecimalField(blank=True, decimal_places=2, max_digits=5, verbose_name='Homocysteine')),
                ('fasting_insulin', models.IntegerField(blank=True, verbose_name='Fasting Insulin')),
                ('ldl_particle', models.IntegerField(blank=True, verbose_name='LDL Particle Number')),
                ('ldl_size', models.IntegerField(blank=True, verbose_name='LDL Size')),
                ('insulin_resistance', models.DecimalField(blank=True, decimal_places=2, max_digits=4, verbose_name='Insulin Resistance Score')),
                ('testosterone', models.IntegerField(blank=True, choices=[(10, '10'), (7, '7'), (5, '5'), (3, '3'), (1, '1')], verbose_name='Testosterone')),
                ('thyroid', models.IntegerField(blank=True, choices=[(10, '10'), (7, '7'), (5, '5'), (3, '3'), (1, '1')], verbose_name='Thyroid Stimulating Hormone')),
                ('vitamin_d3', models.IntegerField(blank=True, verbose_name='Vitamin D3')),
                ('vitamin_b12', models.IntegerField(blank=True, verbose_name='Vitamin B12')),
                ('zinc_rbc', models.IntegerField(blank=True, verbose_name='Zinc RBC')),
                ('magnesium_rbc', models.DecimalField(blank=True, decimal_places=2, max_digits=5, verbose_name='Magnesium RBC')),
                ('omega3_index', models.DecimalField(blank=True, decimal_places=2, max_digits=5, verbose_name='Omega 3 Index')),
                ('nourish_grade', models.IntegerField(blank=True, choices=[(10, '10'), (7, '7'), (5, '5'), (3, '3'), (1, '1')], null=True, verbose_name='Nourish Grade')),
                ('joint_mobility', models.IntegerField(blank=True, choices=[(10, '10'), (7, '7'), (5, '5'), (3, '3'), (1, '1')], verbose_name='Joint Mobility')),
                ('muscle_flexibility', models.IntegerField(blank=True, choices=[(10, '10'), (7, '7'), (5, '5'), (3, '3'), (1, '1')], verbose_name='Muscle Flexibility')),
                ('core_strength', models.IntegerField(blank=True, choices=[(10, '10'), (7, '7'), (5, '5'), (3, '3'), (1, '1')], verbose_name='Core Strength')),
                ('postural_analysis', models.IntegerField(blank=True, choices=[(10, '10'), (7, '7'), (5, '5'), (3, '3'), (1, '1')], verbose_name='Postural Analysis')),
                ('fat_mass', models.IntegerField(blank=True, verbose_name='Fat Mass')),
                ('body_mass_index', models.IntegerField(blank=True, choices=[(10, '10'), (7, '7'), (5, '5'), (3, '3'), (1, '1')], verbose_name='Body Mass Index')),
                ('move_grade', models.IntegerField(blank=True, choices=[(10, '10'), (7, '7'), (5, '5'), (3, '3'), (1, '1')], verbose_name='Move Grade')),
                ('systolic', models.IntegerField(blank=True, verbose_name='Systolic BP')),
                ('diastolic', models.IntegerField(blank=True, verbose_name='Diastolic BP')),
                ('resting_heart_rate', models.IntegerField(blank=True, verbose_name='Resting Heart Rate')),
                ('rest_grade', models.IntegerField(blank=True, choices=[(10, '10'), (7, '7'), (5, '5'), (3, '3'), (1, '1')], verbose_name='Rest Grade')),
                ('coherence_value', models.DecimalField(blank=True, decimal_places=2, max_digits=4, verbose_name='Coherence Value')),
                ('co2_tolerance', models.IntegerField(blank=True, verbose_name='CO2 Tolerance')),
                ('connect_grade', models.IntegerField(blank=True, choices=[(10, '10'), (7, '7'), (5, '5'), (3, '3'), (1, '1')], verbose_name='Connect Grade')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MCFormQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=100)),
                ('answer', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')])),
                ('category', models.CharField(choices=[('Nourish', 'Nourish'), ('Move', 'Move'), ('Rest', 'Rest'), ('Connect', 'Connect'), ('Learn', 'Learn'), ('Spark', 'Spark'), ('Challenge', 'Challenge')], max_length=15)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FormQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=100)),
                ('answer', models.BooleanField(default=False)),
                ('category', models.CharField(choices=[('Nourish', 'Nourish'), ('Move', 'Move'), ('Rest', 'Rest'), ('Connect', 'Connect'), ('Learn', 'Learn'), ('Spark', 'Spark'), ('Challenge', 'Challenge')], max_length=15)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]