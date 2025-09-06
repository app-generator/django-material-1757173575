# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Venture(models.Model):

    #__Venture_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    resumed_name = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    resumed_description = models.CharField(max_length=255, null=True, blank=True)
    pictures = models.CharField(max_length=255, null=True, blank=True)
    default_picture = models.IntegerField(null=True, blank=True)
    address = models.ForeignKey(address, on_delete=models.CASCADE)
    logo = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)

    #__Venture_FIELDS__END

    class Meta:
        verbose_name        = _("Venture")
        verbose_name_plural = _("Venture")


class Address(models.Model):

    #__Address_FIELDS__
    streeet = models.CharField(max_length=255, null=True, blank=True)
    number = models.CharField(max_length=255, null=True, blank=True)
    zip = models.IntegerField(null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    other_info = models.CharField(max_length=255, null=True, blank=True)
    coordinates = models.CharField(max_length=255, null=True, blank=True)

    #__Address_FIELDS__END

    class Meta:
        verbose_name        = _("Address")
        verbose_name_plural = _("Address")



#__MODELS__END
