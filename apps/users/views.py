from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import get_user_model, authenticate

from apps.users.forms import CustomUserRegistrationModelForm, \
    CustomUserSignInForm

CustomUser = get_user_model()


def user_register_view(request):
    if request.method == 'GET':
        response = render(request, 'user-registration.html')
        return response
    elif request.method == 'POST':
        new_user_data = request.POST  # type dictionary  example: {'first_name': 'Акбар', 'email': 'adsj@mald.ci'}
        user_form = CustomUserRegistrationModelForm(new_user_data)
        user_data_is_valid = user_form.is_valid()
        if user_data_is_valid:
            CustomUser.objects.create_user(email=user_form.data['email'], password=user_form.data['password'],
                                           first_name=user_form.data['first_name'], last_name=user_form.data['last_name'],
                                           age=user_form.data['age'])
            # здесь происходит запись нового пользователя в БД
            return HttpResponse('Поздравляю Вы успешно зарегистрировались')
        else:
            # говорим что данные ввели не корректно
            return HttpResponse(f'У вас некорректно заполнена форма {user_form.errors}')


def user_sign_in_view(request):
    if request.method == 'POST':
        sign_in_data = request.POST
        user_form = CustomUserSignInForm(sign_in_data)
        if user_form.is_valid():
            try:
                user = CustomUser.objects.get(email=user_form.data['email'])
            except CustomUser.DoesNotExist:
                return HttpResponse('Не существует такого пользователя')
            else:  # else сработает только тогда, когда успешно сработает try
                if user.check_password(user_form.data['password']):
                    # TODO: доделать процесс аутентификации, есть нюанс
                    authenticate(email=user_form.data['email'],
                                 password=user_form.data['password'])
                    return HttpResponse('Вы успешно авторизались/залогинились')
                else:
                    return HttpResponse('Неправильный пароль')
        else:
            return HttpResponse(f'У вас некорректно заполнена форма {user_form.errors}')
    if request.method == 'GET':
        return render(request, 'user-sign-in.html')
