from django.shortcuts import render
from .models import Course, PurchasedCourse
from django.contrib.auth.decorators import login_required

@login_required
def homepage(request):
    all_courses = Course.objects.all()
    purchased_courses = PurchasedCourse.objects.filter(user=request.user).values_list('course', flat=True)
    courses = all_courses.exclude(id__in=purchased_courses)
    purchased_courses = Course.objects.filter(id__in=purchased_courses)
    return render(request, 'home.html', {'courses': courses, 'purchased_courses': purchased_courses})

# def pay(request):
#     return render(request, 'pay.html')
@login_required
def mylist(request):
    user_courses = PurchasedCourse.objects.filter(user=request.user)
    return render(request, 'mylist.html', {'user_courses': user_courses})

def admin_page(request):
    return render(request, 'admin_page.html')

def search(request):
    query = request.GET.get('q')
    results = Course.objects.filter(name__icontains=query) if query else []
    return render(request, 'search.html', {'results': results, 'query': query})
