from django.db import models


class Women(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок') #CharField для вставления текста с указанием макс кол символов например 255
    content = models.TextField(blank=True, verbose_name='Текст статьи') #TextField
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания') # устанавливает время. не меняет время
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения') # устанавливает время. может менять время
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

