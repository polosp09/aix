from django.contrib import admin
# from .models import *
from aix.models.accounts import AccountModel
from aix.models.bank_account import BankAccountModel
from aix.models.bill import BillModel
from aix.models.coa import ChartOfAccountModel
from aix.models.customer import CustomerModel
from aix.models.customer_location import CustomerLocationModel
from aix.models.entity import EntityModel, EntityManagementModel
from aix.models.invoice import InvoiceModel
from aix.models.journalentry import JournalEntryModel
from aix.models.ledger import LedgerModel
from aix.models.transactions import TransactionModel
from aix.models.vendor import VendorModel

# ______________ import aix models _______________

from aix.models.absence_date import AbsenceDateModel
from aix.models.absence_type import AbsenceTypeModel
from aix.models.account_code_prefix import AccountCodePrefixModel
from aix.models.announcement import AnnouncementModel
from aix.models.asset import AssetModel
from aix.models.attached_email import AttachedEmailModel
from aix.models.benefit_calculation import BenefitCalculationModel
from aix.models.benefit_type import BenefitTypeModel
from aix.models.benefit import BenefitModel
from aix.models.business_industry import BusinessIndustryModel
from aix.models.currency_rate import CurrencyRateModel
from aix.models.currency import CurrencyModel
from aix.models.department import DepartmentModel
from aix.models.dependant import DependantModel
from aix.models.document_status import DocumentStatusModel
from aix.models.document_type import DocumentTypeModel
from aix.models.document import DocumentModel
from aix.models.education import EducationModel
from aix.models.employee_assignment import EmployeeAssignmentModel
from aix.models.employee_avatar import EmployeeAvatarModel
from aix.models.employee_contract_type import EmployeeContractTypeModel
from aix.models.employee_contract import EmployeeContractModel
from aix.models.employee_language import EmployeeLanguageModel
from aix.models.employee_license_detail import EmployeeLicenseDetailModel
from aix.models.employee_license_type import EmployeeLicenseTypeModel
from aix.models.employee_of_the_week import EmployeeOfTheWeekModel
from aix.models.employee_payroll_benefit import EmployeePayrollBenefitModel
from aix.models.employee_payroll import EmployeePayrollModel
from aix.models.employee_transaction import EmployeeTransactionModel
from aix.models.employee import EmployeeModel
from aix.models.equipment import EquipmentModel
from aix.models.equipment_assignment import EquipmentAssignmentModel
from aix.models.equipment_axle import EquipmentAxleModel
from aix.models.equipment_handover import EquipmentHandoverModel
from aix.models.equipment_join import EquipmentJoinModel
from aix.models.equipment_manufacturer import EquipmentManufacturerModel
from aix.models.equipment_type import EquipmentTypeModel
from aix.models.general_notification import GeneralNotificationModel
from aix.models.holiday import HolidayModel
from aix.models.immigration_detail import ImmigrationDetailModel
from aix.models.incoming_document_handler import IncomingDocumentHandlerModel
from aix.models.incoming_document_type import IncomingDocumentTypeModel
from aix.models.incoming_document import IncomingDocumentModel
from aix.models.insurance_detail import InsuranceDetailModel
from aix.models.invoice_action import InvoiceActionModel
from aix.models.invoice_status import InvoiceStatusModel
from aix.models.invoice_type import InvoiceTypeModel
from aix.models.job_applicant import JobApplicantModel
from aix.models.job_category import JobCategoryModel
from aix.models.job import JobModel
from aix.models.kpihse import KpiHseModel
from aix.models.kpionoff import KpiOnOffModel
from aix.models.kpiops import KpiOpsModel
from aix.models.kpipob import KpiPobModel
from aix.models.leave_card_carried_over import LeaveCardCarriedOverModel
from aix.models.leave_card_detail import LeaveCardDetailModel
from aix.models.leave_card import LeaveCardModel
from aix.models.leave_request_action import LeaveRequestActionModel
from aix.models.leave_request_detail import LeaveRequestDetailModel
from aix.models.leave_request_status import LeaveRequestStatusModel
from aix.models.leave_request_workflow_action import LeaveRequestWorkflowActionModel
from aix.models.leave_request_workflow import LeaveRequestWorkflowModel
from aix.models.leave_request import LeaveRequestModel
from aix.models.locations import LocationModel
from aix.models.marital_status import MaritalStatusModel
from aix.models.nation import NationModel
from aix.models.notification_external_type import NotificationExternalTypeModel
from aix.models.notification_tracker import NotificationTrackerModel
from aix.models.notification import NotificationModel
from aix.models.payment_mode import PaymentModeModel
from aix.models.payroll_advance_request_action import PayrollAdvanceRequestActionModel
from aix.models.payroll_advance_request_detail import PayrollAdvanceRequestDetailModel
from aix.models.payroll_advance_request_status import PayrollAdvanceRequestStatusModel
from aix.models.payroll_advance_request_workflow_action import PayrollAdvanceRequestWorkflowActionModel
from aix.models.payroll_advance_request_workflow import PayrollAdvanceRequestWorkflowModel
from aix.models.payroll_advance_request import PayrollAdvanceRequestModel
from aix.models.payroll_advance import PayrollAdvanceModel
from aix.models.qualification import QualificationModel
from aix.models.received_email_document import ReceivedEmailDocumentModel
from aix.models.relationship import RelationshipModel
from aix.models.reporter import ReportModel
from aix.models.requisition_action import RequisitionActionModel
from aix.models.requisition_category import RequisitionCategoryModel
from aix.models.requisition_flow_type import RequisitionFlowTypeModel
from aix.models.requisition_status import RequisitionStatusModel
from aix.models.requisition_workflow_action import RequisitionWorkflowActionModel
from aix.models.requisition_workflow import RequisitionWorkflowModel
from aix.models.requisition import RequisitionModel
from aix.models.route_survey import RouteSurveyModel
from aix.models.route_survey_info import RouteSurveyInfoModel
from aix.models.salary import SalaryModel
from aix.models.skill import SkillModel
from aix.models.task_assignee import TaskAssigneeModel
from aix.models.task_status import TaskStatusModel
from aix.models.task import TaskModel
from aix.models.tax import TaxModel
from aix.models.user_allocation import UserAllocationModel
from aix.models.visa import VisaModel
from aix.models.weekend import WeekendModel
from aix.models.weekly_employee_processed import WeeklyEmployeeProcessedModel
from aix.models.weekly_employee import WeeklyEmployeeModel
from aix.models.work_category import WorkCategoryModel
from aix.models.work_order_status import WorkOrderStatusModel
from aix.models.work_order_jobcard_status import WorkOrderJobcardStatusModel
from aix.models.work_order_jobcard import WorkOrderJobcardModel
from aix.models.work_order_type import WorkOrderTypeModel
from aix.models.work_order import WorkOrderModel
from aix.models.workflow_action_type import WorkflowActionTypeModel
from aix.models.workflow_action import WorkflowActionModel
from aix.models.workflow_status import WorkflowStatusModel
from aix.models.workflow_type import WorkflowTypeModel
from aix.models.workflow import WorkflowModel

# _______________________ end _______________________

class TransactionModelInLine(admin.TabularInline):
    model = TransactionModel


class JournalEntryModelAdmin(admin.ModelAdmin):
    readonly_fields = [
        'ledger'
    ]
    inlines = [
        TransactionModelInLine
    ]

    class Meta:
        model = JournalEntryModel


class EntityManagementInLine(admin.TabularInline):
    model = EntityManagementModel

class EntityManagementModelAdmin(admin.ModelAdmin):
    model = EntityManagementModel

class EntityModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',)
    }
    inlines = [
        EntityManagementInLine
    ]

    class Meta:
        model = EntityModel


class AccountModelAdmin(admin.ModelAdmin):
    actions = [
        'activate',
        'inactivate',
        'lock',
        'unlock'
    ]
    actions_on_top = True
    actions_on_bottom = True
    sortable_by = [
        'code'
    ]
    list_display = [
        '__str__',
        'active',
        'locked'
    ]
    list_filter = [
        'role',
        'balance_type',
    ]

    class Meta:
        model = AccountModel

    def activate(self, request, queryset):
        queryset.update(active=True)

    def inactivate(self, request, queryset):
        queryset.update(active=False)

    def lock(self, request, queryset):
        queryset.update(locked=True)

    def unlock(self, request, queryset):
        queryset.update(locked=False)

    # def role_bs(self, acc):
    #     return acc.role_bs.upper()

    # role_bs.short_description = 'Balance Sheet Role'


class AccountsModelInLine(admin.TabularInline):
    model = AccountModel
    readonly_fields = [
        'role_bs',
        'role',
        'balance_type',
    ]


class ChartOfAccountsModelAdmin(admin.ModelAdmin):
    inlines = [
        AccountsModelInLine
    ]

    class Meta:
        model = ChartOfAccountModel


class LedgerModelAdmin(admin.ModelAdmin):
    class Meta:
        model = LedgerModel


class InvoiceModelAdmin(admin.ModelAdmin):
    readonly_fields = [
        'invoice_number',
        'due_date',
        'ledger'
    ]

    class Meta:
        model = InvoiceModel


class BillModelAdmin(admin.ModelAdmin):
    readonly_fields = [
        'bill_number',
        'due_date',
        'ledger'
    ]

    class Meta:
        model = BillModel


class BankAccountModelAdmin(admin.ModelAdmin):
    class Meta:
        model = BankAccountModel


class CustomerModelAdmin(admin.ModelAdmin):
    class Meta:
        model = CustomerModel


class CustomerLocationModelAdmin(admin.ModelAdmin):
    class Meta:
        model = CustomerLocationModel

class VendorModelAdmin(admin.ModelAdmin):
    class Meta:
        model = VendorModel

# ___________________ set aix models ___________________

class AbsenceDateModelAdmin(admin.ModelAdmin):
    class Meta:
        model = AbsenceDateModel


class AbsenceTypeModelAdmin(admin.ModelAdmin):
    class Meta:
        model = AbsenceTypeModel


class AccountCodePrefixModelAdmin(admin.ModelAdmin):
    class Meta:
        model = AccountCodePrefixModel

class AnnouncementModelAdmin(admin.ModelAdmin):
    class Meta:
        model = AnnouncementModel

class AssetModelAdmin(admin.ModelAdmin):
    class Meta:
        model = AssetModel

class AttachedEmailModelAdmin(admin.ModelAdmin):
    class Meta:
        model = AttachedEmailModel

class BenefitCalculationModelAdmin(admin.ModelAdmin):
    class Meta:
        model = BenefitCalculationModel

class BenefitTypeModelAdmin(admin.ModelAdmin):
    class Meta:
        model = BenefitTypeModel

class BenefitModelAdmin(admin.ModelAdmin):
    class Meta:
        model = BenefitModel

class BusinessIndustryModelAdmin(admin.ModelAdmin):
    class Meta:
        model = BusinessIndustryModel

class CurrencyRateModelAdmin(admin.ModelAdmin):
    class Meta:
        model = CurrencyRateModel

class CurrencyModelAdmin(admin.ModelAdmin):
    class Meta:
        model = CurrencyModel

class DepartmentModelAdmin(admin.ModelAdmin):
    class Meta:
        model = DepartmentModel

class DependantModelAdmin(admin.ModelAdmin):
    class Meta:
        model = DependantModel

class DocumentStatusModelAdmin(admin.ModelAdmin):
    class Meta:
        model = DocumentStatusModel

class DocumentTypeModelAdmin(admin.ModelAdmin):
    class Meta:
        model = DocumentTypeModel

class DocumentModelAdmin(admin.ModelAdmin):
    class Meta:
        model = DocumentModel

class EducationModelAdmin(admin.ModelAdmin):
    class Meta:
        model = EducationModel

class EmployeeAssignmentModelAdmin(admin.ModelAdmin):
    class Meta:
        model = EmployeeAssignmentModel

class EmployeeAvatarModelAdmin(admin.ModelAdmin):
    class Meta:
        model = EmployeeAvatarModel

class EmployeeContractTypeModelAdmin(admin.ModelAdmin):
    class Meta:
        model = EmployeeContractTypeModel

class EmployeeContractModelAdmin(admin.ModelAdmin):
    class Meta:
        model = EmployeeContractModel

class EmployeeLanguageModelAdmin(admin.ModelAdmin):
    class Meta:
        model = EmployeeLanguageModel

class EmployeeLicenseDetailModelAdmin(admin.ModelAdmin):
    class Meta:
        model = EmployeeLicenseDetailModel

class EmployeeLicenseTypeModelAdmin(admin.ModelAdmin):
    class Meta:
        model = EmployeeLicenseTypeModel

class EmployeeOfTheWeekModelAdmin(admin.ModelAdmin):
    class Meta:
        model = EmployeeOfTheWeekModel

class EmployeePayrollBenefitModelAdmin(admin.ModelAdmin):
    class Meta:
        model = EmployeePayrollBenefitModel

class EmployeePayrollModelAdmin(admin.ModelAdmin):
    class Meta:
        model = EmployeePayrollModel

class EmployeeTransactionModelAdmin(admin.ModelAdmin):
    class Meta:
        model = EmployeeTransactionModel

class EmployeeModelAdmin(admin.ModelAdmin):
    class Meta:
        model = EmployeeModel

class GeneralNotificationModelAdmin(admin.ModelAdmin):
    class Meta:
        model = GeneralNotificationModel

class HolidayModelAdmin(admin.ModelAdmin):
    class Meta:
        model = HolidayModel

class ImmigrationDetailModelAdmin(admin.ModelAdmin):
    class Meta:
        model = ImmigrationDetailModel

class IncomingDocumentHandlerModelAdmin(admin.ModelAdmin):
    class Meta:
        model = IncomingDocumentHandlerModel

class IncomingDocumentTypeModelAdmin(admin.ModelAdmin):
    class Meta:
        model = IncomingDocumentTypeModel

class IncomingDocumentModelAdmin(admin.ModelAdmin):
    class Meta:
        model = IncomingDocumentModel

class InsuranceDetailModelAdmin(admin.ModelAdmin):
    class Meta:
        model = InsuranceDetailModel

class InvoiceActionModelAdmin(admin.ModelAdmin):
    class Meta:
        model = InvoiceActionModel

class InvoiceStatusModelAdmin(admin.ModelAdmin):
    class Meta:
        model = InvoiceStatusModel

class InvoiceTypeModelAdmin(admin.ModelAdmin):
    class Meta:
        model = InvoiceTypeModel

class JobApplicantModelAdmin(admin.ModelAdmin):
    class Meta:
        model = JobApplicantModel

class JobCategoryModelAdmin(admin.ModelAdmin):
    class Meta:
        model = JobCategoryModel

class JobModelAdmin(admin.ModelAdmin):
    class Meta:
        model = JobModel

class KpiHseModelAdmin(admin.ModelAdmin):
    class Meta:
        model = KpiHseModel

class KpiOnOffModelAdmin(admin.ModelAdmin):
    class Meta:
        model = KpiOnOffModel

class KpiOpsModelAdmin(admin.ModelAdmin):
    class Meta:
        model = KpiOpsModel

class KpiPobModelAdmin(admin.ModelAdmin):
    class Meta:
        model = KpiPobModel

class LeaveCardCarriedOverModelAdmin(admin.ModelAdmin):
    class Meta:
        model = LeaveCardCarriedOverModel

class LeaveCardDetailModelAdmin(admin.ModelAdmin):
    class Meta:
        model = LeaveCardDetailModel

class LeaveCardModelAdmin(admin.ModelAdmin):
    class Meta:
        model = LeaveCardModel

class LeaveRequestActionModelAdmin(admin.ModelAdmin):
    class Meta:
        model = LeaveRequestActionModel

class LeaveRequestDetailModelAdmin(admin.ModelAdmin):
    class Meta:
        model = LeaveRequestDetailModel

class LeaveRequestStatusModelAdmin(admin.ModelAdmin):
    class Meta:
        model = LeaveRequestStatusModel

class LeaveRequestWorkflowActionModelAdmin(admin.ModelAdmin):
    class Meta:
        model = LeaveRequestWorkflowActionModel

class LeaveRequestWorkflowModelAdmin(admin.ModelAdmin):
    class Meta:
        model = LeaveRequestWorkflowModel

class LeaveRequestModelAdmin(admin.ModelAdmin):
    class Meta:
        model = LeaveRequestModel

class LocationModelAdmin(admin.ModelAdmin):
    class Meta:
        model = LocationModel

class MaritalStatusModelAdmin(admin.ModelAdmin):
    class Meta:
        model = MaritalStatusModel

class NationModelAdmin(admin.ModelAdmin):
    class Meta:
        model = NationModel

class NotificationExternalTypeModelAdmin(admin.ModelAdmin):
    class Meta:
        model = NotificationExternalTypeModel

class NotificationTrackerModelAdmin(admin.ModelAdmin):
    class Meta:
        model = NotificationTrackerModel

class NotificationModelAdmin(admin.ModelAdmin):
    class Meta:
        model = NotificationModel

class PaymentModeModelAdmin(admin.ModelAdmin):
    class Meta:
        model = PaymentModeModel

class PayrollAdvanceRequestActionModelAdmin(admin.ModelAdmin):
    class Meta:
        model = PayrollAdvanceRequestActionModel

class PayrollAdvanceRequestDetailModelAdmin(admin.ModelAdmin):
    class Meta:
        model = PayrollAdvanceRequestDetailModel

class PayrollAdvanceRequestStatusModelAdmin(admin.ModelAdmin):
    class Meta:
        model = PayrollAdvanceRequestStatusModel

class PayrollAdvanceRequestWorkflowActionModelAdmin(admin.ModelAdmin):
    class Meta:
        model = PayrollAdvanceRequestWorkflowActionModel

class PayrollAdvanceRequestWorkflowModelAdmin(admin.ModelAdmin):
    class Meta:
        model = PayrollAdvanceRequestWorkflowModel

class PayrollAdvanceRequestModelAdmin(admin.ModelAdmin):
    class Meta:
        model = PayrollAdvanceRequestModel

class PayrollAdvanceModelAdmin(admin.ModelAdmin):
    class Meta:
        model = PayrollAdvanceModel

class QualificationModelAdmin(admin.ModelAdmin):
    class Meta:
        model = QualificationModel

class ReceivedEmailDocumentModelAdmin(admin.ModelAdmin):
    class Meta:
        model = ReceivedEmailDocumentModel

class RelationshipModelAdmin(admin.ModelAdmin):
    class Meta:
        model = RelationshipModel

class RequisitionActionModelAdmin(admin.ModelAdmin):
    class Meta:
        model = RequisitionActionModel

class RequisitionCategoryModelAdmin(admin.ModelAdmin):
    class Meta:
        model = RequisitionCategoryModel

class RequisitionFlowTypeModelAdmin(admin.ModelAdmin):
    class Meta:
        model = RequisitionFlowTypeModel

class RequisitionStatusModelAdmin(admin.ModelAdmin):
    class Meta:
        model = RequisitionStatusModel

class RequisitionWorkflowActionModelAdmin(admin.ModelAdmin):
    class Meta:
        model = RequisitionWorkflowActionModel

class RequisitionWorkflowModelAdmin(admin.ModelAdmin):
    class Meta:
        model = RequisitionWorkflowModel

class RequisitionModelAdmin(admin.ModelAdmin):
    class Meta:
        model = RequisitionModel

class RouteSurveyModelAdmin(admin.ModelAdmin):
    class Meta:
        model = RouteSurveyModel

class RouteSurveyInfoModelAdmin(admin.ModelAdmin):
    class Meta:
        model = RouteSurveyInfoModel

class SalaryModelAdmin(admin.ModelAdmin):
    class Meta:
        model = SalaryModel

class SkillModelAdmin(admin.ModelAdmin):
    class Meta:
        model = SkillModel

class TaskAssigneeModelAdmin(admin.ModelAdmin):
    class Meta:
        model = TaskAssigneeModel

class TaskStatusModelAdmin(admin.ModelAdmin):
    class Meta:
        model = TaskStatusModel

class TaskModelAdmin(admin.ModelAdmin):
    class Meta:
        model = TaskModel

class TaxModelAdmin(admin.ModelAdmin):
    class Meta:
        model = TaxModel

class UserAllocationModelAdmin(admin.ModelAdmin):
    class Meta:
        model = UserAllocationModel

class ReportModelAdmin(admin.ModelAdmin):
    class Meta:
        model = ReportModel

class VisaModelAdmin(admin.ModelAdmin):
    class Meta:
        model = VisaModel

class WeekendModelAdmin(admin.ModelAdmin):
    class Meta:
        model = WeekendModel

class WeeklyEmployeeProcessedModelAdmin(admin.ModelAdmin):
    class Meta:
        model = WeeklyEmployeeProcessedModel

class WeeklyEmployeeModelAdmin(admin.ModelAdmin):
    class Meta:
        model = WeeklyEmployeeModel

class WorkCategoryModelAdmin(admin.ModelAdmin):
    class Meta:
        model = WorkCategoryModel

class WorkOrderStatusModelAdmin(admin.ModelAdmin):
    class Meta:
        model = WorkOrderStatusModel

class WorkOrderJobcardStatusModelAdmin(admin.ModelAdmin):
    class Meta:
        model = WorkOrderJobcardStatusModel

class WorkOrderJobcardModelAdmin(admin.ModelAdmin):
    class Meta:
        model = WorkOrderJobcardModel

class WorkOrderTypeModelAdmin(admin.ModelAdmin):
    class Meta:
        model = WorkOrderTypeModel

class WorkOrderModelAdmin(admin.ModelAdmin):
    class Meta:
        model = WorkOrderModel

class WorkflowActionTypeModelAdmin(admin.ModelAdmin):
    class Meta:
        model = WorkflowActionTypeModel

class WorkflowActionModelAdmin(admin.ModelAdmin):
    class Meta:
        model = WorkflowActionModel

class WorkflowStatusModelAdmin(admin.ModelAdmin):
    class Meta:
        model = WorkflowStatusModel

class WorkflowTypeModelAdmin(admin.ModelAdmin):
    class Meta:
        model = WorkflowTypeModel

class WorkflowModelAdmin(admin.ModelAdmin):
    class Meta:
        model = WorkflowModel


admin.site.register(EntityModel, EntityModelAdmin)
admin.site.register(JournalEntryModel, JournalEntryModelAdmin)
admin.site.register(LedgerModel, LedgerModelAdmin)
admin.site.register(ChartOfAccountModel, ChartOfAccountsModelAdmin)
admin.site.register(AccountModel, AccountModelAdmin)
admin.site.register(InvoiceModel, InvoiceModelAdmin)
admin.site.register(BillModel, BillModelAdmin)
admin.site.register(BankAccountModel, BankAccountModelAdmin)
admin.site.register(CustomerModel, CustomerModelAdmin)
admin.site.register(CustomerLocationModel, CustomerLocationModelAdmin)
admin.site.register(VendorModel, VendorModelAdmin)
admin.site.register(EntityManagementModel, EntityManagementModelAdmin)

# ___________________ add aix model ___________________

admin.site.register(AbsenceDateModel, AbsenceDateModelAdmin)
admin.site.register(AbsenceTypeModel, AbsenceTypeModelAdmin)
admin.site.register(AnnouncementModel, AnnouncementModelAdmin)
admin.site.register(AccountCodePrefixModel, AccountCodePrefixModelAdmin)
admin.site.register(AssetModel, AssetModelAdmin)
admin.site.register(AttachedEmailModel, AttachedEmailModelAdmin)
admin.site.register(BenefitCalculationModel, BenefitCalculationModelAdmin)
admin.site.register(BenefitTypeModel, BenefitTypeModelAdmin)
admin.site.register(BenefitModel, BenefitModelAdmin)
admin.site.register(BusinessIndustryModel, BusinessIndustryModelAdmin)
admin.site.register(CurrencyRateModel, CurrencyRateModelAdmin)
admin.site.register(CurrencyModel, CurrencyModelAdmin)
admin.site.register(DepartmentModel, DepartmentModelAdmin)
admin.site.register(DependantModel, DependantModelAdmin)
admin.site.register(DocumentStatusModel, DocumentStatusModelAdmin)
admin.site.register(DocumentTypeModel, DocumentTypeModelAdmin)
admin.site.register(DocumentModel, DocumentModelAdmin)
admin.site.register(EducationModel, EducationModelAdmin)
admin.site.register(EmployeeAssignmentModel, EmployeeAssignmentModelAdmin)
admin.site.register(EmployeeAvatarModel, EmployeeAvatarModelAdmin)
admin.site.register(EmployeeContractTypeModel, EmployeeContractTypeModelAdmin)
admin.site.register(EmployeeContractModel, EmployeeContractModelAdmin)
admin.site.register(EmployeeLanguageModel, EmployeeLanguageModelAdmin)
admin.site.register(EmployeeLicenseDetailModel, EmployeeLicenseDetailModelAdmin)
admin.site.register(EmployeeLicenseTypeModel, EmployeeLicenseTypeModelAdmin)
admin.site.register(EmployeeOfTheWeekModel, EmployeeOfTheWeekModelAdmin)
admin.site.register(EmployeePayrollBenefitModel, EmployeePayrollBenefitModelAdmin)
admin.site.register(EmployeePayrollModel, EmployeePayrollModelAdmin)
admin.site.register(EmployeeTransactionModel, EmployeeTransactionModelAdmin)
admin.site.register(EmployeeModel, EmployeeModelAdmin)
admin.site.register(GeneralNotificationModel, GeneralNotificationModelAdmin)
admin.site.register(HolidayModel, HolidayModelAdmin)
admin.site.register(ImmigrationDetailModel, ImmigrationDetailModelAdmin)
admin.site.register(IncomingDocumentHandlerModel, IncomingDocumentHandlerModelAdmin)
admin.site.register(IncomingDocumentTypeModel, IncomingDocumentTypeModelAdmin)
admin.site.register(IncomingDocumentModel, IncomingDocumentModelAdmin)
admin.site.register(InsuranceDetailModel, InsuranceDetailModelAdmin)
admin.site.register(InvoiceActionModel, InvoiceActionModelAdmin)
admin.site.register(InvoiceStatusModel, InvoiceStatusModelAdmin)
admin.site.register(InvoiceTypeModel, InvoiceTypeModelAdmin)
admin.site.register(JobApplicantModel, JobApplicantModelAdmin)
admin.site.register(JobCategoryModel, JobCategoryModelAdmin)
admin.site.register(JobModel, JobModelAdmin)
admin.site.register(KpiHseModel, KpiHseModelAdmin)
admin.site.register(KpiOnOffModel, KpiOnOffModelAdmin)
admin.site.register(KpiOpsModel, KpiOpsModelAdmin)
admin.site.register(KpiPobModel, KpiPobModelAdmin)
admin.site.register(LeaveCardCarriedOverModel, LeaveCardCarriedOverModelAdmin)
admin.site.register(LeaveCardDetailModel, LeaveCardDetailModelAdmin)
admin.site.register(LeaveCardModel, LeaveCardModelAdmin)
admin.site.register(LeaveRequestActionModel, LeaveRequestActionModelAdmin)
admin.site.register(LeaveRequestDetailModel, LeaveRequestDetailModelAdmin)
admin.site.register(LeaveRequestStatusModel, LeaveRequestStatusModelAdmin)
admin.site.register(LeaveRequestWorkflowActionModel, LeaveRequestWorkflowActionModelAdmin)
admin.site.register(LeaveRequestWorkflowModel, LeaveRequestWorkflowModelAdmin)
admin.site.register(LeaveRequestModel, LeaveRequestModelAdmin)
admin.site.register(LocationModel, LocationModelAdmin)
admin.site.register(MaritalStatusModel, MaritalStatusModelAdmin)
admin.site.register(NationModel, NationModelAdmin)
admin.site.register(NotificationExternalTypeModel, NotificationExternalTypeModelAdmin)
admin.site.register(NotificationTrackerModel, NotificationTrackerModelAdmin)
admin.site.register(PaymentModeModel, PaymentModeModelAdmin)
admin.site.register(PayrollAdvanceRequestActionModel, PayrollAdvanceRequestActionModelAdmin)
admin.site.register(PayrollAdvanceRequestDetailModel, PayrollAdvanceRequestDetailModelAdmin)
admin.site.register(PayrollAdvanceRequestStatusModel, PayrollAdvanceRequestStatusModelAdmin)
admin.site.register(PayrollAdvanceRequestWorkflowActionModel, PayrollAdvanceRequestWorkflowActionModelAdmin)
admin.site.register(PayrollAdvanceRequestWorkflowModel, PayrollAdvanceRequestWorkflowModelAdmin)
admin.site.register(PayrollAdvanceRequestModel, PayrollAdvanceRequestModelAdmin)
admin.site.register(QualificationModel, QualificationModelAdmin)
admin.site.register(ReceivedEmailDocumentModel, ReceivedEmailDocumentModelAdmin)
admin.site.register(RelationshipModel, ReceivedEmailDocumentModelAdmin)
admin.site.register(ReportModel, ReportModelAdmin)
admin.site.register(RequisitionActionModel, RequisitionActionModelAdmin)
admin.site.register(RequisitionCategoryModel, RequisitionCategoryModelAdmin)
admin.site.register(RequisitionFlowTypeModel, RequisitionFlowTypeModelAdmin)
admin.site.register(RequisitionStatusModel, RequisitionStatusModelAdmin)
admin.site.register(RequisitionWorkflowActionModel, RequisitionWorkflowActionModelAdmin)
admin.site.register(RequisitionWorkflowModel, RequisitionWorkflowModelAdmin)
admin.site.register(RequisitionModel, RequisitionModelAdmin)
admin.site.register(RouteSurveyModel, RouteSurveyModelAdmin)
admin.site.register(RouteSurveyInfoModel, RouteSurveyInfoModelAdmin)
admin.site.register(SalaryModel, SalaryModelAdmin)
admin.site.register(SkillModel, SkillModelAdmin)
admin.site.register(TaskAssigneeModel, TaskAssigneeModelAdmin)
admin.site.register(TaskStatusModel, TaskStatusModelAdmin)
admin.site.register(TaskModel, TaskModelAdmin)
admin.site.register(TaxModel, TaxModelAdmin)
admin.site.register(UserAllocationModel, UserAllocationModelAdmin)
admin.site.register(VisaModel, VisaModelAdmin)
admin.site.register(WeeklyEmployeeProcessedModel, WeeklyEmployeeProcessedModelAdmin)
admin.site.register(WeeklyEmployeeModel, WeeklyEmployeeModelAdmin)
admin.site.register(WeekendModel, WeekendModelAdmin)
admin.site.register(WorkCategoryModel, WorkCategoryModelAdmin)
admin.site.register(WorkOrderJobcardStatusModel, WorkOrderStatusModelAdmin)
admin.site.register(WorkOrderJobcardModel, WorkOrderJobcardModelAdmin)
admin.site.register(WorkOrderTypeModel, WorkOrderTypeModelAdmin)
admin.site.register(WorkOrderModel, WorkOrderModelAdmin)
admin.site.register(WorkflowActionTypeModel, WorkflowActionTypeModelAdmin)
admin.site.register(WorkflowActionModel, WorkflowActionModelAdmin)
admin.site.register(WorkflowStatusModel, WorkflowStatusModelAdmin)
admin.site.register(WorkflowTypeModel, WorkflowTypeModelAdmin)
admin.site.register(WorkflowModel, WorkflowModelAdmin)
