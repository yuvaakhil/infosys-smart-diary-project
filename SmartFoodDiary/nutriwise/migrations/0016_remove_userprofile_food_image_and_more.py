# Generated by Django 5.1.4 on 2024-12-19 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutriwise', '0015_alter_fooddiaryentry_calories_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='food_image',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='prediction_data',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='calorie_goal',
            field=models.PositiveIntegerField(default=2000),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='carbs_goal',
            field=models.FloatField(default=300.0),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='diet_type',
            field=models.CharField(choices=[('None', 'None'), ('Vegetarian', 'Vegetarian'), ('Vegan', 'Vegan'), ('Keto', 'Keto'), ('Paleo', 'Paleo')], default='None', max_length=20),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='enable_notifications',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='fats_goal',
            field=models.FloatField(default=70.0),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='food_restrictions',
            field=models.TextField(blank=True, help_text='Comma-separated list of restricted foods (e.g., peanuts, gluten)', null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='last_notified',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='notify_on_deficit',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='notify_on_exceed',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='protein_goal',
            field=models.FloatField(default=50.0),
        ),
    ]
