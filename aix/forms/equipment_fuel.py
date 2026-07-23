
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
from aix.models import EquipmentFuelModel

class EquipmentFuelForm(ModelForm):
    class Meta:
        model = EquipmentFuelModel
        fields= ['fuel_date', 'equipment', 'start_location', 'end_location', 'start_mileage', 'end_mileage', 'fuel_qty', 'fuel_price', 'fuel_tank', 'kms_covered', 'description',]

        widgets = {
            'fuel_date': DateInput(attrs={
                'type': 'date',
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            'equipment': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            'status': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            'description': Textarea(attrs={
                'class': 'textarea' + ' w-100',
                'rows': 3
            }),
            'start_mileage': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            'end_mileage': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            'fuel_qty': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            'fuel_price': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            'fuel_tank': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            'start_location': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            'end_location': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            }),
            'kms_covered': DateInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' w-100'
            })
        }

    def __init__(self,work_order,*args,**kwargs):
        super(EquipmentFuelForm,self).__init__(*args,**kwargs)
        self.fields['fuel_date'].widget.attrs.update({'min': work_order.start_date, 'max': work_order.end_date}) 
        
    def get_info(self, email=None, equipment_fuel=None):
        """
        Method that returns formatted information
        :return: subject, msg
        """
        # Cleaned data
        cl_data = super().clean()

        fuel = equipment_fuel.code
        from_email = email
        subject = f'NEW EQUIPMENT FUEL CREATED + {fuel} + from aix Portal'
        description = cl_data.get('description')

        cx = {}
        cx['fuel'] = fuel
        cx['from_email'] = from_email
        cx['subject'] = subject
        cx['description'] = description

        msg = f'Created {fuel} with email {from_email}:'
        msg += f'\n"{subject}"\n\n'
        msg += f'You have created a new equipment fuel number #. {fuel} \n\nDescription\n{description} \n\n\nPlease dont reply this email message\naix@Administrator'

        return subject, msg, cx
    
    def send(self, email=None, equipment_fuel=None):
        subject, msg, cx = self.get_info(email, equipment_fuel)
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


class EquipmentFuelAddForm(EquipmentFuelForm):
    class Meta(EquipmentFuelForm.Meta):
        fields = [
            'fuel_date',
            'equipment',
            'start_location', 
            'end_location', 
            'start_mileage',
            'end_mileage',
            'fuel_qty',
            'fuel_price',
            'fuel_tank',
            'kms_covered',
            'description',
            'status'
        ]