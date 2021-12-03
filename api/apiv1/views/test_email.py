from django.core.mail import send_mail
from django.http import HttpResponse

def sendmail(request):
    subject = ' タイトル '
    message = ' これはメッセージです。'

    to = ['Heitorhirose@gmail.com']
    send_mail(subject, message, None, to)

    return HttpResponse('メール送信完了')

