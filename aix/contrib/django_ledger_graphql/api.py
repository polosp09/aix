from django.urls import reverse
import graphene
from django.utils.functional import SimpleLazyObject

from .customers.schema import CustomerQuery
from .customers.mutations import CustomerMutations
from .auth.mutations import AuthMutation
from .auth.schema import QueryUser
from .bank_account.mutations import BankAccountMutations
from aix.contrib.aix_graphql.bill.schema import Bill_list_Query
from aix.contrib.aix_graphql.accounts.schema import Accountlist_Query
from aix.contrib.aix_graphql.bank_account.schema import Bank_account_Query
from aix.contrib.aix_graphql.coa.schema import ChartOfAccountsQuery
from aix.contrib.aix_graphql.entity.schema import Entity_Query
from aix.contrib.aix_graphql.item.schema import UnitOfMeasureQuery

from aix.contrib.aix_graphql.vendor.schema import VendorsQuery
from aix.contrib.aix_graphql.unit.schema import EntityUnitQuery
from aix.contrib.aix_graphql.ledger.schema import LedgerQuery
from aix.contrib.aix_graphql.transaction.schema import TransactionsQuery
from aix.contrib.aix_graphql.journal_entry.schema import JournalEntryQuery
from aix.contrib.aix_graphql.purchase_order.schema import PurchaseOrderQuery

API_PATH = SimpleLazyObject(lambda: reverse("api"))


class Query(
    CustomerQuery,
    Bill_list_Query,
    Accountlist_Query,
    Bank_account_Query,
    ChartOfAccountsQuery,
    Entity_Query,
    UnitOfMeasureQuery,
    VendorsQuery,
    EntityUnitQuery,
    LedgerQuery,
    TransactionsQuery,
    JournalEntryQuery,
    PurchaseOrderQuery,
    QueryUser,

):
    pass

class Mutation(
    CustomerMutations,
    BankAccountMutations,
    AuthMutation,

):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
