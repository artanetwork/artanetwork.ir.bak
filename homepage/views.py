from django.views.generic import TemplateView

from .models import About, Activity, Slide, Stat

# Create your views here.


class HomepageView(TemplateView):
    template_name = 'homepage/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slides'] = Slide.objects.all()
        context['about'] = About.objects.first()
        context['activities'] = Activity.objects.all()
        context['stats'] = Stat.objects.all()
        return context
