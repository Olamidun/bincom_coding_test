from django.shortcuts import render, HttpResponse

# Create your views here.
from .models import PollingUnit, AnnouncedPuResults, AnnouncedLgaResults, Ward, Lga


def polling_unit_result(request, id):
    polling_units = PollingUnit.objects.get(uniqueid=id)
    print(polling_units.polling_unit_name)
    print(polling_units.polling_unit_description)
    announced_pu_result = AnnouncedPuResults.objects.filter(polling_unit_uniqueid=polling_units.uniqueid)
    context = {'polling_unit_result':announced_pu_result}
    return render(request, 'election_results/polling_unit_result.html', context)

def total_result(request):
    lgas = Lga.objects.all()

    if request.method == "POST":
        lga = request.POST.get('lga')
        lga_results = AnnouncedLgaResults.objects.all()
        # polling_units = PollingUnit.objects.filter(lga_name=lga)
        polling_unit_results = AnnouncedLgaResults.objects.filter(lga_name=lga)

        print(polling_unit_results)
        # result_list = []
        # for unit in polling_units:
        #     polling_unit_results = AnnouncedLgaResult.objects.filter(polling_unit_uniqueid=unit.uniqueid)
        #     for result in polling_unit_results:
        #         result_list.append(result)
        return render(request, 'election_results/total_result_shown.html', {'polling_unit_results': polling_unit_results })
        
    return render(request, 'election_results/total_result.html', {'lgas': lgas})
