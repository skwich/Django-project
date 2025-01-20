from django.db import models

# GENERAL MODELS
class SalaryDynamicsOfYear(models.Model):
    year = models.IntegerField("Год")
    salary = models.PositiveIntegerField("Зарплата в рублях")
    def __str__(self):
        return str(self.year)

    class Meta:
        verbose_name = "Динамика уровня зарплат по годам"
        verbose_name_plural = "Динамика уровня зарплат по годам"


class CountDynamicsOfYear(models.Model):
    year = models.IntegerField("Год")
    vacancies_number = models.PositiveIntegerField("Вакансий")

    def __str__(self):
        return str(self.year)

    class Meta:
        verbose_name = "Динамика количества вакансий по годам"
        verbose_name_plural = "Динамика количества вакансий по годам"


class SalaryDynamicsOfCity(models.Model):
    city = models.CharField("Город", max_length=255)
    salary = models.PositiveIntegerField("Зарплата в рублях")

    def __str__(self):
        return str(self.city)

    class Meta:
        verbose_name = "Уровень зарплат по городам"
        verbose_name_plural = "Уровень зарплат по городам"


class RateOfCity(models.Model):
    city = models.CharField("Город", max_length=255)
    rate = models.FloatField("Доля")

    def __str__(self):
        return str(self.city)

    class Meta:
        verbose_name = "Доля вакансий по городам"
        verbose_name_plural = "Доля вакансий по городам"


class Top20Skills(models.Model):
    year = models.IntegerField("Год")
    skill = models.CharField("Навык", max_length=255)

    def __str__(self):
        return str(self.year)

    class Meta:
        verbose_name = "ТОП-20 навыков по годам"
        verbose_name_plural = "ТОП-20 навыков по годам"


# Images Model
class ImagesModel(models.Model):
    name = models.CharField("Название изображения", max_length=255)
    image = models.ImageField()

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Изображения"
        verbose_name_plural = "Изображения"