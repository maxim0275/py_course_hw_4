from django.urls import path
from . import views

app_name = 'MailingApp'

urlpatterns = [
    path('', views.MainPageView.as_view(), name='main_page'),

    path('recipient/list/', views.MailRecipientListView.as_view(), name='recipient_list'),
    path('recipient/create/', views.MailRecipientCreateView.as_view(), name='recipient_create'),
    path('recipient/detail/<int:pk>/', views.MailRecipientDetailView.as_view(), name='recipient_detail'),
    path('recipient/update/<int:pk>/', views.MailRecipientUpdateView.as_view(), name='recipient_update'),
    path('recipient/delete/<int:pk>/', views.MailRecipientDeleteView.as_view(), name='recipient_delete'),

    path('message/list/', views.MessageListView.as_view(), name='message_list'),
    path('message/create/', views.MessageCreateView.as_view(), name='message_create'),
    path('message/detail/<int:pk>/', views.MessageDetailView.as_view(), name='message_detail'),
    path('message/update/<int:pk>/', views.MessageUpdateView.as_view(), name='message_update'),
    path('message/delete/<int:pk>/', views.MessageDeleteView.as_view(), name='message_delete'),

    path('mmail/list/', views.MailManageListView.as_view(), name='mmail_list'),
    path('mmail/create/', views.MailManageCreateView.as_view(), name='mmail_create'),
    path('mmail/detail/<int:pk>/', views.MailManageDetailView.as_view(), name='mmail_detail'),
    path('mmail/update/<int:pk>/', views.MailManageUpdateView.as_view(), name='mmail_update'),
    path('mmail/delete/<int:pk>/', views.MailManageDeleteView.as_view(), name='mmail_delete'),
    path('mmail/<int:mailmanage_id>/todo/', views.MailManageTODOView.as_view(), name='mmail_todo')

]
