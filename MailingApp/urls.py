from django.urls import path
from . import views

app_name = 'MailingApp'

urlpatterns = [
    path('recipient/list/', views.MailRecipientListView.as_view(), name='recipient_list'),
    path('recipient/create/', views.MailRecipientCreateView.as_view(), name='recipient_create'),
    path('recipient/detail/<int:pk>/', views.MailRecipientDetailView.as_view(), name='recipient_detail'),
    path('recipient/update/<int:pk>/', views.MailRecipientUpdateView.as_view(), name='recipient_update'),
    path('recipient/delete/<int:pk>/', views.MailRecipientDeleteView.as_view(), name='recipient_delete'),
    path('message/list/', views.MessageListView.as_view(), name='message_list'),
    path('message/create/', views.MessageCreateView.as_view(), name='message_create'),
    path('message/detail/<int:pk>/', views.MessageDetailView.as_view(), name='message_detail'),
    path('message/update/<int:pk>/', views.MessageUpdateView.as_view(), name='message_update'),
    path('message/delete/<int:pk>/', views.MessageDeleteView.as_view(), name='message_delete')

]
