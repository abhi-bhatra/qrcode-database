from dbapp.models import Entry
from django.shortcuts import render, get_object_or_404
from .models import Entry, Customer, Cmodel
from .forms import customerForm

# Create your views here.
def home(request):
    dbapps = Entry.objects
    return render(request, 'dbapp/home.html',{'jobs':dbapps})

def detail(request, job_id):
    if request.method == 'POST':
        filled_form=customerForm(request.POST)
        if filled_form.is_valid():
            if request.POST.get('cname') and request.POST.get('cnumber'):
                post=Customer()
                post.cname= request.POST.get('cname')
                post.cnumber= request.POST.get('cnumber')
                post.save()
            else:
                return render(request,'dbapp/detail.html')
            note="Thanks for registraion"
            new_form=customerForm()
            return render(request, 'dbapp/detail.html', {'form':new_form, 'note':note})
    else:
        form = customerForm()
        job_detail = get_object_or_404(Entry, pk=job_id)
        return render(request, 'dbapp/detail.html',{
            'job':job_detail,
            'form': form
            })
