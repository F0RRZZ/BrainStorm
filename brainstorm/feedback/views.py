import os

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.views.generic.base import TemplateView

import feedback.forms
import feedback.models


class FeedbackFormView(FormView):
    model = feedback.models.Feedback
    form_class = feedback.forms.FeedbackForm
    template_name = 'feedback/feedback.html'
    success_url = reverse_lazy('feedback:success')

    def form_valid(self, form):
        text = form.cleaned_data.get('text')
        email = form.cleaned_data.get('email')
        personal_data = feedback.models.PersonalData(email=email)
        personal_data.save()
        new_feedback = feedback.models.Feedback(
            text=text, personal_data=personal_data
        )
        new_feedback.save()
        if self.request.FILES.getlist('files'):
            feedback_dir = os.path.join('uploads', str(new_feedback.id))
            os.makedirs(feedback_dir)
            for file in self.request.FILES.getlist('files'):
                file_system = FileSystemStorage(location=feedback_dir)
                filename = file_system.save(file.name, file)
                feedback_file = feedback.models.FeedbackFile(
                    feedback=new_feedback,
                    file=filename,
                )
                feedback_file.save()
        send_mail(
            'Subject',
            text,
            settings.EMAIL,
            [email],
            fail_silently=False,
        )
        return super().form_valid(form)


class SuccessPageView(TemplateView):
    template_name = 'feedback/success.html'
