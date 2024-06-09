from django.shortcuts import redirect, render,HttpResponse
from .chapa import payment
from django.contrib import messages
from django.template import loader
# Create your views here.
def pay(request):
    if request.method == 'POST':
        # Get form data
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        amount = request.POST.get('amount')
        email = request.POST.get('email')
        
        ret = payment(first_name, last_name, phone, amount, email)
        # print(ret)
        if ret['status'] == 'success':
            checkout_url = ret['data']['checkout_url']
       
            return HttpResponse(loader.render_to_string('new_tab.html', {'checkout_url': checkout_url}))
        else:
            error_message = ret['message']
            messages.error(request, error_message)
        # return render(request, 'success.html')
    
    # If GET request, render the payment form
    return render(request, 'pay.html')
