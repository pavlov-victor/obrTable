from django.db import models


class Script(models.Model):
    name = models.TextField('Название')
    answer = models.TextField('Ответ')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Скрипт"
        verbose_name_plural = "Скрипт"


class Source(models.Model):
    name = models.TextField('Источник')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Источник"
        verbose_name_plural = 'Источники'


class Location(models.Model):
    name = models.TextField('Местоположение')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = 'Локации'


class Question(models.Model):
    created = models.DateTimeField('Дата создания обращения', auto_now_add=True)
    source = models.ForeignKey(Source, models.SET_NULL, related_name='questions', null=True, blank=False,
                               verbose_name='Источник вопроса')
    fio = models.TextField(verbose_name='ФИО')
    birth_date = models.DateField(verbose_name='Дата рождения')
    location = models.ForeignKey(Location, models.SET_NULL, null=True, related_name='queestions',
                                 verbose_name='Местоположение')
    phone = models.IntegerField('Номер телефона', help_text='Только цифры с 8')
    question = models.TextField('Вопрос')
    script = models.ForeignKey(Script, models.SET_NULL, null=True, verbose_name='Скрипт')
    status = models.CharField(max_length=255, choices=(
        ['НОВОЕ', 'НОВОЕ'],
        # ['ОБРАБОТАНО', 'ОБРАБОТАНО'],
        ['В ОБРАБОТКЕ', 'В ОБРАБОТКЕ'],
        # ['ВАЖНОЕ', 'ВАЖНОЕ'],
        # ['СООБЩЕННО', 'СООБЩЕННО'],
        # ['ОТКЛОНЕНО', 'ОТКЛОНЕНО'],
        ["ЗАВЕРШЕНО", "ЗАВЕРШЕНО"]
    ), default='НОВОЕ', verbose_name='Статус')

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
