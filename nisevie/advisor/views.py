from django.shortcuts import render, redirect

from django.contrib.auth.models import User as AccountHolder
from advisor.models import SavingPlan, Stream, StreamCategory
from bankCredentials.models import BankAccount
from .utils import add_stream, calculate_stream_total

#🌟
def home_view(request):
    holder_id = request.user.id
    customer = AccountHolder.objects.get(id=holder_id)
    bank_account = BankAccount.objects.get(account_holder = customer)

    # saving plans 
    saving_plans = SavingPlan.objects.get(target_account = bank_account)
    context = {
        'plans': saving_plans
    }
    return render(request, 'home.html', context)

# plan advisor landing page
def advisor_view(request):
    return render(request, 'advisor/advisor.html')

# plan advisor record income streams
def advisor_record_incomes(request):
    if request.POST:
        stream_name = request.POST['stream_name']
        stream_amount = request.POST['stream_amount']
        time_interval = request.POST['time_interval']
        stream_frequency = request.POST['stream_frequency']
        add_stream(request.user.id, False, stream_name, stream_amount, stream_frequency, time_interval,     )
        return redirect('/home/streams/')
    
    # active income streams
    holder = AccountHolder.objects.get(id=request.user.id) # account holder
    account = BankAccount.objects.get(account_holder = holder) #account linked to income stream
    stream_category = StreamCategory.objects.get(category_name = "Income")# category classification separating Expenses from Incomes

    income_streams = Stream.objects.filter(category= stream_category, linked_account=account)

    context = {
        'income_streams': income_streams
    }
    return render(request, 'advisor/income_streams.html', context)

def advisor_record_expenses(request):
    if request.POST:
        stream_name = request.POST['stream_name']
        stream_amount = request.POST['stream_amount']
        time_interval = request.POST['time_interval']
        stream_frequency = request.POST['stream_frequency']
        can_save_amount = request.POST['can_save_amount']
        least_expenditure = request.POST['least_expenditure']

        add_stream(request.user.id, True, stream_name, stream_amount, stream_frequency, time_interval, can_save_amount, least_expenditure, 0)
        return redirect('/home/expenses/')
    
    # active expense streams
    holder = AccountHolder.objects.get(id=request.user.id) # account holder
    account = BankAccount.objects.get(account_holder = holder) #account linked to income stream
    stream_category = StreamCategory.objects.get(category_name = "Expense")# category classification separating Expenses from Incomes

    expenses = Stream.objects.filter(category= stream_category, linked_account=account)

    context = {
        'expenses': expenses
    }
    return render(request, 'advisor/expense_streams.html', context)

def advisor_suggestion_view(request):
    holder = AccountHolder.objects.get(id=request.user.id) # account holder
    account = BankAccount.objects.get(account_holder = holder) #account linked to income stream
    total_income = 0

    # active expense streams
    expense_category = StreamCategory.objects.get(category_name = "Expense")
    expense_list = Stream.objects.filter(category= expense_category, linked_account=account)
    expenses = Stream.objects.filter(category= expense_category, linked_account=account).values()
    total_expenses = calculate_stream_total(list(expenses))
    # active income streams
    stream_category = StreamCategory.objects.get(category_name = "Income")
    income_streams = Stream.objects.filter(category= stream_category, linked_account=account).values()
    income_list = Stream.objects.filter(category= stream_category, linked_account=account)
    total_income = calculate_stream_total(list(income_streams))

    context = {
        'total_income': total_income,
        'total_expense': total_expenses,
        'expense_list': expense_list,
        'income_list': income_list
    }

    return render(request, 'advisor/suggestions.html', context)

# 🐛
def PlanCreatorPage(request):
    if request.method == 'POST':
        time_interval = request.POST['interval']
        income_stream = request.POST['income']
        initial_amount = request.POST['amount']
        deposit_frequency = request.POST['frequency']
        new_plan = SavingPlan(time_interval=time_interval,
                              income_stream=income_stream,
                              initial_amount=initial_amount,
                              deposit_frequency=deposit_frequency)
        new_plan.save()

    return render(request, )

