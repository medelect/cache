from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import datetime


from django.shortcuts import render_to_response
import sqlalchemy, sqlalchemy.orm
from models import Base, Language, Income
from .forms import NameForm, IncomeForm
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


def name(request):
    if request.method == 'POST':
        form_o = NameForm(request.POST)
        if form_o.is_valid():
           # return render(request, 'cache/name.html', {'form': form, 'other': form_o})
            return HttpResponseRedirect('/thanks/')
    else:
        form = NameForm()

    return render(request, 'cache/name.html', {'form': form, 'other': [1, 2, 3]})

def IncomeView(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.validate():
            newRecord = Income('2001-01-03', form.quantas)
            session.add(newRecord)
            session.commit()
            return HttpResponseRedirect('cache/inc.html')
    else:
        form = IncomeForm()

    return render(request, 'cache/income.html', {'form': form})

