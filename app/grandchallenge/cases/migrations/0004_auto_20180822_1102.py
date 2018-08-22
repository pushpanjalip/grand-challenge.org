# Generated by Django 2.0.8 on 2018-08-22 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("datasets", "0001_initial"),
        ("cases", "0003_auto_20180821_1045"),
    ]

    operations = [
        migrations.AddField(
            model_name="rawimageuploadsession",
            name="annotationset",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="datasets.AnnotationSet",
            ),
        ),
        migrations.AddField(
            model_name="rawimageuploadsession",
            name="imageset",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="datasets.ImageSet",
            ),
        ),
    ]
