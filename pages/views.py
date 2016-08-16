from fiber.views import FiberTemplateView
from fiber.models import Page


class IndexPage(FiberTemplateView):
    def get_context_data(self):
        data = super(IndexPage, self).get_context_data()
        data['blog_pages'] = Page.objects.filter(parent__url='blog').order_by('-id')[:4]
        data['cources'] = Page.objects.filter(parent__url='cources').order_by('-id')[:4]
        data['reviews'] = Page.objects.filter(parent__url='reviews').order_by('-id')[:8]
        return data


class AboutTechersPage(FiberTemplateView):
    def get_context_data(self):
        data = super(AboutTechersPage, self).get_context_data()
        data['prepodavateli'] = Page.objects.filter(parent__url='prepodavateli').order_by('-id')[:4]
        return data
