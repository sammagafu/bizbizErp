from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings 

# Create your models here.

class Project(models.Model):
    id_employee = models.ManyToManyField(settings.AUTH_USER_MODEL,  verbose_name=_('Employee'), related_name='project_employee_user')
    id_project_pm = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, verbose_name='Project Manager', related_name='project_pm_user', null=True, blank=True)
    client = models.CharField(max_length=300, verbose_name=_('Client name'))
    name = models.CharField(max_length=200, verbose_name=_('Name'))
    number = models.IntegerField(verbose_name=_('Project number'))
    number_2 = models.IntegerField(verbose_name=_('Project number 2'))
    project_type = models.CharField(max_length=50, verbose_name=_('Project type'))
    status = models.CharField(max_length=50, verbose_name=_('Status'))
    start_date = models.DateField(verbose_name=_('Start date'))
    end_date = models.DateField(verbose_name=_('End date'))
    contact = models.CharField(max_length=500, verbose_name=_('Contact'))
    comments = models.TextField(max_length=500, verbose_name=_('Comments'), null=True, blank=True)

    def __str__(self):
        return self.name+" number: "+ str(self.number) +" number2: " + str(self.number_2) + " project_pm: " + self.id_project_pm.get_full_name()

class ProjectFeedback(models.Model):
    models.ForeignKey(Project, verbose_name=_(""), on_delete=models.CASCADE)
    date = models.DateField(verbose_name=_('Start date'))
    feedback = models.TextField(max_length=500, verbose_name=_('Feedback'), null=True, blank=True)