from django.shortcuts import render_to_response, render
from django.template.context import RequestContext
from models import Citizen, OBCFormResponse, Case, Office, OfficeVisit, SMSFeedback
from forms import CaseForm, OBCFormForm, CitizenForm, AadhaarLookup, Form
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
import random
import json

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
        data = [];
        uniqueCounter = 0
        for case in Case.objects.all():
            temp = [] 
            temp.append(case.citizen.first_name)
            temp.append(case.citizen.last_name)
            temp.append(case.id)
            temp.append(case.office.office_name)
            temp.append("<input id=" + "'sms" + str(uniqueCounter) + "' type='checkbox' value='False'>")
            temp.append("<input id=" + "'robo" + str(uniqueCounter) + "' type='checkbox' value='False'>")
            temp.append("<input id=" + "'followup" + str(uniqueCounter) + "' type='checkbox' value='False'>")
            temp.append("<a data-toggle='modal' href=" + "'#" + str(case.id) + "' class='btn btn-primary btn-sm'></a>")
            temp.append(case.citizen)
            temp.append(case.office)
            temp.append(case.officevisit_set.all())
            temp.append(case.smsfeedback_set.all())
            temp.append(case.robocallfeedback_set.all())
            data.append(temp)
            uniqueCounter += 1
        context = {"cases": data, "length": len(data)}
        return render_to_response('bribecaster/datatables.html', context)

def SMSOnlyTable(request):
    if request.method == "GET":
        context = {"cases": Case.objects.filter(sms_selected = True)}
        return render_to_response('bribecaster/datatables.html', context)

def RobocallOnlyTable(request):
    if request.method == "GET":
        context = {"cases": Case.objects.filter(robo_call_selected = True)}
        return render_to_response('bribecaster/datatables.html', context)

def FollowUpCallOnlyTable(request):
    if request.method == "GET":
        context = {"cases": Case.objects.filter(sms_selected = True)}
        return render_to_response('bribecaster/datatables.html', context)

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


def obc_form(request, citizen_id=None, aadhaar_number=None):
    if request.method == "POST":
        obc_form_response = OBCFormResponse()
        obc_form = OBCFormForm(request.POST, instance=obc_form_response)
        if obc_form.is_valid():
            case = Case()
            case.office = Office.first()
            case.sms_selected = True
            case.robo_call_selected = False
            case.follow_up_selected = False

            sms_feedback = SMSFeedback().create("I am well satisfied")
            
            office_visit = OfficeVisit()

            if citizen_id != None:
                citizen = Citizen.objects.get(pk = citizen_id)
                case.citizen = citizen
                case.save()

                office_visit.citizen = citizen
                office_visit.case = case
                office_visit.save()
            else:
                user = Citizen()
                citizen = CitizenForm(request.POST, instance=user)
                if citizen.is_valid():
                    citizen = citizen.save()
                    case.citizen = citizen
                    case.save()

                    office_visit.citizen = citizen
                    office_visit.case = case

                    office_visit.save()

            sms_feedback.case = case
            sms_feedback.save()

            obc_form = obc_form.save(commit=False)
            obc_form.citizen = citizen
            obc_form.office_visit = office_visit
            obc_form.save() 
        return HttpResponseRedirect(reverse('aadhaar_lookup'))


    if request.method == "GET":
        obc_form = OBCFormForm()
        citizen_form = CitizenForm(initial={'aadhaar_number': aadhaar_number})
        inputFilter = ["Caste Serial Number", "Name of Father", "Name of Mother", "Male Constitutional Posts",
            "Female Constitutional Posts","Male Start of Appointment", "Male End of Appointment","Female Start of Appointment", "Female End of Appointment"]
        if citizen_id != None:
            try:
                citizen = Citizen.objects.get(pk=citizen_id)
                context = {'obc_form': obc_form, 'citizen': citizen, 'citizen_form':citizen_form, 'inputFilter': inputFilter}
                return render(request, 'bribecaster/OBC_form.html', context)
            except Exception as e:
                pass
        citizen = None
        context = {'obc_form': obc_form, 'citizen': citizen, 'citizen_form':citizen_form, 'inputFilter': inputFilter}
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
                form_aadhaar_number = aadhaar_lookup_response.cleaned_data['aadhaar_number']
                citizen = Citizen.objects.get(aadhaar_number = form_aadhaar_number)
                return HttpResponseRedirect(reverse('obc_form_ci', kwargs={"citizen_id":citizen.id}))
            except Exception as e :
                return HttpResponseRedirect(reverse('obc_form_an', kwargs={"aadhaar_number":form_aadhaar_number}))
        return HttpResponseRedirect(reverse('aadhaar_lookup'))

def office_chart(request, office_id=None):
    if request.method == "GET":
        if office_id == None:
            all_information = {}
            all_information['office_name'] = "All"
            total_sms = 0
            sentiments = {1:0, 2:0, 3:0, 4:0, 5:0}
            offices = Office.objects.all()
            for office in offices:
                for case in office.case_set.all():
                    sentiment = case.smsfeedback_set.first().sms_sentiment
                    sentiments[sentiment] += 1
                    total_sms += 1
            all_information['sentiment'] = sentiments
            all_information['total_sms'] = total_sms
            return HttpResponse(json.dumps(all_information), content_type="application/json") 

        else:

            try:
                office = Office.objects.get(pk=office_id)
            except Exception as e:
                not_found = {'status': 404, 'message':"Office not found " + str(office_id)}
                return HttpResponse(json.dumps(not_found), content_type="application/json") 

            office_information = {}
            office_information['office_name'] = office.office_name

            total_sms = 0
            sentiments = {1:0, 2:0, 3:0, 4:0, 5:0}
            
            for case in office.case_set.all():
                sentiment = case.smsfeedback_set.first().sms_sentiment
                sentiments[sentiment] += 1
                total_sms += 1
            office_information['sentiment'] = sentiments
            office_information['total_sms'] = total_sms
            return HttpResponse(json.dumps(office_information), content_type="application/json") 
            #if an office is specified return json for for that particular office

        #json should be of the form {"office": office_name, "sentiments" {1: count, 2:count, 3:count, 4:count, 5:count}, "total_sms": 40}

def office_num_cases(request):
    if request.method == "GET":
        offices = {}
        cases = Case.objects.all()
        for case in cases:
            if case.office in offices:
                offices[case.office][0] += 1
            else:
                offices[case.office] = [1, 0]
        diff = []
        for office in offices:
            offices[office][0] *= 10 + random.randint(0, 200)
            offices[office][1] = offices[office][0] + random.randint(-offices[office][0], offices[office][0]/2)
            higher = max(offices[office][0], offices[office][1])
            lower = min(offices[office][0], offices[office][1])
            diff.append((office, offices[office][0], offices[office][1], offices[office][0] - offices[office][1], random.randint(lower, higher), random.randint(lower, higher), random.randint(lower, higher), random.randint(lower, higher), random.randint(lower, higher)))
        diff.sort(key=lambda x: x[3])
        context = {'offices': list(enumerate(diff, start=1))}
        return render(request, 'bribecaster/casesperoffice.html', context)



