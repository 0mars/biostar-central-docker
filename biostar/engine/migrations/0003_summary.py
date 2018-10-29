# Generated by Django 2.1.2 on 2018-10-28 18:46

from django.db import migrations


def format_summary(apps, schema_editor):
    """Format summary so it is the first line of the  """

    recipes = apps.get_model('engine', 'Analysis')
    for recipe in recipes.objects.all():
        first_line = recipe.text.splitlines()[0]

        # Set recipe.summary as the first line of the recipe.text
        recipe.summary = first_line
        recipe.save()

    return


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0002_bigint'),
    ]

    operations = [
        migrations.RunPython(format_summary),
    ]
