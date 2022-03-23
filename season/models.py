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
