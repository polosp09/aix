
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail
from django.forms import (ModelForm, DateInput, TextInput, Select,
                          CheckboxInput, BaseModelFormSet,
                          modelformset_factory, Textarea)
from django.forms import ValidationError
from django.template.loader import render_to_string
from django.utils.translation import gettext_lazy as _
from aix.settings import MANDO_FORM_INPUT_CLASSES
from aix.models import WorkOrderModel
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class WorkOrderForm(ModelForm):
    class Meta:
        model = WorkOrderModel
        fields= ['start_date', 'end_date', 'clientref', 'wo_type', 'category', 'service_type', 'currency', 'remarks', 'description',]

        widgets = {
            'order_no': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' is-large'
            }),
            'remarks': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'clientref': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'start_date': DateInput(attrs={
                'type': 'date',
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'end_date': DateInput(attrs={
                'type': 'date',
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'status': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'description': Textarea(attrs={
                'class': 'textarea' + MANDO_FORM_INPUT_CLASSES
            }),
            'clientref': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'currency': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'wo_type': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'customer': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'category': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            'status': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            'is_active': CheckboxInput(attrs={'type': 'checkbox'})
        }

    def __init__(self,*args,**kwargs):
        super(WorkOrderForm,self).__init__(*args,**kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('start_date', css_class='form-group col-md-6 mb-2'),
                Column('end_date', css_class='form-group col-md-6 mb-2'),
                css_class='form-row'
            ),
            # 'customer',
            'clientref',
            Row(
                Column('work_type', css_class='form-group col-md-6 mb-2'),
                Column('category', css_class='form-group col-md-4 mb-2'),
                Column('currency', css_class='form-group col-md-2 mb-2'),
                css_class='form-row'
            ),
            'status',
            Submit('submit', 'Save')
        )
    
    def get_info(self, email=None, work_order=None):
        """
        Method that returns formatted information
        :return: subject, msg
        """
        # Cleaned data
        cl_data = super().clean()

        wo = work_order.order_no
        from_email = email
        subject = f'NEW WORK ORDER CREATED + {wo} + from aix Portal'
        description = cl_data.get('description')

        cx = {}
        cx['wo'] = wo
        cx['from_email'] = from_email
        cx['subject'] = subject
        cx['description'] = description

        msg = f'Created {wo} with email {from_email}:'
        msg += f'\n"{subject}"\n\n'
        msg += f'You have created a new work order number #. {wo} \n\nDescription\n{description} \n\n\nPlease dont reply this email message\naix@Administrator'

        return subject, msg, cx
    
    def send(self, email=None, work_order=None):
        subject, msg, cx = self.get_info(email, work_order)
        # print(settings.EMAIL_HOST_USER)
        # msg_plain = render_to_string('templates/email.txt', {'some_params': some_params})
        # msg_html = render_to_string('templates/email.html', {'some_params': some_params})
        msg_html = render_to_string('aix/email/wo_new.html', cx)
        # print(msg_html)
        # msg_html = msg
        send_mail(
            subject=subject,
            message=msg,
            # html_message=msg_html,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.RECIPIENT_ADDRESS]
        )
        # to = [email,]
        # xmsg = EmailMultiAlternatives(subject, msg, cx['from_email'], to)
        # xmsg.attach_alternative(msg_html, "text/html")
        # xmsg.send()