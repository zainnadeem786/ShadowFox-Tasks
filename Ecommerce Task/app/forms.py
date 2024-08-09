from django import forms
from .models import Order


class CheckoutForm(forms.ModelForm):
    first_name = forms.CharField( widget= forms.TextInput( attrs={'placeholder' : 'First Name' } ) )
    last_name = forms.CharField( widget= forms.TextInput( attrs={'placeholder' : 'last Name' } ) )
    email = forms.EmailField( widget= forms.TextInput( attrs={'placeholder' : 'Email' } ) )
    phone = forms.CharField( widget= forms.TextInput( attrs={'placeholder' : 'Phone' } ) )
    address = forms.CharField( widget= forms.TextInput( attrs={'placeholder' : ' Enter address' } ) )
    zip_code = forms.CharField( widget= forms.TextInput( attrs={'placeholder' : ' Zip / Postal Code ' } ) )
    city = forms.CharField( widget= forms.TextInput( attrs={'placeholder' : ' City ' } ) )
    state = forms.CharField( widget= forms.TextInput( attrs={'placeholder' : ' State ' } ) )
    country = forms.CharField( widget= forms.TextInput( attrs={'placeholder' : ' Country ' } ) )
    note = forms.Textarea()
    user = forms.CharField(required=False)

    class Meta:

        fields = ('__all__')
        model = Order