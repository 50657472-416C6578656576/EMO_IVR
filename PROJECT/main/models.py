from django.db import models
from django.contrib.auth.models import User


class Sportsman(models.Model):
    trainer = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50)
    dob = models.DateField('Дата рождения')
    start_number = models.PositiveIntegerField('Стартовый номер')
    about = models.CharField('Характеристика', default="...", max_length=250)
    rating = models.IntegerField('Рейтинг', default=0)


class Competition(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField('Название', max_length=50)
    description = models.CharField('Краткое описание', max_length=250)
    full_text = models.TextField('Описание', default="...", max_length=5000)
    comp_time = models.DateField('Дата проведения')
    free_access = models.BooleanField('Доступно', default=True)
    preview = models.ImageField('Обложка', upload_to='pictures/', default="pictures/default.jpg")
    participants = models.ManyToManyField(Sportsman, null=True)


class Team(models.Model):
    leader = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    title = models.CharField('Название', max_length=50)
    club = models.CharField('Клуб', max_length=50)