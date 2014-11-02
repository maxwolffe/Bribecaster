from django.shortcuts import render_to_response, render
from django.template.context import RequestContext
from models import CaseForm
from django.http import HttpResponseRedirect

def index(request):
    return render_to_response('bribecaster/index.html', context_instance=RequestContext(request))

def form(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CaseForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('bribecaster/form-showcase.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CaseForm()
    return render(request, 'bribecaster/form-showcase.html', {'form': form})