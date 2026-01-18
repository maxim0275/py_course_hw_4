from django import forms

from MailingApp.models import MailManage


class MailManageForm(forms.ModelForm):
    class Meta:
        model = MailManage
        fields = ['date_first_send', 'date_last_send', 'status', 'message', 'recipient']

    def __init__(self, *args, **kwargs):
        super(MailManageForm, self).__init__(*args, **kwargs)
        self.fields['date_first_send'].widget.attrs.update({'class': 'form-control'})
        self.fields['date_last_send'].widget.attrs.update({'class': 'form-control'})
        self.fields['status'].widget.attrs.update({'class': 'form-control'})
        self.fields['message'].widget.attrs.update({'class': 'form-control'})

    def clean(self):
        cleaned_data = super().clean()
        # invalid_words = [
        #     'казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар'
        # ]
        date_first_send = cleaned_data.get('date_first_send')
        date_last_send = cleaned_data.get('date_last_send')

        if date_first_send >= date_last_send:
            self.add_error('date_last_send', "Дата окончания рассылки должна быть позже даты начала рассылки")



        return cleaned_data
