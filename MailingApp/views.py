from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from MailingApp.models import MailRecipient, Message, MailManage


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
    fields = ['recipient', 'message', 'status', 'date_first_send', 'date_last_send']
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
        print(mmail)
        print(mmail.date_first_send)
        print(mmail.date_last_send)
        #


        return redirect('MailingApp:mmail_list')
