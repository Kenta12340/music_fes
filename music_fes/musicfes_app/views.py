from django.shortcuts import render
from django.shortcuts import redirect
from .models import Reserve
from .forms import ReserveForm
from django.core.paginator import Paginator

def index(request):
    return render(request,'musicfes_app/index.html')

def form(request):
    params = {
        'form': ReserveForm()
    }
    if(request.method == 'POST'):
        name = request.POST['name']
        sheets = request.POST['sheets']
        phone_number = request.POST['phone_number']
        adress = request.POST['adress']
        reserve = Reserve(name=name,sheets=sheets,phone_number=phone_number,adress=adress)
        reserve.save()
        return redirect(to='end')
    return render(request,'musicfes_app/form.html',params)

def end(request):
    return render(request,'musicfes_app/end.html')

def tiket(request):
    return render(request,'musicfes_app/tiket.html')

def info(request):
    return render(request,'musicfes_app/info.html')

def access(request):
    return render(request,'musicfes_app/access.html')
def orderlist(request,page=1):
    data = Reserve.objects.all().reverse()
    paginator = Paginator(data, 10)
    params = {
        'title': 'Message',
        'data': paginator.get_page(page),
    }
    return render(request,'musicfes_app/Orderlist.html',params)
# Create your views here.
