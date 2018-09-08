from django.shortcuts import render

# Create your views here.


def patient_view(request, patient_id=0):
    patient_info = get_patient_info(patient_id)
    return render(request, 'patientdisplay.html', {'patient': patient_info})


def get_patient_info(pid):
    return {"name": "Trishul"}