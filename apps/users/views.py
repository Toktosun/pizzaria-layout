from django.shortcuts import render

from apps.users.forms import CustomUserRegistrationModelForm


def user_register_view(request):
    if request.method == 'GET':
        response = render(request, 'user-registration.html')
        return response
    elif request.method == 'POST':
        new_user_data = request.POST  # type dictionary  example: {'first_name': 'Акбар', 'email': 'adsj@mald.ci'}
        user_form = CustomUserRegistrationModelForm(new_user_data)
        user_data_is_valid = user_form.is_valid()
        if user_data_is_valid:
            # здесь происходит запись нового пользователя в БД
            pass
        else:
            # говорим что данные ввели не корректно
            pass
