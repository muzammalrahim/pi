from django import forms
from django.forms import ModelForm
from xx.models import *
from django.core.exceptions import ValidationError
from django.core import validators

LANGUAGE_CHOICES = [
    ('nl', 'Dutch'),
    ('en', 'English'),
]
COUNTRIES = [
    ('nl', 'Netherlands'),
    ('be', 'Belgium'),
    ('ae', 'United Arabic Emirates'),
    ('uk', 'United Kingdom'),
    ('us', 'United States'),
]
ROLES = [
    ('admin', 'admin'),
    ('regular', 'regular'),
]
DHCP_FIXED = [
    ('dhcp', 'dhcp'),
    ('fixed', 'fixed'),
]


def emptyy(sstr):
    try:
        return len(sstr)
    except:
        return 0


class CliCommandForm(forms.Form):
    def clean(self):
        baviaan = 'aap'

    # code = forms.CharField(required=True, max_length=18)
    code = forms.CharField(
        required=True,
        max_length=18,
        widget=forms.TextInput(

            attrs={

                "placeholder": "code",
                "class": "form-control"
            }
        ))
    # command = forms.CharField(required=True, widget=forms.Textarea, max_length=500)
    command = forms.CharField(
        required=True,
        max_length=500,
        widget=forms.Textarea(

            attrs={

                "placeholder": "command ",
                "class": "form-control"
            }
        ))
    # remark = forms.CharField(required=False, widget=forms.Textarea, max_length=500)
    remark = forms.CharField(
        required=False,
        max_length=500,
        widget=forms.Textarea(

            attrs={

                "placeholder": "add remarks here  ",
                "class": "form-control"
            }
        ))

    # last_updated = forms.DateTimeField(required=False, disabled=True)
    last_updated = forms.CharField(
        required=False,
        disabled=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))
    # created = forms.DateTimeField(required=False, disabled=True)
    created = forms.CharField(
        required=False,
        disabled=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )


class CliCommandNewForm(forms.Form):
    def clean(self):
        code = self.cleaned_data.get('code')
        try:
            code_exists = True
            clicommand = CliCommand.objects.get(code=code)
        except:
            code_exists = False
        if code_exists:
            raise forms.ValidationError("This code exists already.")
            return code

    # code = forms.CharField(max_length=18)
    code = forms.CharField(
        max_length=18,
        widget=forms.TextInput(

            attrs={

                "placeholder": "code",
                "class": "form-control"
            }
        ))

    # command = forms.CharField(required=True, widget=forms.Textarea, max_length=500)
    command = forms.CharField(
        required=True,
        max_length=500,
        widget=forms.Textarea(

            attrs={

                "placeholder": "command ",
                "class": "form-control"
            }
        ))
    # remark = forms.CharField(required=False, widget=forms.Textarea, max_length=500)
    remark = forms.CharField(
        required=False,
        max_length=500,
        widget=forms.Textarea(

            attrs={

                "placeholder": "add remarks here  ",
                "class": "form-control"
            }
        ))
    # last_updated = forms.DateTimeField(required=False, disabled=True)
    last_updated = forms.CharField(
        required=False,
        disabled=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))
    # created = forms.DateTimeField(required=False, disabled=True)

    created = forms.CharField(
        required=False,
        disabled=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )


class MyAccountForm(forms.Form):
    class Meta:
        model = Xuser
        fields = ('__all__')

    def clean(self):
        baviaan = self.cleaned_data.get('name')

    # name = forms.CharField(required=False)
    name = forms.CharField(
        required=False,
        widget=forms.TextInput(

            attrs={

                "placeholder": "name",
                "class": "form-control"
            }
        ))

    # userid = forms.CharField(required=False, disabled=True, label="Userid")
    userid = forms.CharField(
        required=False,
        disabled=True,
        label="Userid",
        widget=forms.TextInput(

            attrs={

                "placeholder": "user id ",
                "class": "form-control"
            }
        ))
    # email = forms.EmailField(required=False)
    email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))
    # support_end_date = forms.DateTimeField(required=False, disabled=True)
    support_end_date = forms.CharField(
        required=False,
        disabled=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))
    # last_login = forms.DateTimeField(required=False, disabled=True)
    last_login = forms.CharField(
        required=False,
        disabled=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))

    # last_updated = forms.DateTimeField(required=False, disabled=True)
    last_updated = forms.CharField(
        required=False,
        disabled=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))

    # created = forms.DateTimeField(required=False, disabled=True)
    created = forms.CharField(
        required=False,
        disabled=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))
    # id = forms.IntegerField(required=False, disabled=True)
    id = forms.IntegerField(
        required=False,
        disabled=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))


class PasswordForm(forms.Form):
    class Meta:
        model = Xuser
        fields = ('__all__')

    def clean(self):
        password = self.cleaned_data.get('password')
        confirm = self.data.get('confirm')
        if password != confirm:
            raise forms.ValidationError("Passwords dont match")
            return password

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))

    # password = forms.CharField(required=True, widget=forms.PasswordInput)
    # confirm = forms.CharField(required=True, widget=forms.PasswordInput)
    confirm = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Confirm Password",
                "class": "form-control"
            }
        ))


class NewNetworkForm(forms.Form):
    class Meta:
        model = NewNetwork
        fields = ('__all__')
        # fields = ('newssid','psk')

    def clean(self):
        newssid = self.cleaned_data.get('newssid')
        psk = self.cleaned_data.get('psk')
        wlan_dhcp_fixed = self.cleaned_data.get('wlan_dhcp_fixed')
        wlan_static_IP = self.cleaned_data.get('wlan_static_IP')
        wlan_router = self.cleaned_data.get('wlan_router')
        wlan_network_domain = self.cleaned_data.get('wlan_network_domain')
        eth_dhcp_fixed = self.cleaned_data.get('eth_dhcp_fixed')
        eth_static_IP = self.cleaned_data.get('eth_static_IP')
        eth_router = self.cleaned_data.get('eth_router')
        eth_network_domain = self.cleaned_data.get('eth_network_domain')
        # if psk == None:
        #    psk = ''
        # if newssid == None:
        #    newssid = ''
        # if psk != None and newssid == None :
        if len(psk) > 0 and len(newssid) == 0:
            raise forms.ValidationError("You cant enter a password without SSID")
            return newssid
        if wlan_dhcp_fixed == 'fixed' and (
                len(wlan_static_IP) == 0 or len(wlan_router) == 0 or len(wlan_network_domain) == 0):
            # if wlan_dhcp_fixed == 'fixed' and (emptyy(wlan_static_IP) or emptyy(wlan_router) or emptyy(wlan_network_domain)):
            # if wlan_dhcp_fixed == 'fixed' and (wlan_static_IP == None  or wlan_router == None  or wlan_network_domain == None):
            raise forms.ValidationError("For fixed wifi IP, enter static IP, router and domain")
            return wlan_dhcp_fixed
        # if eth_dhcp_fixed == 'fixed' and (emptyy(eth_static_IP) or emptyy(eth_router) or emptyy(eth_network_domain)):
        if eth_dhcp_fixed == 'fixed' and (
                len(eth_static_IP) == 0 or len(eth_router) == 0 or len(eth_network_domain) == 0):
            raise forms.ValidationError("For fixed wired IP, enter static IP, router and domain")
            # self._errors['eth_dhcp_fixed'] = "Passwords must match."
            return eth_dhcp_fixed

    newssid = forms.CharField(required=False, label="SSID new or to update")
    psk = forms.CharField(required=False, label="WiFi password", min_length=8)
    wlan_dhcp_fixed = forms.TypedChoiceField(choices=DHCP_FIXED)
    wlan_static_IP = forms.GenericIPAddressField(required=False)
    wlan_router = forms.GenericIPAddressField(required=False)
    wlan_network_domain = forms.GenericIPAddressField(required=False)
    eth_dhcp_fixed = forms.TypedChoiceField(choices=DHCP_FIXED)
    eth_static_IP = forms.GenericIPAddressField(required=False)
    eth_router = forms.GenericIPAddressField(required=False)
    eth_network_domain = forms.GenericIPAddressField(required=False)


class RegisterForm(forms.Form):
    class Meta:
        model = Xuser
        fields = ('__all__')

    def clean(self):
        password = self.cleaned_data.get('password')
        confirm = self.data.get('confirm')
        if password != confirm:
            raise forms.ValidationError("Passwords dont match")
            return password

    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "name",
                "class": "form-control"
            }
        ))
    # name = forms.CharField(required=True,min_length=5)
    userid = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "userid",
                "class": "form-control"
            }
        ))
    # userid = forms.CharField(required=True, min_length=5)
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))
    # email = forms.EmailField(required=True)
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))
    # password = forms.CharField(required=True, widget=forms.PasswordInput, min_length=8)
    confirm = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Confirm Password",
                "class": "form-control"
            }
        ))
    # confirm = forms.CharField(required=True, widget=forms.PasswordInput)


class RpiForm(forms.Form):
    computernr = forms.CharField(disabled=True)
    version = forms.CharField(disabled=True)
    wifiAvailableNetworks = forms.CharField(disabled=True)
    wifiKnownNetworks = forms.CharField(disabled=True)
    wifiCurrentNetwork = forms.CharField(disabled=True)
    ipAddressWlan = forms.CharField(disabled=True)
    ipAddressEth = forms.CharField(disabled=True)
    ping_response_time = forms.IntegerField(disabled=True)
    sd_card = forms.CharField(disabled=True)
    last_reboot = forms.DateTimeField(disabled=True)
    created = forms.DateTimeField(disabled=True)
    last_seen = forms.DateTimeField(disabled=True)
    id = forms.IntegerField(disabled=True)


def check_sizex(name):
    if len(name) < 2:
        raise forms.ValidationError("the name is too short")
    return name


class SettingsForm(forms.Form):
    sender = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Sender",
                "class": "form-control"
            }
        ))

    smtp_server = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "smtp server",
                "class": "form-control"
            }
        ))
    message_new_user = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "message new user",
                "class": "form-control"
            }
        ))
    free_period_in_months = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "free period in months",
                "class": "form-control"
            }

        )
    )

    # sender = forms.CharField()
    # smtp_server = forms.CharField()
    # message_new_user = forms.CharField(widget=forms.Textarea)
    # free_period_in_months = forms.IntegerField()


class XuserForm(forms.Form):
    class Meta:
        model = Xuser
        fields = ('name')
        fields = ('__all__')

    def clean2(self):
        cleaned_data = super(XuserForm, self).clean()
        name = cleaned_data.get("name")
        if len(name) < 2:
            self.add_error('name', 'name max 10')
        return cleaned_data

    def clean(self):
        # name = self.cleaned_data.get('name')
        cleaned_data = super(XuserForm, self).clean()
        name = cleaned_data.get("name")
        if len(name) < 2:
            errors = {}
            errors['name'] = ValidationError('message1', code='invalid')
            raise forms.ValidationError("Name should be at least 10 characters")
            return name

    # name = forms.CharField()
    name = forms.CharField(
        widget=forms.TextInput(

            attrs={
                "class": "form-control"
            }
        ))
    # userid = forms.CharField(disabled=True, label="Userid")
    userid = forms.CharField(
        disabled=True,
        label="Userid",
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))
    # email = forms.EmailField(required=False)
    email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))
    # password = forms.CharField(required=False, widget=forms.PasswordInput)
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))
    role = forms.TypedChoiceField(required=False, choices=ROLES)

    # failed_logins = forms.IntegerField()
    failed_logins = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))
    # support_end_date = forms.DateTimeField(disabled=True)
    support_end_date = forms.CharField(
        disabled=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))
    # last_login = forms.DateTimeField(disabled=True)
    last_login = forms.CharField(
        disabled=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))
    # last_updated = forms.DateTimeField(disabled=True)
    last_updated = forms.CharField(
        disabled=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))
    # created = forms.DateTimeField(disabled=True)
    created = forms.CharField(
        disabled=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))
    # id = forms.IntegerField(disabled=True)
    id = forms.CharField(
        disabled=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))


class XnewRpiForm(forms.Form):
    class Meta:
        model = Xuser
        fields = ('__all__')

    def clean(self):
        cleaned_data = super(XnewRpiForm, self).clean()
        computernr = cleaned_data.get("computernr")
        activation_code = cleaned_data.get("activation_code")
        try:
            newrpi = NewRpi.objects.get(computernr=computernr, activation_code=activation_code)
        except:
            errors = {}
            errors['computernr'] = ValidationError('message1', code='invalid')
            raise forms.ValidationError("I didnt find a device with these data.")
            return computernr

    computernr = forms.CharField(required=True)
    activation_code = forms.CharField(required=True)
