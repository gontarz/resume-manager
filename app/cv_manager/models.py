# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import gettext_lazy as _


class TimestampedModel(models.Model):
    created = models.DateTimeField(
        auto_now_add=True
    )
    updated = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        abstract = True


class Person(TimestampedModel):
    class Role(models.IntegerChoices):
        RECRUITER = 1, _('recruiter')
        CONSULTANT = 2, _('consultant')
        CHIEF = 3, _('chief')
        HEADHUNTER = 4, _('hed hunter')
        USER = 5, _('user')
        OTHER = 6, _('other')

    role = models.IntegerField(
        choices=Role.choices
    )
    name = models.TextField(
        null=True,
        blank=True
    )
    surname = models.TextField(
        null=True,
        blank=True
    )
    email = models.EmailField(
        null=True,
        blank=True
    )
    # todo: add phone validator
    phone = models.TextField(
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.name} {self.surname} {self.Role._value2label_map_.get(self.role)}'


class Company(TimestampedModel):
    name = models.TextField(
        null=True,
        blank=True
    )
    address = models.TextField(
        null=True,
        blank=True
    )
    # todo: add phone validator
    phone = models.TextField(
        null=True,
        blank=True
    )
    email = models.EmailField(
        null=True,
        blank=True
    )
    description = models.TextField(
        null=True,
        blank=True
    )

    employees = models.ManyToManyField(
        to=Person,
        blank=True
    )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['name']


class Conversation(TimestampedModel):
    class Type(models.IntegerChoices):
        MAIL = 1, _('email')
        MESSAGE = 2, _('message')
        PHONE = 3, _('phone call')
        VIDEO = 4, _('video call')
        MEETING = 5, _('meeting')
        OTHER = 6, _('other')

    type = models.IntegerField(
        choices=Type.choices
    )
    content = models.TextField(
        null=True,
        blank=True
    )
    additional = models.TextField(
        null=True,
        blank=True
    )
    sent = models.DateTimeField(
        null=True,
        blank=True
    )
    sender = models.ForeignKey(
        to=Person,
        related_name='sender',
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )
    receiver = models.ForeignKey(
        to=Person,
        related_name='reciver',
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.Type._value2label_map_.get(self.type)} {if_exists(self.sender)} {if_exists(self.receiver)} {self.updated}'


class CVFile(TimestampedModel):
    class DataType(models.IntegerChoices):
        CURRICULUM_VITAE = 1, _('curriculum vitae')
        MOTIVATION_LETTER = 2, _('motivation letter')
        ATTACHMENT = 3, _('attachment')

    type = models.IntegerField(
        choices=DataType.choices
    )
    file = models.FileField(
        upload_to='cv'
    )

    def __str__(self):
        return f'{self.DataType._value2label_map_.get(self.type)} {str(self.updated)}'

    class Meta:
        ordering = ['updated']


class CVData(TimestampedModel):
    additional_info = models.TextField(
        null=True,
        blank=True
    )
    files = models.ManyToManyField(
        to=CVFile,
        blank=True
    )

    def __str__(self):
        return f'{str(self.updated)}'


class Offer(TimestampedModel):
    link = models.TextField(
        null=True,
        blank=True
    )
    content = models.TextField(
        null=True,
        blank=True
    )
    additional = models.TextField(
        null=True,
        blank=True
    )
    published = models.DateTimeField(
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.link} {str(self.updated)}'


class Recruitment(TimestampedModel):
    company = models.ForeignKey(
        to=Company,
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )
    recruiter = models.ForeignKey(
        to=Person,
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )
    cv_data = models.ForeignKey(
        to=CVData,
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )
    offer = models.ForeignKey(
        to=Offer,
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )
    conversation = models.ManyToManyField(
        to=Conversation,
        blank=True
    )
    sent = models.DateTimeField(
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{if_exists(self.company)} {if_exists(self.recruiter)} {str(self.updated)}'


def if_exists(obj):
    return obj if obj else ''
