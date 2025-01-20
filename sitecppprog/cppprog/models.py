from django.db import models

# GENERAL MODELS
class SalaryDynamicsOfYear(models.Model):
    year = models.IntegerField("Год")
    salary = models.PositiveIntegerField("Зарплата в рублях")
    def __str__(self):
        return f"{self.year} - {self.salary}"

    class Meta:
        verbose_name = "Динамика уровня зарплат по годам"
        verbose_name_plural = "Динамика уровня зарплат по годам"
        ordering = ['year', 'salary']


class CountDynamicsOfYear(models.Model):
    year = models.IntegerField("Год")
    vacancies_number = models.PositiveIntegerField("Вакансий")

    def __str__(self):
        return f"{self.year} - {self.vacancies_number}"

    class Meta:
        verbose_name = "Динамика количества вакансий по годам"
        verbose_name_plural = "Динамика количества вакансий по годам"
        ordering = ['year', 'vacancies_number']


class SalaryDynamicsOfCity(models.Model):
    city = models.CharField("Город", max_length=255)
    salary = models.PositiveIntegerField("Зарплата в рублях")

    def __str__(self):
        return f"{self.city} - {self.salary}"

    class Meta:
        verbose_name = "Уровень зарплат по городам"
        verbose_name_plural = "Уровень зарплат по городам"
        ordering = ['-salary']


class RateOfCity(models.Model):
    city = models.CharField("Город", max_length=255)
    rate = models.FloatField("Доля")

    def __str__(self):
        return f"{self.city} - {self.rate}"

    class Meta:
        verbose_name = "Доля вакансий по городам"
        verbose_name_plural = "Доля вакансий по городам"
        ordering = ['-rate']


class Top20Skills(models.Model):
    year = models.IntegerField("Год")
    skill = models.CharField("Навык", max_length=255)
    count = models.PositiveIntegerField("Количество")

    def __str__(self):
        return f"{self.year} - {self.skill} - {self. count}"

    class Meta:
        verbose_name = "ТОП-20 навыков по годам"
        verbose_name_plural = "ТОП-20 навыков по годам"
        ordering = ['-year', '-count']


# C++ prog
class VacancySalaryDynamicsOfYear(models.Model):
    year = models.IntegerField("Год")
    salary = models.PositiveIntegerField("Зарплата в рублях")

    def __str__(self):
        return f"{self.year} - {self.salary}"

    class Meta:
        verbose_name = "Динамика уровня зарплат по годам для профессии C++ программист"
        verbose_name_plural = "Динамика уровня зарплат по годам для профессии C++ программист"
        ordering = ['salary']


class VacancyCountDynamicsOfYear(models.Model):
    year = models.IntegerField("Год")
    vacancies_number = models.PositiveIntegerField("Вакансий")

    def __str__(self):
        return f"{self.year} - {self.vacancies_number}"

    class Meta:
        verbose_name = "Динамика количества вакансий по годам для профессии C++ программист"
        verbose_name_plural = "Динамика количества вакансий по годам для профессии C++ программист"
        ordering = ['year', 'vacancies_number']


class VacancySalaryDynamicsOfCity(models.Model):
    city = models.CharField("Город", max_length=255)
    salary = models.PositiveIntegerField("Зарплата в рублях")

    def __str__(self):
        return f"{self.city} - {self.salary}"

    class Meta:
        verbose_name = "Уровень зарплат по городам для профессии C++ программист"
        verbose_name_plural = "Уровень зарплат по городам для профессии C++ программист"
        ordering = ['-salary']


class VacancyRateOfCity(models.Model):
    city = models.CharField("Город", max_length=255)
    rate = models.FloatField("Доля")

    def __str__(self):
        return f"{self.city} - {self.rate}"

    class Meta:
        verbose_name = "Доля вакансий по городам для профессии C++ программист"
        verbose_name_plural = "Доля вакансий по городам для профессии C++ программист"
        ordering = ['-rate']


class VacancyTop20Skills(models.Model):
    year = models.IntegerField("Год")
    skill = models.CharField("Навык", max_length=255)
    count = models.PositiveIntegerField("Количество")

    def __str__(self):
        return f"{self.year} - {self.skill} - {self. count}"

    class Meta:
        verbose_name = "ТОП-20 навыков по годам для профессии C++ программист"
        verbose_name_plural = "ТОП-20 навыков по годам для профессии C++ программист"
        ordering = ['-year', '-count']


# Images Model
class ImagesModel(models.Model):
    name = models.CharField("Название изображения", max_length=255)
    image = models.ImageField()

    def __str__(self):
        return f"{self.name} - {self.image}"

    class Meta:
        verbose_name = "Изображения"
        verbose_name_plural = "Изображения"
        ordering = ['-name']