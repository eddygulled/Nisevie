from .models import StreamCategory, Stream
from bankCredentials.models import BankAccount
from django.contrib.auth.models import User

# add stream category
def add_stream_category(is_expense: bool):
    category_name = "Income"
    if is_expense:
        category_name = "Expense"
    new_category = StreamCategory(category_name = category_name)
    new_category.save()

def add_stream(_linked_account:int, is_expense:bool, _name: str, _amount: float, _interval: int, _tag: str, _can_save: int, _least_expenditure: float, _time_delay: int):
  
    account = BankAccount.objects.get(id = _linked_account)

    stream_category = StreamCategory.objects.get(category_name = "Income")
    if is_expense:
        stream_category = StreamCategory.objects.get(category_name = "Expense")

    new_stream = Stream(linked_account = account, name=_name, category=stream_category, amount=_amount, tag = _tag, time_interval=_interval, can_save_amount=_can_save, least_expenditure=_least_expenditure, time_delay=_time_delay)
    new_stream.save()

def calculate_stream_total(query_set):
    total = 0
    for item in query_set:
        total += float(item['amount'])
    return total

def calculate_plan_total(query_set):
    total = 0
    for item in query_set:
        total += float(item.current_amount)
    return total