from django.shortcuts import render_to_response, render
from django.template.context import RequestContext
from models import Citizen, OBCFormResponse, Case, Office, OfficeVisit
from forms import CaseForm, OBCFormForm, CitizenForm, AadhaarLookup
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def index(request):
    return render_to_response('bribecaster/index.html', context_instance=RequestContext(request))

def form(request):
    if request.method == 'POST':
        pass
        # create a form instance and populate it with data from the request:
        form = Form(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('bribecaster/form-showcase.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = Form()
    return render(request, 'bribecaster/form-showcase.html', {'form': form})

def detail(request, case_id):
    if request.method == "GET":
        case = Case.objects.get(pk=case_id)
        return render(request, 'bribecaster/userdetail.html', {'case_id': case_id, 
            'case': case, 
            'citizen': case.citizen, 
            'office': case.office,
            'visit': case.officevisit_set.all(),
            'sms': case.smsfeedback_set.all(),
            'robo': case.robocallfeedback_set.all()})
    

def table(request):
    if request.method == "GET":
        context = {"cases": Case.objects.all()}
        return render_to_response('bribecaster/data-table.html', context)

def SMSOnlyTable(request):
    if request.method == "GET":
        context = {"cases": Case.objects.filter(sms_selected = True)}
        return render_to_response('bribecaster/data-table.html', context)

def RobocallOnlyTable(request):
    if request.method == "GET":
        context = {"cases": Case.objects.filter(robo_call_selected = True)}
        return render_to_response('bribecaster/data-table.html', context)

def FollowUpCallOnlyTable(request):
    if request.method == "GET":
        context = {"cases": Case.objects.filter(sms_selected = True)}
        return render_to_response('bribecaster/data-table.html', context)

def user_lookup(request):
    if request.method == "POST":
        user = Citizen()
        citizen_form_response = CitizenForm(request.POST, instance=user)
        if citizen_form_response.is_valid():
            possible_user = None
            try:
                possible_user = Citizen.objects.get(aadhaar_number = citizen_form_response.cleaned_data['aadhaar_number'])
            except Exception as django_api_error:
                pass
            if possible_user:
                return HttpResponseRedirect(reverse('obc_form', kwargs={"citizen_id":possible_user.id}))
            citizen_form_response.save()
            return HttpResponseRedirect(reverse('obc_form', kwargs={"citizen_id":user.id}))

        else:
            citizen_form = CitizenForm()
            context = {"form": citizen_form}
            return render(request, 'bribecaster/user_form.html', context)


    elif request.method == "GET":
        citizen_form = CitizenForm()
        context = {"form": citizen_form}
        return render(request, 'bribecaster/user_form.html', context)


def obc_form(request, citizen_id=None):
    if request.method == "POST":
        citizen = Citizen.objects.get(pk = citizen_id)
        case = Case()
        case.citizen = citizen
        case.office = Office.first()
        case.sms_selected = False
        case.robo_call_selected = False
        case.follow_up_selected = False
        case.save()
        return HttpResponseRedirect(reverse('table'))


    if request.method == "GET":
        obc_form = OBCFormForm()
        citizen_form = CitizenForm()
        if citizen_id != None:
            try:
                citizen = Citizen.objects.get(pk=citizen_id)
                context = {'obc_form': obc_form, 'citizen': citizen, 'citizen_form':citizen_form}
                return render(request, 'bribecaster/OBC_form.html', context)
            except Exception as e:
                pass
        citizen = None
        context = {'obc_form': obc_form, 'citizen': citizen, 'citizen_form':citizen_form}
        return render(request, 'bribecaster/OBC_form.html', context)

def aadhaar_lookup(request):
    if request.method == "GET":
        aadhaar_lookup = AadhaarLookup()
        context = {'aadhaar_form': aadhaar_lookup}
        return render(request, 'bribecaster/aadhaar_lookup.html', context)

    if request.method == "POST":
        aadhaar_lookup_response = AadhaarLookup(request.POST)
        if aadhaar_lookup_response.is_valid():
            try:
                citizen = Citizen.objects.get(aadhaar_number = aadhaar_lookup_response.cleaned_data['aadhaar_number'])
                return HttpResponseRedirect(reverse('obc_form', kwargs={"citizen_id":citizen.id}))
            except Exception as e :
                return HttpResponseRedirect(reverse('obc_form'))
        return HttpResponseRedirect(reverse('obc_form'))






