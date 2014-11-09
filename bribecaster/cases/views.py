from django.shortcuts import render_to_response, render
from django.template.context import RequestContext
from models import Citizen, OBCFormResponse
from forms import CaseForm, OBCFormForm, CitizenForm
from django.http import HttpResponseRedirect

def index(request):
    return render_to_response('bribecaster/index.html', context_instance=RequestContext(request))

def form(request):
    if request.method == 'POST':
        pass
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

def user_lookup(request):
    if request.method == "POST":
        user = Citizen()
        citizen_form_response = CitizenForm(request.POST, instance=user)
        citizen_form_response.save()
        return HttpResponseRedirect(reverse('obc_form', args=(user.id,)))

    elif request.method == "GET":
        citizen_form = CitizenForm()
        context = {"form": citizen_form}
        return render(request, 'bribecaster/user_form.html', context)


def obc_form(request):
    if request.method == "POST":
        return HttpResponseRedirect('bribecaster/form-showcase.html')
        pass
        # handle the forms
    if request.method == "GET":
        obc_form = OBCFormForm()
        context = {'form': obc_form}
        return render(request, 'bribecaster/OBC_form.html', context)
