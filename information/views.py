from django.shortcuts import render
from django.http import HttpResponse
from .past_or_present import past_or_present
import threading
# Create your views here.

def index(request):
    t1 = threading.Thread(target=past_or_present)
    t1.start()
    return render(request, 'info/index.html')

def indoor(request):
    t1 = threading.Thread(target=past_or_present)
    t1.start()
    return render(request, 'info/indoor.html')

def outdoor(request):
    t1 = threading.Thread(target=past_or_present)
    t1.start()
    return render(request, 'info/outdoor.html')

def tools(request):
    t1 = threading.Thread(target=past_or_present)
    t1.start()
    return render(request, 'info/tools.html')

def saplings(request):
    t1 = threading.Thread(target=past_or_present)
    t1.start()
    return render(request, 'info/saplings.html')

# indoor 

def page_open_tomato(request):
    t1 = threading.Thread(target=past_or_present)
    t1.start()
    return render(request, 'indoor_plants/Tomato.html')

def page_open_lemon(request):
    t1 = threading.Thread(target=past_or_present)
    t1.start()
    return render(request, 'indoor_plants/lemon.html')

def page_open_chilly(request):
    t1 = threading.Thread(target=past_or_present)
    t1.start()
    return render(request, 'indoor_plants/chilly.html')

def page_open_curry(request):
    t1 = threading.Thread(target=past_or_present)
    t1.start()
    return render(request, 'indoor_plants/curry.html')

def page_open_aloevera(request):
    t1 = threading.Thread(target=past_or_present)
    t1.start()
    return render(request, 'indoor_plants/Aloevera.html')

def page_open_lemongrass(request):
    t1 = threading.Thread(target=past_or_present)
    t1.start()
    return render(request, 'indoor_plants/lemongrass.html')

def page_open_turmeric(request):
    t1 = threading.Thread(target=past_or_present)
    t1.start()
    return render(request, 'indoor_plants/turmeric.html')

def page_open_indianbasil(request):
    t1 = threading.Thread(target=past_or_present)
    t1.start()
    return render(request, 'indoor_plants/indianbasil.html')

def page_open_babysunrose(request):
    t1 = threading.Thread(target=past_or_present)
    t1.start()
    return render(request, 'indoor_plants/babysunRose.html')

def page_open_palm(request):
    t1 = threading.Thread(target=past_or_present)
    t1.start()
    return render(request, 'indoor_plants/cycas_palm.html')

def page_open_moneyplant(request):
    t1 = threading.Thread(target=past_or_present)
    t1.start()
    return render(request, 'indoor_plants/moneyplant.html')

# outdoor

def page_open_plumbago(request):
    t1 = threading.Thread(target=past_or_present)
    t1.start()
    return render(request, 'outdoor_plants/plumbago.html')

def page_open_gulmohar(request):
    t1 = threading.Thread(target=past_or_present)
    t1.start()
    return render(request, 'outdoor_plants/gulmohar.html')

def page_open_ajuga(request):
    t1 = threading.Thread(target=past_or_present)
    t1.start()
    return render(request, 'outdoor_plants/ajuga.html')

def page_open_hibiscus(request):
    t1 = threading.Thread(target=past_or_present)
    t1.start()
    return render(request, 'outdoor_plants/hibiscus.html')

def page_open_mango(request):
    t1 = threading.Thread(target=past_or_present)
    t1.start()
    return render(request, 'outdoor_plants/mango.html')

def page_open_jamun(request):
    t1 = threading.Thread(target=past_or_present)
    t1.start()
    return render(request, 'outdoor_plants/jamun.html')

def page_open_guava(request):
    t1 = threading.Thread(target=past_or_present)
    t1.start()
    return render(request, 'outdoor_plants/Guava.html')

def page_open_papaya(request):
    t1 = threading.Thread(target=past_or_present)
    t1.start()
    return render(request, 'outdoor_plants/papaya.html')

def page_open_coconut(request):
    t1 = threading.Thread(target=past_or_present)
    t1.start()
    return render(request, 'outdoor_plants/coconut.html')

def page_open_neem(request):
    t1 = threading.Thread(target=past_or_present)
    t1.start()
    return render(request, 'outdoor_plants/neem.html')

def page_open_ashoka(request):
    t1 = threading.Thread(target=past_or_present)
    t1.start()
    return render(request, 'outdoor_plants/Ashoka.html')


# tools

def page_open_trowel(request):
    t1 = threading.Thread(target=past_or_present)
    t1.start()
    return render(request, 'gardening_tools/trowel.html')

def page_open_secateurs(request):
    t1 = threading.Thread(target=past_or_present)
    t1.start()
    return render(request, 'gardening_tools/secateurs.html')

def page_open_rake(request):
    t1 = threading.Thread(target=past_or_present)
    t1.start()
    return render(request, 'gardening_tools/rake.html')

def page_open_gloves(request):
    t1 = threading.Thread(target=past_or_present)
    t1.start()
    return render(request, 'gardening_tools/gloves.html')

def page_open_watercan(request):
    t1 = threading.Thread(target=past_or_present)
    t1.start()
    return render(request, 'gardening_tools/watercan.html')

def page_open_spade(request):
    t1 = threading.Thread(target=past_or_present)
    t1.start()
    return render(request, 'gardening_tools/spade.html')

def page_open_saw(request):
    t1 = threading.Thread(target=past_or_present)
    t1.start()
    return render(request, 'gardening_tools/saw.html')

def page_open_hoe(request):
    t1 = threading.Thread(target=past_or_present)
    t1.start()
    return render(request, 'gardening_tools/hoe.html')

def page_open_knife(request):
    t1 = threading.Thread(target=past_or_present)
    t1.start()
    return render(request, 'gardening_tools/Gardenknife.html')

def page_open_shovel(request):
    t1 = threading.Thread(target=past_or_present)
    t1.start()
    return render(request, 'gardening_tools/shovel.html')

def page_open_fork(request):
    t1 = threading.Thread(target=past_or_present)
    t1.start()
    return render(request, 'gardening_tools/fork.html')
