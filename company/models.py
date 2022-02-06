from basics.models import AddressMixin, CompanyMixin
from django.db import models

from django.urls import reverse

from user.models import User



class Company(CompanyMixin, AddressMixin):

    user = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name='company',
        blank=True,
        null=True,
    )
    
    def get_absolute_url_edit_company(self):
            return reverse('user:edit_company', args=[self.pk])
    
    class Meta:
        verbose_name_plural = 'Empresas'

    # def get_absolute_company(self):
    #     return reverse('user:edit_company', kwargs={'pk': self.user.pk})
