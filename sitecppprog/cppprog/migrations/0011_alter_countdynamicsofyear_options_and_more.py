# Generated by Django 5.1.4 on 2025-01-20 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cppprog', '0010_vacancytop20skills'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='countdynamicsofyear',
            options={'ordering': ['year', 'vacancies_number'], 'verbose_name': 'Динамика количества вакансий по годам', 'verbose_name_plural': 'Динамика количества вакансий по годам'},
        ),
        migrations.AlterModelOptions(
            name='salarydynamicsofyear',
            options={'ordering': ['year', 'salary'], 'verbose_name': 'Динамика уровня зарплат по годам', 'verbose_name_plural': 'Динамика уровня зарплат по годам'},
        ),
    ]
