# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Company, Conversation, CVData, CVFile, Recruitment, Person, Offer


class CompanyAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated',)


class ConversationAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated',)


class CVDataAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated',)


class CVFileAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated',)


class RecruiterAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated',)


class OfferAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated',)


class DataAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated',)


admin.site.register(Company, CompanyAdmin)
admin.site.register(Conversation, ConversationAdmin)
admin.site.register(CVData, CVDataAdmin)
admin.site.register(CVFile, CVFileAdmin)
admin.site.register(Recruitment, DataAdmin)
admin.site.register(Person, RecruiterAdmin)
admin.site.register(Offer, OfferAdmin)
