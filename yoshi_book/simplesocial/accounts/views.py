from django.shortcuts import render
#reverse_lazy pour log in log out ou je vais
from django.core.urlresolvers import reverse_lazy
#créer un formulaire pour le login
from . import forms
#createview
from django.views.generic import CreateView


# Create your views here.
class SignUp(CreateView):
    form_class = forms.UtilisateurCreationForm
    #reverse_lazy pour aller sur la page que si le user a appuyé sur le bouton submit
    success_url = reverse_lazy('login')
    template_name = ('accounts/signup.html')
