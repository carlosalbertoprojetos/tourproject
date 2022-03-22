from django.db import models


class Season(models.Model):
    
    YEARS_CHOICES = (
        ('2022', '2022'),
        ('2023', '2023'),
        ('2024', '2024'),
        ('2025', '2025'),
        ('2026', '2026'),
        ('2027', '2027'),
        ('2028', '2028'),
        ('2029', '2029'),
        ('2030', '2030'),
    )

    name = models.CharField('Temporada', max_length=255)
    year = models.CharField('Ano', choices=YEARS_CHOICES, max_length=4)

    class Meta:
        verbose_name = 'Temporada'
        verbose_name_plural = 'Temporadas'

    def __str__(self):
        return self.name + ' Temporada /' + self.year


class PeriodSeasons(models.Model):

    description = models.CharField('Descrição', max_length=150)
    season = models.ForeignKey(Season, on_delete=models.DO_NOTHING)
    date_start = models.DateField('Data Inicial')
    date_end = models.DateField('Data Final')

    class Meta:
        ordering = ['-date_start']
        verbose_name = 'Descrição Temporada'
        verbose_name_plural = 'Descrição Temporadas'

    def __str__(self):
        return self.description + ' / ' + str(self.date_start) + ' a ' + str(self.date_end)
