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
from aix.models import WorkOrderActivityModel

class WorkOrderActivityForm(ModelForm):
    class Meta:
        model = WorkOrderActivityModel
        fields= ['activity_date',
            'activity_description',
            'work_code',
            'from_location',
            'to_location',
            'etd',
            'eta',
            'atd',
            'ata',
            'comments',
            'status', ]

        widgets = {
            'activity_date': DateInput(attrs={
                'type': 'date',
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            'activity_description': Textarea(attrs={
                'class': 'textarea'
            }),
            'reason': Textarea(attrs={
                'class': 'textarea' + ' w-100'
            }),
            'comments': Textarea(attrs={
                'class': 'textarea' + ' w-100'
            }),
            'etd': DateInput(attrs={
                'type': 'time',
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            'eta': DateInput(attrs={
                'type': 'time',
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            'atd': DateInput(attrs={
                'type': 'time',
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            'ata': DateInput(attrs={
                'type': 'time',
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            'status': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            'trip_activity': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            'work_code': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            'from_location': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            'to_location': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            'activity_time': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            'kms_passed': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            'consol_fuel': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            'operator': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            'banksman': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            'rigger1': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            'rigger2': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            'rigger3': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            'rigger4': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            'section2_description': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            'section2_time_taken': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            'section2_ton_cargo': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            'section2_number_lifts': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            'section2_ton_lifts': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            'no_routine': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            'no_simple': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            'no_complicated': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            'no_complex': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            'ton_routine': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            'ton_simple': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            'ton_complicated': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            'section3_description': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            'section3_time_taken': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            'section3_ton_cargo': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            'section3_number_lifts': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            'section3_ton_lifts': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            'llt_dsb': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            'llt_tgi': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            'llt_rig1': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            'llt_rig2': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            'llt_rig3': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            'llt_other': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            
            'tlt_dsb': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            'tlt_tgi': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            'tlt_rig1': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            'tlt_rig2': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            'tlt_rig3': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            'tlt_other': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            'dnt_dsb': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            'dnt_tgi': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            'dnt_rig1': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            'dnt_rig2': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            'dnt_rig3': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            'dnt_other': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
        }

    def __init__(self,wo_task,*args,**kwargs):
        super(WorkOrderActivityForm,self).__init__(*args,**kwargs)
        self.fields['activity_date'].widget.attrs.update({'min': wo_task.startdate, 'max': wo_task.enddate})
    
    def configure(self, entity_slug: str or EntityModel, user_model,):
        self.code = generate_code()
        return self
    
    def get_info(self, email=None, activity=None):
        """
        Method that returns formatted information
        :return: subject, msg
        """
        # Cleaned data
        cl_data = super().clean()

        from_email = email
        subject = f'NEW TASK ACTIVITY CREATED + {activity.code} + from aix Portal'
        description = cl_data.get('activity_description')

        cx = {}
        cx['activity'] = activity
        cx['from_email'] = from_email
        cx['subject'] = subject
        cx['activity_description'] = description

        msg = f'Created {activity} with email {from_email}:'
        msg += f'\n"{subject}"\n\n'
        msg += f'You have created a new task activity number #. {activity.code} \n\nDescription\n{description} \n\n\nPlease dont reply this email message\naix@Administrator'

        return subject, msg, cx
    
    def send(self, email=None, activity=None):
        subject, msg, cx = self.get_info(email, activity)
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


class WorkOrderActivityAddForm(WorkOrderActivityForm):
    class Meta(WorkOrderActivityForm.Meta):
        fields = [
            'activity_date',
            'activity_description',
            'work_code',
            'from_location',
            'to_location',
            'etd',
            'eta',
            'atd',
            'ata',
            'status',
        ]