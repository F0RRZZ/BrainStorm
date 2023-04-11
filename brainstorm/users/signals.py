import allauth.account.signals
import django.db.models.signals
import django.dispatch

import users.models


@django.dispatch.receiver(allauth.account.signals.user_signed_up)
def user_signed_up_(request, user, **kwargs):
    user.is_active = True
    user.save()


@django.dispatch.receiver(
    django.db.models.signals.pre_save, sender=users.models.User
)
def update_normalized_email(sender, instance, **kwargs):
    instance.normalized_email = instance.email.lower()
