from django.contrib.auth import get_user_model


def get_user_from_email_or_mobile_or_employee_code(username):
    user_model = get_user_model()
    mobile_user = user_model.objects.filter(phone_no=username).first()
    email_user = user_model.objects.filter(email=username).first()
    if email_user:
        user = email_user
    else:
        user = mobile_user
    return user
