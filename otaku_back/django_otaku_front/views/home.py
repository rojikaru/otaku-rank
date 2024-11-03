from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'OtakuRank'
        context['description'] = 'OtakuRank is a platform for anime and manga fans to share their opinions and reviews.'
        return context
