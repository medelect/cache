from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import datetime


from django.shortcuts import render_to_response
import sqlalchemy, sqlalchemy.orm
from models import Base, Language, Income, Bill, Inflow, Groups
from .forms import NameForm, IncomeForm, BillForm, InflowForm, GroupsForm
from django.core.mail import send_mail


engine = sqlalchemy.create_engine('postgresql://axe:222@localhost:5432/my_cache')
Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)

def index():
    return HttpResponse("Tmp Index") 

def inc(request):
    tb = session.query(Income.quantas).filter(Income.quantas > 100).all()
    if tb:
        return render_to_response('cache/inc.html',{'tb': tb})
    return HttpResponse("PPZDC") 


def BillView(request):
    if request.method == 'POST':
        form = BillForm(request.POST)
        if form.validate():
            dataFromForm = {}
            for field in form:
                dataFromForm[field.name] = field._value()
            newRecord = Bill(**dataFromForm)
            session.add(newRecord)
            session.commit()
#            return HttpResponseRedirect('cache/???.html') # show saved record
    else:
        form = BillForm()
    return render(request, 'cache/inpt.html', {'form': form})

def IncomeView(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.validate():
            dataFromForm = {}
            for field in form:
                dataFromForm[field.name] = field._value()
            newRecord = Income(**dataFromForm)
            session.add(newRecord)
            session.commit()
#            return HttpResponseRedirect('cache/inc.html') # show saved record
    else:
        form = IncomeForm()
    return render(request, 'cache/inpt.html', {'form': form})


def InflowView(request):
    if request.method == 'POST':
        form = InflowForm(request.POST)
        if form.validate():
            dataFromForm = {}
            for field in form:
                dataFromForm[field.name] = field._value()
            newRecord = Inflow(**dataFromForm)
            session.add(newRecord)
            session.commit()
#            return HttpResponseRedirect('cache/inc.html') # show saved record
    else:
        form = InflowForm()
    return render(request, 'cache/inpt.html', {'form': form})


def GroupsView(request):
    if request.method == 'POST':
        form = GroupsForm(request.POST)
        if form.validate():
            dataFromForm = {}
            for field in form:
                dataFromForm[field.name] = field._value()
            newRecord = Groups(**dataFromForm)
            session.add(newRecord)
            session.commit()
#            return HttpResponseRedirect('cache/inc.html') # show saved record
    else:
        form = GroupsForm()
    return render(request, 'cache/inpt.html', {'form': form})


