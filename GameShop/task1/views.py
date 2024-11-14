from django.shortcuts import render
from task1.models import Games,Buyer
from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister



def shop(request):
    games = Games.objects.all()
    data_db = {
        'title': 'Магазин',
        'menu': menu,
        'products': games,
    }
    return render(request, 'task1/games.html', context=data_db)

def cart(request):
    return render(request, 'task1/cart.html')

def menu(request):
    return render(request, 'task1/menu.html')



def sign_up_by_django(request):
    info = ''
    Users = Buyer.objects.all()

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']


            if Buyer.objects.filter(name=username).exists():
                info = "Ошибка: пользователь уже существует."
            elif password != repeat_password:
                info = "Ошибка: пароли не совпадают."
            elif int(age) < 18:
                info = "Ошибка: возраст должен быть не менее 18 лет."
            else:



                Buyer.objects.create(name=username, balance=500.0, age=age)
                info = f"Приветствуем, {username}!"

    else:
        form = UserRegister()

    context = {'form': form, 'info': info}
    return render(request, 'task1/registration_page.html', context)


def sign_up_by_html(request):
    info={}
    users = Buyer.objects.all()

    if request.method == 'POST':

        username = request.POST.get("username")
        password = request.POST.get("password")
        repeat_password = request.POST.get("repeat_password")
        age = request.POST.get("age")

        print(f'Username:{username}')
        print(f'password:{password}')
        print(f'repeat_password:{repeat_password}')
        print(f'age:{age}')

        if password == repeat_password and int(age) >= 18 and username not in users:
            Buyer.objects.create(name=username, balance=500.0, age=age)
            return HttpResponse(f'Приветствуем, {username}!')
        else:
            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif int(age) < 18:
                info['error'] = 'Возраст должен быть старше 18 лет'
            else:
                info['error'] = 'Пользователь  уже существует'

    return render(request, 'task1/registration_page.html', {'info': info})
