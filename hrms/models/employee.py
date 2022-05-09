from django.db import models
from django.conf import settings 
from django.utils.translation import gettext_lazy as _


# Create your models here.

#create your own user class.

class UserStateModel(models.Model):
    state_description = models.CharField(max_length=50, verbose_name=_('User Status'))

    def __str__(self):
            return self.state_description

class WorkHoursModel(models.Model):
    description = models.CharField(max_length=200, verbose_name=_('Change description'))
    rate_of_pay = models.DecimalField(verbose_name=_("Wage rate"), default=1.00, max_digits=3, decimal_places=2)

    def __str__(self):
            return self.description

class UserProfileInfo(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("User"), related_name='user_profile')
    user_manager = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name=_("Manager"), related_name='user_manager')
    user_work_hours = models.ForeignKey(WorkHoursModel, null=True, blank=False, on_delete=models.DO_NOTHING, verbose_name='Godziny pracy', related_name='user_work_hours')
    user_state = models.ForeignKey(UserStateModel, null=True, blank=False, on_delete=models.DO_NOTHING, verbose_name='Stan użytkownika', related_name='user_state')
    pesel = models.CharField(max_length=11, verbose_name='PESEL')
    street = models.CharField(max_length=200, verbose_name=_('street'))
    city = models.CharField(max_length=200, verbose_name=_("City"))
    phone = models.CharField(max_length=20, verbose_name=_('Telephone'))
    post_code = models.CharField(max_length=6, verbose_name=_("Post Code"))
    house_number = models.CharField(max_length=20, verbose_name=_("House Number"))
    image = models.ImageField(upload_to='avatars/', default=None, null=True, blank=True)

    def __str__(self):
        return str(self.user.id) +', ' + self.user.get_full_name() + ',  PESEL: ' + self.pesel

class UserAccessModel(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, verbose_name=_("User"), related_name='user_access')
    rfid = models.CharField(max_length=200, verbose_name='rfid')
    comments = models.CharField(max_length=500, verbose_name=_("Comment"), null=True, blank=True)

    def __str__(self):
            return self.user.get_full_name() + ',  PESEL: ' + self.pesel


