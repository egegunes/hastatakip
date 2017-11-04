from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class Randevu(models.Model):
    STATE_OPEN = 1
    STATE_CANCELLED = 2
    STATES = (
        (STATE_OPEN, _('Açık')),
        (STATE_CANCELLED, _('İptal'))
    )

    hasta = models.CharField(_('Hasta'), max_length=64)
    date = models.DateField(_('Tarih'))
    time = models.TimeField(_('Saat'))
    person_number = models.IntegerField(_('Kişi sayısı'))
    contact_phone = models.CharField(_('İrtibat No'), max_length=13)
    state = models.SmallIntegerField(choices=STATES, default=STATE_OPEN)

    def __str__(self):
        return '{} {} - {} - {} kişi'.format(self.date, self.time, self.hasta, self.person_number)

    def get_absolute_url(self):
        return reverse('randevu:detail', kwargs={'pk': self.pk})
