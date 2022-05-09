from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings 

# Create your models here.
class HolidayModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, verbose_name=_('Employee'), related_name='holiday_user')
    approver_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING,  null=True, blank=True, default=None, verbose_name='Approving person', related_name='holiday_approver_user')
    start_date = models.DateField(verbose_name=_('Start date'))
    end_date = models.DateField(verbose_name=_('End Date'))
    is_used = models.BooleanField(default=False, verbose_name=_('Is completed'))
    is_approved = models.BooleanField(default=False, verbose_name=_('Is approved'))

    def __str__(self):
        return "Free: " + self.user.get_full_name() + " PESEL: " + self.user.user_profile.pesel + "  From: " + str(self.start_date) + " TO: " + str(self.end_date)
