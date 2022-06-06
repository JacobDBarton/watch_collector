from multiprocessing import context
from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Watch

# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'

class Description(TemplateView):
    template_name = 'description.html'

class Watch_View:
    def __init__(self, name, image, description):
        self.name = name
        self.image = image
        self.description = description

watches = [
    Watch("Privateer Sport Mechanical Brown Leather Watch", "https://fossil.scene7.com/is/image/FossilPartners/BQ2429_main?$sfcc_fos_large$", "The Privateer Sport is a stainless steel watch with a black case color. It comes equipped with a clear dial color and a brown leather band sitting at 45mm on the size chart."),
    Watch("The Minimalist Three-Hand Brown Leather Watch", "https://fossil.scene7.com/is/image/FossilPartners/FS5439_main?$sfcc_fos_large$", "The Minimalist 3H is a stainless steel watch with a silver case color. It comes equipped with a beige dial color and a brown leather band sitting at 44mm on the size chart."),
    Watch("Rhett Chronograph Brown Leather Watch", "https://fossil.scene7.com/is/image/FossilPartners/BQ2163_main?$sfcc_fos_large$", "The Rhett is a stainless steel watch with a 2-Tone case color. It comes equipped with a navy blue dial color and a light brown leather band sitting at 42mm on the size chart."),
    Watch("Fenmore Midsize Multifunction Black Leather Watch", "https://fossil.scene7.com/is/image/FossilPartners/BQ2364_main?$sfcc_fos_large$", "The Fenmore is a stainless steel watch with a base case color. It comes equipped with a black dial color and black fashion band sitting at 44mm on the size chart."),
]

class WatchList(TemplateView):
    model=Watch
    template_name = 'watch_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["watches"] = Watch.objects.all()
        return context