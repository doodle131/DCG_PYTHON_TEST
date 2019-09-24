from django import forms

from python_test.models import Client


class ClientForm(forms.ModelForm):
    """
    -if we create a form using Form class, then it is an unbound form
    -if we create a form using ModelForm, then the form is bound to a particular model
    -a bound form knows where to store the data unlike an unbound form
    """

    class Meta:  # the name Meta defines that this data contains metadata for the form created above
        # here we inform the model to which this form is bound and where the data input to this form will be store
        model = Client
        fields = ['name']
        # the 'fields' var includes the fields that the form will include from the model
