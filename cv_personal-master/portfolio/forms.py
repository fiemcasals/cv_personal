from django import forms

class ContactForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=120, widget=forms.TextInput(attrs={"placeholder":"Tu nombre"}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={"placeholder":"tucorreo@dominio.com"}))
    mensaje = forms.CharField(label="Mensaje", widget=forms.Textarea(attrs={"rows":6, "placeholder":"Escribe tu consulta aquí..."}))
