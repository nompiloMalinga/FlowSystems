from django import forms 
from .models import UserForm


class UserForm(forms.ModelForm):
    
   class Meta:  
        model = UserForm 
        fields = "__all__"
 
        def __init__(self, *args, **kwargs):
            super(UserForm, self).__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'form-control'  