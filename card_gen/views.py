import os
import random
import requests
import json

import qrcode


from django.db.models.base import Model as Model
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, TemplateView
from django.views import View

from . models import Config
from . forms import ConfigForm, ContactPhoneForm, ContactForm, MessageForm
from .var import API_URL

global_phone_number = "+48"

class APIClient:
    @staticmethod
    def post_api(lead_data):
        url = API_URL
        headers = {'Content-Type': 'application/json'}
        try:
            response = requests.request("POST", url, headers=headers, data=lead_data)
            if response.status_code == 201:
                print(response.text)
        except Exception as error:
            print(f"Found error: {error}")


class NewCard(View):
    def get(self, request):
        context = {
            "config_form": ConfigForm()
        }
        return render(request, 'card_gen/index.html', context)

    def post(self, request):
        config_form = ConfigForm(request.POST, request.FILES)
        if config_form.is_valid():
            config = config_form.save()
            url = reverse('result', kwargs={'user_slug': config.slug})
            config.vcard_address = f"http://127.0.0.1:8000/{config.slug}/card"
            img = qrcode.make(f"http://127.0.0.1:8000{url}card")
            current_directory = os.getcwd()
            directory = os.path.abspath(os.path.join(current_directory, "uploads/qrcodes"))
            if not os.path.exists(directory):
                os.makedirs(directory)
            qr_name = f"qrcode-{url.replace('/', '')}.png"
            img_path = os.path.join(directory, qr_name)
            img.save(img_path)
            config.qr_code_image = f"qrcodes/{qr_name}"
            config.save()
            return HttpResponseRedirect(url)
        else:
            context = {
            "config_form": config_form
        }
        return render(request, 'card_gen/index.html', context)


class ResultView(DetailView):
    model = Config
    template_name = 'card_gen/result.html'
    context_object_name = 'result'

    def get_object(self, queryset=None):
        return get_object_or_404(Config, slug=self.kwargs['user_slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['config'] = self.object
        return context
    
class CardView(DetailView):
    model = Config
    template_name = 'card_gen/card.html'
    context_object_name = 'card'

    def get_object(self, queryset=None):
        return get_object_or_404(Config, slug=self.kwargs['user_slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['config'] = self.object
        return context

    
class PresentationView(View):
    template_name = 'card_gen/presentation.html'

    def get(self, request, user_slug):
        config = Config.objects.get(slug=user_slug)
        contact_phone_form = ContactPhoneForm()
        context = {
            "config": config,
            "contact_phone_form": contact_phone_form,
        }
        return render(request, self.template_name, context)
    
    def post_api(self, lead_data):
        # auth_token = "Authorization"
        url = "https://url_systemu/api/v1/lead/"
        headers = {
        'Content-Type': 'application/json'
        }
        try:
            response = requests.request("POST", url, headers=headers, data=lead_data)
            if response .status_code == 201:
                print(response.text)
        except Exception as error:
            print(f"Found error: {error}")
  

    def post(self, request, user_slug):
        config = Config.objects.get(slug=user_slug)
        contact_phone_form = ContactPhoneForm(request.POST)
        if contact_phone_form.is_valid():
            payload = json.dumps({
                "campaign_token": "{campaign_token}",
                "phone": contact_phone_form.cleaned_data['phone_number'],
                "email": "",
                "name": "",
                "surname": ""
                })
            APIClient.post_api(payload)
            # contact = contact_phone_form.save()
            url = reverse('thank_you', kwargs={'user_slug': config.slug,})
            return HttpResponseRedirect(url)
        else:
            context = {
            "config": config,
            "contact_phone_form": contact_phone_form,
        }
        global global_phone_number 
        global_phone_number = contact_phone_form['phone_number'].value()
        return render(request, self.template_name, context)


class ThankYouView(View):
    template_name = 'card_gen/thank_you.html'

    def get(self, request, user_slug):
        config = Config.objects.get(slug=user_slug)
        contact_form = ContactForm()
        context = {
            "config": config,
            "contact_form": contact_form,
        }
        return render(request, self.template_name, context)

    def post(self, request, user_slug):
        config = Config.objects.get(slug=user_slug)
        contact_form = ContactForm(request.POST)
        full_name = contact_form['name'].value()
        new = full_name.split()
        name = new[0]
        surname = new[1]
        global global_phone_number 

        if contact_form.is_valid():
            payload = json.dumps({
                "campaign_token": "{campaign_token}",
                "phone": global_phone_number,
                "email": contact_form.cleaned_data['email_address'],
                "name": name,
                "surname": surname
                })
            APIClient.post_api(payload)
            url = reverse('message', kwargs={'user_slug': config.slug})
            return HttpResponseRedirect(url)
        else:
            context = {
            "config": config,
            "contact_form": contact_form,
        }
        return render(request, self.template_name, context)


class MessageView(View):
    template_name = 'card_gen/message.html'

    def get(self, request, user_slug):
        config = Config.objects.get(slug=user_slug)
        message_form = MessageForm()
        context = {
            "config": config,
            "message_form": message_form,
        }
        return render(request, self.template_name, context)
    
    def post(self, request, user_slug):
        config = Config.objects.get(slug=user_slug)
        message_form = MessageForm(request.POST)
        global global_phone_number 
        if message_form.is_valid():
            payload = json.dumps({
                "campaign_token": "{campaign_token}",
                "phone": global_phone_number,
                "comments": [
        {
            "text": message_form.cleaned_data["date"]
        },
        {
            "text": message_form.cleaned_data["topic"]
        }
    ]
                })
            APIClient.post_api(payload)
            url = reverse('in_touch', kwargs={'user_slug': config.slug})
            return HttpResponseRedirect(url)
        else:
            context = {
            "config": config,
            "message_form": message_form,
        }
        return render(request, self.template_name, context)


class InTouchView(TemplateView):
    model = Config
    template_name = 'card_gen/in_touch.html'
    context_object_name = 'in_touch'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        config= Config.objects.get(slug=self.kwargs['user_slug'])
        context['config'] = config
        number = random.randint(1, 8)
        meme_name = f"{number}.jpg"
        context['meme_name'] = meme_name
        print(context['meme_name'])

        return context
    
    def post(self, request, *args, **kwargs):
        return redirect('in_touch', user_slug=self.kwargs['user_slug'])
