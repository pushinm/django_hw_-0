from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=50)
    main_body = models.TextField(verbose_name='Статья')

    def __str__(self) -> str:
        return f'{self.title}'

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('magazine:article_view', kwargs={'pk': self.pk})