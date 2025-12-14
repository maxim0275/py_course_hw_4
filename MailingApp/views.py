from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from MailingApp.models import MailRecipient, Message


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


# ===============================================================
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
