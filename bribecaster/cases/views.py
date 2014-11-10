from django.shortcuts import render_to_response, render
from django.template.context import RequestContext
from models import Form, OBCFormResponse, Case, OfficeVisit, SMSFeedback
from django.http import HttpResponseRedirect

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
            'visit': OfficeVisit.objects.get(case=case_id, citizen=case.citizen),
            'sms': SMSFeedback.objects.get(case=case_id) if (case.sms_selected) else None,
            'robo': RoboCallFeedback.objects.get(case=case_id) if (case.sms_selected and case.robo_call_selected) else None})
    

def table(request):
    return render_to_response('bribecaster/data-table.html', context_instance=RequestContext(request))

def obc_form(request):
    if request.method == "POST":
        # handle the forms
        return 
    if request.method == "GET":
        print("request.get")
        obc_form = OBCFormResponse()
        context = {'form': obc_form}
        return render(request, 'case/OBC_form.html', context)
