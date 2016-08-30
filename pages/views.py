# -*- coding: utf-8 -*-

from fiber.views import FiberTemplateView
from django.views.generic import ListView
from django.db.models import Q
from fiber.models import Page, ContentItem, PageContentItem
from pages.forms import ContactForm
from pages.models import ContactModel
from django.template.loader import get_template
from django.core.mail import EmailMessage, send_mail
from django.template import Context
from django.shortcuts import render, redirect

from pure_pagination.mixins import PaginationMixin


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

def contact_me(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        print "=================="

        if form.is_valid():
            print "form is valid"
            contact_name = request.POST.get('name', '')
            contact_email = request.POST.get('email', '')
            contact_message = request.POST.get('message', '')
            
            template = get_template('contact_template.txt')
            print "I am trying to save to db"
            try:
                saved_form = form.save()
                form_id = saved_form.id
                contact_status = True
                print "Entry saved to db"
            except:
                contact_status = False
            
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'contact_message': contact_message,
                'contact_status': contact_status,
            }
            content = template.render(context)
            
            email = EmailMessage(
                "New email from contact form",
                content,
                contact_email,
                ['shelby_dima@mail.ru'],
                headers = {'Reply-To': contact_email }
            )
            print "I am trying to send email"
            try:
                email.send()
                update_saved_form = ContactModel.objects.get(pk=form_id)
                update_saved_form.sended = True
                update_saved_form.save()
                print "Email saved"
            except:
                pass
            
            return redirect('/')
    print form.errors
    return render(request, 'index.html', {
        'form': form,
    })

class SearchList(PaginationMixin, ListView):
    paginate_by = 10 #this variable is used for pagination
    template_name = 'search_results.html'
    
    def get_queryset(self):
                 
        search = self.request.GET.get('search', None)
        self.search = search
        if search:
            search_in_content = ContentItem.objects.filter(content_html__icontains=search).values('id')
            search_in_page_content = PageContentItem.objects.filter(content_item__in=search_in_content).values('page_id')
            objects = Page.objects.filter(
                Q(id__in=search_in_page_content) | Q(title__icontains=search)
                )
        else:
            objects = Page.objects.all()
        
        return objects
    
    def get_context_data(self, **kwargs):
        context = super(SearchList, self).get_context_data(**kwargs)
        context['search'] = self.search
        return context

# def search(request):
#     search = request.GET.get('search', None)
#     search_in_content = ContentItem.objects.filter(content_html__icontains=search).values('id')
#     print search_in_content
#     search_in_page_content = PageContentItem.objects.filter(content_item__in=search_in_content).values('page_id')
#     print search_in_page_content
#     search_results = Page.objects.filter(id__in=search_in_page_content)
#     return render(request, 'search_results.html', {
#         'search': search,
#         'search_results': search_results, 
#     })


    """
    if search_query:
        search_results = Page.objects.live().search(search_query)

        # Log the query so Wagtail can suggest promoted results
        Query.get(search_query).add_hit()
    else:
        search_results = Page.objects.none()

    # Render template
    return render(request, 'search_results.html', {
        'search_query': search_query,
        'search_results': search_results,
    })
    """
