# Generated by Django 4.1.6 on 2023-02-05 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UserForm",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("firstname", models.CharField(max_length=50)),
                ("lastname", models.CharField(max_length=50)),
                ("date_of_birth", models.DateField(max_length=8)),
                ("uploaded_file", models.FileField(upload_to="")),
            ],
            options={
                "db_table": "user_profile",
                "managed": True,
            },
        ),
    ]