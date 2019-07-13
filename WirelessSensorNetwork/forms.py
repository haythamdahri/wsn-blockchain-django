from django import forms

from WirelessSensorNetwork.blockchain import Blockchain

accounts = Blockchain.get_blockchain_accounts()

class SearchForm(forms.Form):
    search = forms.CharField(widget=forms.TextInput(attrs={
                             'class': 'form-control mr-sm-2',
                              'placeholder': 'Search a node address',
                               'aria-label': 'Search'}),
                               required = True,
                               max_length = 255)

class LoginForm(forms.Form):
    address = forms.CharField(widget=forms.TextInput(attrs={
                             'class': 'form-control',
                              'placeholder': 'Fill your ethereum address',}),
                               required = True,
                               max_length = 255)

class TransactionForm(forms.Form):
    data = forms.CharField(required=True, widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "Data..."}))


