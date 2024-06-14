from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, HttpResponse
from django.contrib import messages
from django.template import loader
from file.models import Course, PurchasedCourse
from .chapa import payment

@login_required
def pay(request):
    if request.method == 'POST':
        course_name = request.POST.get('course_name')
        course = Course.objects.get(name=course_name)

        # Retrieving user information from the logged-in user
        first_name = request.user.first_name
        last_name = request.user.last_name
        email = request.user.email
        phone = request.POST.get('phone')
        amount = course.price

        # Proceed with payment processing
        ret = payment(first_name, last_name, phone, amount, email)
        if ret['status'] == 'success':
            checkout_url = ret['data']['checkout_url']
       
            return HttpResponse(loader.render_to_string('new_tab.html', {'checkout_url': checkout_url})) 
        else:
            error_message = ret['message']
            messages.error(request, error_message)

    # If GET request, render the pay.html template
    course_name = request.GET.get('course_name')
    course = Course.objects.get(name=course_name)
    return render(request, 'pay.html', {'course': course, 'user': request.user})
