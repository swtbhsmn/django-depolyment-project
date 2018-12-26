from django.shortcuts import render
from . import forms
# Create your views here.
def index(request):
    return render(request,'basicapp/index.html')

def form_name_view(request):
    form=forms.FormName()



    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("Successfully")
            print("NAME"+form.cleaned_data['firstname'])
            print("EMAIL"+form.cleaned_data['email'])
            print("TEXT"+form.cleaned_data['text'])
    return render(request,'basicapp/d_form.html',{'form':form})