from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView, DetailView

from aix.forms.employee import EmployeeForm
from aix.forms.employee_assignment import EmployeeAssignmentAddForm
from aix.forms.employee_contract import EmployeeContractAddForm
from aix.forms.employee_language import EmployeeLanguageAddForm
from aix.forms.employee_license_detail import EmployeeLicenseDetailAddForm
from aix.forms.employee_payroll import EmployeePayrollAddForm
from aix.forms.leave_card import LeaveCardForm, LeaveCardAddForm
from aix.models.entity import EntityModel
from aix.models.employee import EmployeeModel
from aix.models.employee_contract import EmployeeContractModel
from aix.models.employee_language import EmployeeLanguageModel
from aix.models.employee_license_detail import EmployeeLicenseDetailModel
from aix.models.employee_payroll import EmployeePayrollModel
from aix.models.employee_assignment import EmployeeAssignmentModel
from aix.models.leave_card import LeaveCardModel
from aix.views.mixins import LoginRequiredMixIn
from datetime import datetime
import csv
from itertools import islice
from django.db import migrations

BATCH_SIZE = 1000


class EmployeeModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/employees/employee.html'
    context_object_name = 'employees'
    PAGE_TITLE = _('Employee List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return EmployeeModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class EmployeeModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/employees/employee.html'
    PAGE_TITLE = _('Create New Employee')
    form_class = EmployeeForm
    context_object_name = 'employee'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return EmployeeForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:employee-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        employee_model: EmployeeModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        employee_model.entity = entity_model
        employee_model.save()
        return super().form_valid(form)


class EmployeeModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/employees/employee.html'
    PAGE_TITLE = _('Employee Update')
    context_object_name = 'employee'
    form_class = EmployeeForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'employee_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return EmployeeModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:employee-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 


class EmployeeModelDetailView(LoginRequiredMixIn, DetailView):
    slug_url_kwarg = 'employee_pk'
    slug_field = 'uuid'
    context_object_name = 'employee'
    template_name = 'aix/app/employees/details/employee_details.html'
    extra_context = {
        'hide_menu': True
    }

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        employee_model: EmployeeModel = self.object
        title = f'Employee {employee_model.name}'
        context['page_title'] = title
        context['header_title'] = title

        contract_qs = EmployeeContractModel.objects.for_employee(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
                employee=employee_model
            ).select_related('employee__entity')
        language_qs = EmployeeLanguageModel.objects.for_employee(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
                employee=employee_model
            ).select_related('employee__entity')
        license_qs = EmployeeLicenseDetailModel.objects.for_employee(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
                employee=employee_model
            ).select_related('employee__entity')
        payroll_qs = EmployeePayrollModel.objects.for_employee(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
                employee=employee_model
            ).select_related('employee__entity')
        assignment_qs = EmployeeAssignmentModel.objects.for_employee(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
                employee=employee_model
            ).select_related('employee__entity')
        leave_card_qs = LeaveCardModel.objects.for_employee(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
                employee=employee_model
            ).select_related('employee__entity')
        context['contract_qs'] = contract_qs
        context['language_qs'] = language_qs
        context['license_qs'] = license_qs
        context['assignment_qs'] = assignment_qs
        context['leave_card_qs'] = leave_card_qs
        context['payroll_qs'] = payroll_qs

        employee_forms = {}
        employee_forms['add_assignment'] = EmployeeAssignmentAddForm
        employee_forms['add_leave_card'] = LeaveCardAddForm
        employee_forms['add_contract'] = EmployeeContractAddForm
        employee_forms['add_license'] = EmployeeLicenseDetailAddForm
        employee_forms['add_language'] = EmployeeLanguageAddForm
        employee_forms['add_payroll'] = EmployeePayrollAddForm
        context['employee_forms'] = employee_forms
        
        return context

    def get_queryset(self):
        return EmployeeModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')



class EmployeeModelPullView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/employees/employee.html'
    PAGE_TITLE = _('Create New Employee')
    form_class = EmployeeForm
    context_object_name = 'employee'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    entity_id = None
    department_id = None
    user_id = None

    def get(self, request, *args, **kwargs):
        response = super(EmployeeModelPullView, self).get(request, *args, **kwargs)
        context = self.get_context_data()
        entity_qs = EntityModel.objects.all()
        # entity_model: EntityModel = get_object_or_404(entity_qs, slug__exact=self.kwargs['entity_slug'])
        # entity_model = EntityModel.objects.for_user(
        #     user_model=self.request.user
        # ).get(slug__exact=self.kwargs['entity_slug'])
        entity_model: EntityModel = get_object_or_404(entity_qs, slug__exact=self.kwargs['entity_slug'])
        self.entity_id = entity_model.uuid
        self.department_id = '53793f4b57f74bf3ba363001fb2c7062'
        self.user_id = self.request.user.id
        self.import_staff_records()
        return response

    def read_csv_file(self, file_path: str, batch_size: int):
        with open(file_path, "r") as f:
            reader = csv.reader(f)
            while True:
                batch = list(islice(reader, batch_size))

                if not batch:
                    return

                yield batch


    def import_staff_records(self):
        x = 0
        for batch in self.read_csv_file("staffs.csv", BATCH_SIZE):
            qs = []
            for fld in batch:
                if x >= 1:
                    # m = datetime.date(fld[17])
                    # md = m.strftime("%d-%b-%y")
                    # # print(md)
                    # mx = fld[17]
                    # # print(mx)
                    # # m = datetime.date(f'{mx}')
                    # md = datetime.strptime(mx, "%Y-%m-%d")
                    # print(datetime.strptime(fld[17], "%Y-%m-%d"))
                    employee = EmployeeModel(
                            entity_id=self.entity_id,
                            department_id=self.department_id,
                            # user_id=self.user_id,
                            idnumber=fld[1],
                            name=fld[2],
                            designation=fld[3],
                            nationality=fld[4],
                            gender=fld[5],
                            dateofbirth=fld[6],
                            contactnumber=fld[7],
                            emergencycontact=fld[8],
                            contractstartdate=fld[9],
                            locationsite=fld[10],
                            passportidno=fld[11],
                            permitissuedate=fld[12],
                            permitexpirydate=fld[13],
                            medicalstartdate=fld[14],
                            medicalexpirydate=fld[15],
                            operatorstartdate=fld[16],
                            operatorexpirydate=fld[17],
                            defensivestartdate=fld[18],
                            defensiveexpirydate=fld[19],
                            category=fld[20],
                            wostatus=fld[21],  # Field name made lowercase.
                            status=fld[22],
                            imageurl=fld[23]
                        )
                    qs.append(employee)
                x = x+1
                # print(x)
        EmployeeModel.objects.bulk_create(qs)
        
        # for batch in self.read_csv_file("staff.csv", BATCH_SIZE):
        #     EmployeeModel.objects.bulk_create(
        #         [
        #             EmployeeModel(
        #                 idnumber=idnumber,
        #                 name=name,
        #                 designation=designation,
        #                 nationality=nationality,
        #                 gender=gender,
        #                 dateofbirth=dateofbirth,
        #                 contactnumber=contactnumber,
        #                 emergencycontact=emergencycontact,
        #                 contractstartdate=contractstartdate,
        #                 locationsite=locationsite,
        #                 passportidno=passportidno,
        #                 permitissuedate=permitissuedate,
        #                 permitexpirydate=permitexpirydate,
        #                 medicalstartdate=medicalstartdate,
        #                 medicalexpirydate=medicalexpirydate,
        #                 operatorstartdate=operatorstartdate,
        #                 operatorexpirydate=operatorexpirydate,
        #                 defensivestartdate=defensivestartdate,
        #                 defensiveexpirydate=defensiveexpirydate,
        #                 category=category,
        #                 wostatus=wostatus,  # Field name made lowercase.
        #                 status=status,
        #                 imageurl=imageurl
        #             )
                    
        #             # for idnumber, name, designation, nationality, gender, dateofbirth, contactnumber, emergencycontact, contractstartdate, locationsite, passportidno, permitissuedate, permitexpirydate, medicalstartdate, medicalexpirydate, operatorstartdate, operatorexpirydate, defensivestartdate, defensiveexpirydate, category, wostatus, status, imageurl in batch
        #         ],
        #         batch_size=BATCH_SIZE,
        #     )
    
    def delete_staff_records(apps, schema_editor):
        EmployeeModel.objects.all().delete()

# class Migration(migrations.Migration):
#     dependencies = [
#         ("employee", "0001_initial"),
#     ]

#     operations = [
#         migrations.RunPython(
#             code=import_staff_records,
#             reverse_code=delete_staff_records,
#         ),
#     ]