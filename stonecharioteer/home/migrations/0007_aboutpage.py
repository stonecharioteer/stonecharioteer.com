# Generated by Django 2.0.13 on 2019-09-12 16:28

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('home', '0006_auto_20190912_1610'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('body', wagtail.core.fields.RichTextField(blank=True)),
            ],
            options={
                'verbose_name': 'About Page',
                'verbose_name_plural': 'About Pages',
            },
            bases=('wagtailcore.page',),
        ),
    ]