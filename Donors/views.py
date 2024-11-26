from django.shortcuts import render, redirect
from .models import Donor
from .forms import DonorRegistrationForm, UpdateDonationForm

def register_donor(request):
    if request.method == 'POST':
        form = DonorRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('donor_list')
    else:
        form = DonorRegistrationForm()
    return render(request, 'donors/register.html', {'form': form})

def update_donation(request, donor_id):
    donor = Donor.objects.get(id=donor_id)
    if request.method == 'POST':
        form = UpdateDonationForm(request.POST, instance=donor)
        if form.is_valid():
            form.save()
            return redirect('donor_list')
    else:
        form = UpdateDonationForm(instance=donor)
    return render(request, 'donors/update.html', {'form': form, 'donor': donor})

def donor_list(request):
    # Get filter parameters from the GET request
    blood_group = request.GET.get('blood_group', '')
    name = request.GET.get('name', '')
    mobile_number = request.GET.get('mobile_number', '')
    is_available = request.GET.get('is_available', '')

    # Start with all donors
    donors = Donor.objects.all()

    # Filter by blood group if specified
    if blood_group:
        donors = donors.filter(blood_group=blood_group)

    # Filter by name if specified
    if name:
        donors = donors.filter(name__icontains=name)

    # Filter by mobile number if specified
    if mobile_number:
        donors = donors.filter(mobile_number__icontains=mobile_number)

    # Filter by BCS batch if specified
    if is_available:
        donors = donors.filter(is_available__icontains=is_available)

    return render(request, 'donors/list.html', {'donors': donors})