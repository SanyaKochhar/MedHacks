from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.urls import reverse, reverse_lazy, resolve
from django.shortcuts import HttpResponseRedirect, HttpResponse

from medhacks_app.data import DATA
from medhacks_app.forms import DLForm
# Create your views here.


@login_required
def search_drivers_license(request):
    if request.method == 'POST':
        form = DLForm(request.POST)
        if form.is_valid():
            drivers_license = form.cleaned_data.get('drivers_license')
            return redirect(patient_view, patient_id=drivers_license)
    else:
        form = DLForm()
    return render(request, 'drivers_license_search.html', {'form': form})


@login_required
def patient_view(request, patient_id=0):
    patient_info = get_patient_info(patient_id)
    if patient_info:
        return render(request, 'patientdisplay.html', {'patient': patient_info})
    return HttpResponse("Drivers License Not Found")


def get_patient_info(pid):
    print(pid)
    if pid in DATA.keys():
        return DATA[pid]
    return None


def logout_view(request):
    if not request.user.is_anonymous:
        logout(request)
    return HttpResponseRedirect(reverse_lazy('login'))


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('patient')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})