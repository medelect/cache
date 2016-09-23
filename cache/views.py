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

def is_empty():
    return len(session.query(Language).all()) <= 0

def populate():
    new_langs = [Language('Python','py'),
                 Language('Ruby', 'rb'),
                 Language('Common Lisp', 'lisp'),
                 Language('Objective-C', 'm')
                ]
    session.add_all(new_langs)
    session.commit()

def index(request):
    if is_empty():
        populate()
    lang = session.query(Language).all()
    return render_to_response('cache/index.html',{'langsi': lang})
    #return HttpResponse("Hello, World")




def dtme(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s. Some changes</body></html>" % now
    return HttpResponse(html)



def inc(request):
    tb = session.query(Income.quantas).filter(Income.quantas > 100).all()
   # tb = session.query(year(Income.date)).all()
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

