from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request, 'info/index.html')

def indoor(request):
    return render(request, 'info/indoor.html')

def outdoor(request):
    return render(request, 'info/outdoor.html')

def tools(request):
    return render(request, 'info/tools.html')

# indoor 

def page_open_lemon(request):
    return render(request, 'indoor_plants/lemon.html')

def page_open_chilly(request):
    return render(request, 'indoor_plants/chilly.html')

def page_open_curry(request):
    return render(request, 'indoor_plants/curry.html')

def page_open_aloevera(request):
    return render(request, 'indoor_plants/Aloevera.html')

def page_open_lemongrass(request):
    return render(request, 'indoor_plants/lemongrass.html')

def page_open_turmeric(request):
    return render(request, 'indoor_plants/turmeric.html')

def page_open_indianbasil(request):
    return render(request, 'indoor_plants/indianbasil.html')

def page_open_babysunrose(request):
    return render(request, 'indoor_plants/babysunRose.html')

# outdoor

def page_open_plumbago(request):
    return render(request, 'outdoor_plants/plumbago.html')

def page_open_ajuga(request):
    return render(request, 'outdoor_plants/ajuga.html')

def page_open_hibiscus(request):
    return render(request, 'outdoor_plants/hibiscus.html')

def page_open_mango(request):
    return render(request, 'outdoor_plants/mango.html')

def page_open_jamun(request):
    return render(request, 'outdoor_plants/jamun.html')

def page_open_guava(request):
    return render(request, 'outdoor_plants/Guava.html')

def page_open_papaya(request):
    return render(request, 'outdoor_plants/papaya.html')

def page_open_coconut(request):
    return render(request, 'outdoor_plants/coconut.html')

# tools

def page_open_trowel(request):
    return render(request, 'gardening_tools/trowel.html')

def page_open_secateurs(request):
    return render(request, 'gardening_tools/secateurs.html')

def page_open_rake(request):
    return render(request, 'gardening_tools/rake.html')

def page_open_gloves(request):
    return render(request, 'gardening_tools/gloves.html')

def page_open_watercan(request):
    return render(request, 'gardening_tools/watercan.html')

def page_open_spade(request):
    return render(request, 'gardening_tools/spade.html')

def page_open_saw(request):
    return render(request, 'gardening_tools/saw.html') 

def page_open_hoe(request):
    return render(request, 'gardening_tools/hoe.html') 