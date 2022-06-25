# Generated by Django 2.2.11 on 2020-08-18 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0117_v400_remove_cloudforms_inventory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='scm_type',
            field=models.CharField(
                blank=True,
                choices=[
                    ('', 'Manual'),
                    ('git', 'Git'),
                    ('hg', 'Mercurial'),
                    ('svn', 'Subversion'),
                    ('insights', 'Red Hat Insights'),
                    ('archive', 'Remote Archive'),
                ],
                default='',
                help_text='Specifies the source control system used to store the project.',
                max_length=8,
                verbose_name='SCM Type',
            ),
        ),
        migrations.AlterField(
            model_name='projectupdate',
            name='scm_type',
            field=models.CharField(
                blank=True,
                choices=[
                    ('', 'Manual'),
                    ('git', 'Git'),
                    ('hg', 'Mercurial'),
                    ('svn', 'Subversion'),
                    ('insights', 'Red Hat Insights'),
                    ('archive', 'Remote Archive'),
                ],
                default='',
                help_text='Specifies the source control system used to store the project.',
                max_length=8,
                verbose_name='SCM Type',
            ),
        ),
    ]
