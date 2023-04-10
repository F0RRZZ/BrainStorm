import allauth.account.signals
import django.dispatch


@django.dispatch.receiver(allauth.account.signals.user_signed_up)
def user_signed_up_(request, user, **kwargs):
    user.is_active = True
    user.save()
