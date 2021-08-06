from django.shortcuts import render, HttpResponse

# Create your views here.
from .models import PollingUnit, AnnouncedPuResults, Ward, Lga


def polling_unit_result(request, id):
    polling_units = PollingUnit.objects.get(uniqueid=id)
    print(polling_units.polling_unit_name)
    print(polling_units.polling_unit_description)
    announced_pu_result = AnnouncedPuResults.objects.filter(polling_unit_uniqueid=polling_units.uniqueid)
    context = {'polling_unit_result':announced_pu_result}
    return render(request, 'election_results/polling_unit_result.html', context)

def  total_result(request, lga_id):
    lgas = Lga.objects.all()
    # wards = Ward.objects.filter(lga_id=lga_id)
    # # print(wards)
    # for ward in wards:
    #     polling_units = PollingUnit.objects.filter(ward_id=ward.ward_id)
        # for polling_unit in polling_units:

        #     print(polling_unit.polling_unit_name)
    # context = {'lgas': lgas, 'polling_units': polling_units}
    return render(request, 'election_results/total_result.html', {'lgas': lgas})
