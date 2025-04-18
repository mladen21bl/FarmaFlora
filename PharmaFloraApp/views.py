from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Plant
from .forms import PlantForm
from django.core.paginator import Paginator
from django.contrib import messages


INDICATION_CATEGORIES = {
    "Respiratorni sistem": ["ekspektorans", "antitusik", "mukolitik", "bronhodilatator", "antialergik", "antiasmatik"],
    "Digestivni sistem": ["karminativ", "laksativ", "antispazmodik", "digestivni enzim", "antiemetik"],
    "Nervni sistem": ["sedativ", "anksiolitik", "nootropik", "antikonvulziv"],
    "Bubrezi i mokraćni sistem": ["diuretik", "uroantiseptik"],
    "Srce i krvni sudovi": ["kardiotonik", "vazodilatator", "hipotenziv", "antitrombotik"],
    "Imuni sistem": ["imunostimulans", "imunomodulator", "antiinflamator", "antipiretik"],
    "Koža i sluzokože": ["dermatoprotektiv", "cicatrizant", "antiseptik", "antimikotik"],
    "Mišićno-koštani sistem": ["analgetik", "antireumatik", "miorelaksans", "antiedemik"],
    "Endokrini sistem": ["adaptogen", "hipoglikemijski agens", "antidiabetik", "hormonski modulator"],
    "Reproduktivni sistem": ["afrodizijak", "menagog", "antiandrogen", "uterotonik"],
    "Hepatobiliarni sistem": ["hepatoprotektiv", "holagog","holeretik","holekinetik" "detoksikant"],
    "Limfni sistem": ["limfotonik", "limfodrenant", "antiinflamator"],
    "Metabolički sistem": ["antioksidans", "antihiperlipidemijski agens", "metabolički stimulator"],
    "Očne bolesti": ["oftalmotonik", "miotik", "midrijatik", "antiglaukomik"]
}

def index(request):
    indications_filters = request.GET.getlist('indication')

    if not indications_filters:
        if 'indications_filters' in request.session:
            del request.session['indications_filters']

    plants_list = Plant.objects.all()
    if indications_filters:
        for indication in indications_filters:
            plants_list = plants_list.filter(indications__icontains=indication)

    paginator = Paginator(plants_list, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    open_categories = []
    if indications_filters:
        for category, indications in INDICATION_CATEGORIES.items():
            if any(indication in indications_filters for indication in indications):
                open_categories.append(category)

    if indications_filters:
        request.session['indications_filters'] = indications_filters

    context = {
        'page_obj': page_obj,
        'indications_filters': indications_filters,
        'indication_categories': INDICATION_CATEGORIES,
        'open_categories': open_categories,
    }

    return render(request, 'PharmaFloraApp/index.html', context)



def results(request):
    indications_filters = request.GET.getlist('indication')

    plants_list = Plant.objects.all()

    if indications_filters:
        for indication in indications_filters:
            plants_list = plants_list.filter(indications__icontains=indication)

    paginator = Paginator(plants_list, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'indications_filters': indications_filters
    }
    return render(request, 'PharmaFloraApp/search_by_effect.html', context)

def create_plant(request):
    if request.method == 'POST':
        form = PlantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PlantForm()

    context = {
        'form': form,
    }
    return render(request, 'PharmaFloraApp/create_plant.html', context)

def plant_detail(request, pk):
    plant = get_object_or_404(Plant, pk=pk)
    context = {
        'plant': plant,
    }
    return render(request, 'PharmaFloraApp/plant_detail.html', context)

from django.shortcuts import render, get_object_or_404, redirect
from .forms import PlantForm
from .models import Plant

def edit_plant(request, pk):

    plant = get_object_or_404(Plant, pk=pk)

    if request.method == 'POST':
        form = PlantForm(request.POST, request.FILES, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PlantForm(instance=plant)

    context = {
        'form': form,
        'plant': plant,
    }
    return render(request, 'PharmaFloraApp/edit_plant.html', context)

def delete_plant(request, pk):
    plant = get_object_or_404(Plant, pk=pk)

    if request.method == 'POST':
        plant.delete()
        return redirect('index')

    context = {
        'plant': plant,
    }
    return render(request, 'PharmaFloraApp/delete_plant.html', context)



def delete_all_plants(request):
    if request.method == 'POST':
        Plant.objects.all().delete()
        messages.success(request, 'Sve biljke su uspješno izbrisane.')
        return redirect('index')

    return render(request, 'PharmaFloraApp/delete_all_plants.html')

def base(request):
    return render(request, 'PharmaFloraApp/base.html')



def plant_detail_molecule(request, pk):
    plant = get_object_or_404(Plant, pk=pk)
    context = {
        'plant': plant,
    }
    return render(request, 'PharmaFloraApp/plant_detail_molecule.html', context)


def search_by_name(request):
    query = request.GET.get('q')
    plants = Plant.objects.filter(name__icontains=query) if query else Plant.objects.all()

    context = {
        'plants': plants,
    }
    return render(request, 'PharmaFloraApp/search_by_name.html', context)

def clear_session(request):
    if 'indications_filters' in request.session:
        del request.session['indications_filters']
    return HttpResponse("Sesija je obrisana.")
