from fiber.views import FiberTemplateView
from fiber.models import Page
from pages.forms import ContactForm
from pages.models import ContactModel
from django.template.loader import get_template
from django.core.mail import EmailMessage, send_mail
from django.template import Context
from django.shortcuts import render, redirect


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
                # send_mail('Email from ' + contact_name, contact_message, contact_email, ['shelby_dima@mail.ru'], fail_silently=False)
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
