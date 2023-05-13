from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.shortcuts import render, redirect

from accounts.consumers import ChatConsumer
from accounts.models import Interest, User
from accounts.utilities import get_user_from_email_or_mobile_or_employee_code


def index(request):
    return render(request, 'login.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['Uname']
        password = request.POST['Pass']
        username = get_user_from_email_or_mobile_or_employee_code(username)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            messages.success(request, f' welcome {username.name} !!')
            user_interests = request.user.interest.all()
            same_interest_users = User.objects.filter(interest__in=user_interests).exclude(id=request.user.id)
            return render(request, 'chatPage.html', {'same_interest_users': same_interest_users})
        else:
            messages.info(request, f'account done not exit plz sign in')
            return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        print(request.POST)
        name = request.POST['name']
        phone = request.POST['phone_no']
        email = request.POST['email']
        password = request.POST['pass']
        interest = dict(request.POST)['interest']
        gender = request.POST['gender']
        country = request.POST['country']
        user = User.objects.create_user(name=name, phone_no=phone, password=password, email=email, gender=gender,
                                        country=country)
        for i in interest:
            user.interest.add(i)
        user.save()
        print(user.interest)
        return redirect('/')
    else:
        interest = Interest.objects.all()
        return render(request, 'signup.html', context={'interest': interest})


def logout_view(request):
    logout(request)
    return redirect('/')

def chatPage(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("/")
    context = {}
    print('something')
    return render(request, "chatPage.html", context)