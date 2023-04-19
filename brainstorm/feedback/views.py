import os

import django.conf
import django.core.files.storage
import django.core.mail
import django.urls
import django.views.generic
import django.views.generic.base

import feedback.forms
import feedback.models


class FeedbackFormView(django.views.generic.FormView):
    model = feedback.models.Feedback
    form_class = feedback.forms.FeedbackForm
    template_name = 'feedback/feedback.html'
    success_url = django.urls.reverse_lazy('feedback:success')

    def form_valid(self, form):
        subject = form.cleaned_data.get('subject')
        text = form.cleaned_data.get('text')
        email = form.cleaned_data.get('email')
        new_feedback = feedback.models.Feedback(
            subject=subject,
            text=text,
        )
        new_feedback.save()
        personal_data = feedback.models.PersonalData(
            email=email,
            feedback=new_feedback,
        )
        personal_data.save()
        if self.request.FILES.getlist('files'):
            feedback_dir = os.path.join('uploads', str(new_feedback.id))
            os.makedirs(feedback_dir)
            for file in self.request.FILES.getlist('files'):
                file_system = django.core.files.storage.FileSystemStorage(
                    location=feedback_dir
                )
                filename = file_system.save(file.name, file)
                feedback_file = feedback.models.FeedbackFile(
                    feedback=new_feedback,
                    file=filename,
                )
                feedback_file.save()
        django.core.mail.send_mail(
            subject,
            text + f'\nАвтор: {email}',
            django.conf.settings.EMAIL,
            [django.conf.settings.EMAIL],
            fail_silently=False,
        )
        return super().form_valid(form)


class SuccessPageView(django.views.generic.base.TemplateView):
    template_name = 'feedback/success.html'
