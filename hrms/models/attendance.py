from django.db import models
from django.conf import settings 
from django.utils.translation import gettext_lazy as _

class EntranceExitReason(models.Model):
    reason_description = models.CharField(max_length=200, verbose_name='description')

    def __str__(self):
        return self.reason_description

class EntranceExitModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, verbose_name=_('attendee'), related_name='entrance_exit_user')
    reason = models.ForeignKey(EntranceExitReason, on_delete=models.DO_NOTHING, verbose_name=_('Reason'), related_name='entrance_exit_reason')
    approver_user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True, blank=True, default=None, verbose_name=_("Approving person"), related_name='entrance_exit_approver_user')
    start_date = models.DateField(verbose_name=_("Entrance Time"))
    end_date = models.DateField(verbose_name=_("Finish Time"))
    is_approved = models.BooleanField(default=False, verbose_name=_("Approved"))

    def __str__(self):
        return str(self.user.get_full_name()) + " PESEL " + str(self.user.user_profile.pesel) + " powód: " + str(self.reason)