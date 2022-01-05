from django.db.models import Q
from django.views.generic import TemplateView

from cat.models import Car


class CarsView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        params = self.request.GET
        query = Q()
        for key, value in params.items():
            if value and key in vars(Car):
                query &= Q(**{key: value})
        return {"cars": Car.objects.filter(query)}