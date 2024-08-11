from django.shortcuts import render
from .models import *
from .forms import *
from django.core.paginator import Paginator 
from .filters import *
from django.http import HttpResponse

# Create your views here.
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def categoryview(request):
    page_number = request.GET.get('page', 1)
    filter = CategoryFilter(request.GET, queryset=Category.objects.all())
    categories = filter.qs
    paginator = Paginator(categories, 3)
    page = paginator.get_page(page_number)

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CategoryForm()    
    context = {'form':form, 'page':page}
    return render(request, 'category.html', context)




def unitview(request):
    units = Unit.objects.all()
    if request.method == 'POST':
        form = UnitForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UnitForm()   
    context = {'form':form, 'uts':units}
    return render(request, 'unit.html', context)



def itemview(request):
    page_number = request.GET.get('page')
    filter = ItemFilter(request.GET, queryset=Item.objects.all())
    items = filter.qs
    paginator = Paginator(items, 3)
    page = paginator.get_page(page_number)
    items = Item.objects.all()
    if request.method == 'POST':
        form = ItemForm(request.POST)
    else:
        form = ItemForm()
    context = {'form':form, 'page':page}
    return render(request, 'item.html', context)
    

def Supplierview(request):
    suppliers = Supplier.objects.all()
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SupplierForm()
    context = {'form':form, 'supplrs':suppliers}
    return render(request, 'supplier.html', context)    


def Orderview(request):
    orders = Order.objects.all()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = OrderForm()   
    context = {'form':form, 'ordrs':orders}
    return render(request, 'order.html', context)


def Employeeview(request):
    employees = Employee.objects.all()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = EmployeeForm()
    context = {'form':form, 'employs':employees}
    return render(request, 'employee.html', context)


def home(request):
    context={}
    return render(request, 'home.html', context)