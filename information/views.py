from django.shortcuts import render
from django.http import HttpResponse
from .past_or_present import past_or_present

# Create your views here.

def index(request):
    past_or_present()
    return render(request, 'info/index.html')

def indoor(request):
    past_or_present()
    return render(request, 'info/indoor.html')

def outdoor(request):
    past_or_present()
    return render(request, 'info/outdoor.html')

def tools(request):
    past_or_present()
    return render(request, 'info/tools.html')

# indoor 

def page_open_tomato(request):
    past_or_present()
    return render(request, 'indoor_plants/tomato.html')

def page_open_lemon(request):
    past_or_present()
    return render(request, 'indoor_plants/lemon.html')

def page_open_chilly(request):
    past_or_present()
    return render(request, 'indoor_plants/chilly.html')

def page_open_curry(request):
    past_or_present()
    return render(request, 'indoor_plants/curry.html')

def page_open_aloevera(request):
    past_or_present()
    return render(request, 'indoor_plants/Aloevera.html')

def page_open_lemongrass(request):
    past_or_present()
    return render(request, 'indoor_plants/lemongrass.html')

def page_open_turmeric(request):
    past_or_present()
    return render(request, 'indoor_plants/turmeric.html')

def page_open_indianbasil(request):
    past_or_present()
    return render(request, 'indoor_plants/indianbasil.html')

def page_open_babysunrose(request):
    past_or_present()
    return render(request, 'indoor_plants/babysunRose.html')

def page_open_palm(request):
    past_or_present()
    return render(request, 'indoor_plants/cycas_palm.html')

def page_open_moneyplant(request):
    past_or_present()
    return render(request, 'indoor_plants/moneyplant.html')

# outdoor

def page_open_plumbago(request):
    past_or_present()
    return render(request, 'outdoor_plants/plumbago.html')

def page_open_gulmohar(request):
    past_or_present()
    return render(request, 'outdoor_plants/gulmohar.html')

def page_open_ajuga(request):
    past_or_present()
    return render(request, 'outdoor_plants/ajuga.html')

def page_open_hibiscus(request):
    past_or_present()
    return render(request, 'outdoor_plants/hibiscus.html')

def page_open_mango(request):
    past_or_present()
    return render(request, 'outdoor_plants/mango.html')

def page_open_jamun(request):
    past_or_present()
    return render(request, 'outdoor_plants/jamun.html')

def page_open_guava(request):
    past_or_present()
    return render(request, 'outdoor_plants/Guava.html')

def page_open_papaya(request):
    past_or_present()
    return render(request, 'outdoor_plants/papaya.html')

def page_open_coconut(request):
    past_or_present()
    return render(request, 'outdoor_plants/coconut.html')

def page_open_neem(request):
    past_or_present()
    return render(request, 'outdoor_plants/neem.html')

def page_open_ashoka(request):
    past_or_present()
    return render(request, 'outdoor_plants/ashoka.html')


# tools

def page_open_trowel(request):
    past_or_present()
    return render(request, 'gardening_tools/trowel.html')

def page_open_secateurs(request):
    past_or_present()
    return render(request, 'gardening_tools/secateurs.html')

def page_open_rake(request):
    past_or_present()
    return render(request, 'gardening_tools/rake.html')

def page_open_gloves(request):
    past_or_present()
    return render(request, 'gardening_tools/gloves.html')

def page_open_watercan(request):
    past_or_present()
    return render(request, 'gardening_tools/watercan.html')

def page_open_spade(request):
    past_or_present()
    return render(request, 'gardening_tools/spade.html')

def page_open_saw(request):
    past_or_present()
    return render(request, 'gardening_tools/saw.html')

def page_open_hoe(request):
    past_or_present()
    return render(request, 'gardening_tools/hoe.html')

def page_open_knife(request):
    past_or_present()
    return render(request, 'gardening_tools/Gardenknife.html')

def page_open_shovel(request):
    past_or_present()
    return render(request, 'gardening_tools/shovel.html')

def page_open_fork(request):
    past_or_present()
    return render(request, 'gardening_tools/fork.html')
