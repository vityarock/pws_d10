from django.db import models

# Create your models here.
class Car(models.Model):
    AUTO = 1
    ROBOT = 2
    MECHANIC = 3
    VARIATOR = 4
    KPP_CHOICES = [(AUTO, 'Автоматическая'),
                   (ROBOT, 'Роботизированная'),
                   (MECHANIC, 'Механическая'),
                   (VARIATOR, 'Вариатор'),
    ]



    vendor = models.CharField("Марка", max_length=64)
    name = models.CharField("Модель", max_length=64)
    year = models.PositiveIntegerField("Год",)
    transmission = models.SmallIntegerField("КПП", choices=KPP_CHOICES)
    color = models.CharField("Цвет", max_length=64)

    def __str__(self):
        return f'{self.vendor} {self.name} ({self.year})'
