from django.shortcuts import render
from contact.forms import ContactForm
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template
from django.http import HttpResponse

def index(request):
    return render(request, 'contact/about.html')
def contact(request):
    form_class = ContactForm
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():

            contact_email = request.POST.get(
                'contact_email'
            , '')
            form_content = request.POST.get('content', '')

            template = get_template('contact/about_template.txt')
            context = {
                
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render(context)

            email = EmailMessage(
                "Новая форма обратной связи",
                content,
                "Мой сайт" +'',
                ['alexsander.golubnik@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return redirect('contact')

    return render(request, 'contact/about.html', {
        'form': form_class,
    })
