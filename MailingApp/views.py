import datetime

from django.core.mail import send_mail
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, TemplateView

from MailingApp.forms import MailManageForm
from MailingApp.models import MailRecipient, Message, MailManage, MailAtt


class MainPageView(TemplateView):
    template_name = 'MailingApp/main_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["mail_manage_count"] = MailManage.objects.all().count()
        context["recipient_count"] = MailRecipient.objects.all().count()

        active_mmail = MailManage.objects.filter(date_first_send__lte= datetime.datetime.today().date())
        active_mmail = active_mmail.filter(date_last_send__gte=datetime.datetime.today().date())
        active_mmail = active_mmail.filter(status="STARTED")
        context["active_mail_manage_count"] = active_mmail.count()

        return context


# ============================ MailRecipient ===================================
class MailRecipientListView(ListView):
    model = MailRecipient
    template_name = 'MailingApp/recipient_list.html'
    context_object_name = 'recipient'


class MailRecipientCreateView(CreateView):
    model = MailRecipient
    fields = ['email', 'full_name', 'comment']
    template_name = 'MailingApp/recipient_form.html'
    context_object_name = 'recipient'
    success_url = reverse_lazy('MailingApp:recipient_list')


class MailRecipientDetailView(DetailView):
    model = MailRecipient
    template_name = 'MailingApp/recipient_detail.html'
    context_object_name = 'recipient'


class MailRecipientUpdateView(UpdateView):
    model = MailRecipient
    fields = ['email', 'full_name', 'comment']
    template_name = 'MailingApp/recipient_form.html'
    success_url = reverse_lazy('MailingApp:recipient_list')


class MailRecipientDeleteView(DeleteView):
    model = MailRecipient
    template_name = 'MailingApp/recipient_confirm_delete.html'
    context_object_name = 'recipient'
    success_url = reverse_lazy('MailingApp:recipient_list')


# ============================ Message ===================================
class MessageListView(ListView):
    model = Message
    template_name = 'MailingApp/message_list.html'
    context_object_name = 'messages'


class MessageCreateView(CreateView):
    model = Message
    fields = ['topic', 'body']
    template_name = 'MailingApp/message_form.html'
    context_object_name = 'message'
    success_url = reverse_lazy('MailingApp:message_list')


class MessageDetailView(DetailView):
    model = Message
    template_name = 'MailingApp/message_detail.html'
    context_object_name = 'message'


class MessageUpdateView(UpdateView):
    model = Message
    fields = ['topic', 'body']
    template_name = 'MailingApp/message_form.html'
    success_url = reverse_lazy('MailingApp:message_list')


class MessageDeleteView(DeleteView):
    model = Message
    template_name = 'MailingApp/message_confirm_delete.html'
    success_url = reverse_lazy('MailingApp:message_list')


# ======================= MailManage ==========================================
class MailManageListView(ListView):
    model = MailManage
    template_name = 'MailingApp/mmail_list.html'
    context_object_name = 'mmails'


class MailManageCreateView(CreateView):
    model = MailManage
    fields = ['recipient', 'message', 'status', 'date_first_send', 'date_last_send']
    template_name = 'MailingApp/mmail_form.html'
    context_object_name = 'mmail'
    success_url = reverse_lazy('MailingApp:mmail_list')


class MailManageDetailView(DetailView):
    model = MailManage
    template_name = 'MailingApp/mmail_detail.html'
    context_object_name = 'mmail'


class MailManageUpdateView(UpdateView):
    model = MailManage
    form_class = MailManageForm
    # fields = ['recipient', 'message', 'status', 'date_first_send', 'date_last_send']
    template_name = 'MailingApp/mmail_form.html'
    success_url = reverse_lazy('MailingApp:mmail_list')


class MailManageDeleteView(DeleteView):
    model = MailManage
    template_name = 'MailingApp/mmail_confirm_delete.html'
    success_url = reverse_lazy('MailingApp:mmail_list')

    # def form_valid(self, form):
    #     # Очистите связи ManyToMany перед удалением объекта
    #     print("Before clear:", self.object.recipient.all())
    #     self.object.recipient.clear()
    #     print("After clear:", self.object.recipient.all())
    #
    #     # Продолжайте удаление объекта
    #     return super().form_valid(form)


class MailManageTODOView(View):

    def post(self, request, mailmanage_id):
        # Если время рассылки находится между start_time и end_time, то отправка разрешена, иначе выводится сообщение об ошибке

        # Получить объект рассылки
        mmail = get_object_or_404(MailManage, id=mailmanage_id)

        if mmail.date_first_send < datetime.datetime.today().date() < mmail.date_last_send:
            # Выполнить рассылку
            for client in mmail.recipient.all():
                print(client)
                result_sendmail = send_mail(mmail.message.topic, mmail.message.body, 'your_email@email.com',
                                            [client.email], fail_silently=True)
                # Записать информацию о попытке
                mail_send_attempt = MailAtt()
                if result_sendmail:
                    # успех
                    result = "SUCC"
                else:
                    # не успех
                    result = "FAIL"
                mail_send_attempt.date_time_att = datetime.datetime.today().date()
                mail_send_attempt.status = result
                mail_send_attempt.server_answer = result_sendmail
                mail_send_attempt.mailing = mmail
                mail_send_attempt.save()
        else:
            return HttpResponseForbidden("Период рассылки не разрешен!")

        return redirect('MailingApp:mmail_list')
