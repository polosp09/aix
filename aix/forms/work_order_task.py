
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
from aix.models import WorkOrderTaskModel

class WorkOrderTaskForm(ModelForm):
    class Meta:
        model = WorkOrderTaskModel
        fields= ['startdate', 'enddate', 'startlocation', 'endlocation', 'description', 'currentstatus', 'tripdistance', 'fuel', 'weight',]

        widgets = {
            'startdate': DateInput(attrs={
                'type': 'date',
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            'enddate': DateInput(attrs={
                'type': 'date',
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            'currentstatus': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            'description': Textarea(attrs={
                'class': 'textarea' + ' w-100'
            }),
            'currentstatus': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            'tripdistance': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            'fuel': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            'startlocation': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            'endlocation': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            'statusdate': DateInput(attrs={
                'type': 'date',
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            'currentstatus': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            })
        }

    def __init__(self,work_order,*args,**kwargs):
        super(WorkOrderTaskForm,self).__init__(*args,**kwargs)
        self.fields['startdate'].widget.attrs.update({'min': work_order.start_date, 'max': work_order.end_date})
        self.fields['enddate'].widget.attrs.update({'min': work_order.start_date, 'max': work_order.end_date})
        # self.fields['startdate'].queryset =  work_orders
        # self.fields["enddate"].widget = DateTimeInput()
        # self.fields["enddate"].input_formats = ["%Y-%m-%dT%H:%M", "%Y-%m-%d %H:%M"]

        
        
    def get_info(self, email=None, work_order_task=None):
        """
        Method that returns formatted information
        :return: subject, msg
        """
        # Cleaned data
        cl_data = super().clean()

        task = work_order_task.tripno
        from_email = email
        subject = f'NEW WORK ORDER TASK CREATED + {task} + from aix Portal'
        description = cl_data.get('description')

        cx = {}
        cx['task'] = task
        cx['from_email'] = from_email
        cx['subject'] = subject
        cx['description'] = description

        msg = f'Created {task} with email {from_email}:'
        msg += f'\n"{subject}"\n\n'
        msg += f'You have created a new work order task number #. {task} \n\nDescription\n{description} \n\n\nPlease dont reply this email message\naix@Administrator'

        return subject, msg, cx
    
    def send(self, email=None, work_order_task=None):
        subject, msg, cx = self.get_info(email, work_order_task)
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


class WorkOrderTaskAddForm(WorkOrderTaskForm):
    class Meta(WorkOrderTaskForm.Meta):
        fields = [
            'startdate',
            'enddate',
            'startlocation', 
            'endlocation', 
            'description',
            'tripdistance',
            'fuel',
            'weight',
            'currentstatus'
        ]