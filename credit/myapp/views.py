from django.shortcuts import render, redirect
from .form import CreditCardApplicationForm




def credit_card_application(request):
    if request.method == "POST":
        form = CreditCardApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Redirect to a success page
    else:
        form = CreditCardApplicationForm()
    return render(request, 'creditcard/application_form.html', {'form': form})
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # ✅ Make sure this template exists
