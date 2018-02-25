from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UtilisateurCreationForm(UserCreationForm):

    class Meta():
        fields = ('username','email','password1','password2') #pour confirmer
        model = get_user_model()

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label = 'yoshi account name'
        self.fields['email'].label = 'Email here'
