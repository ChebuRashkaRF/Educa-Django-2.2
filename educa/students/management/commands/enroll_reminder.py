import datetime
from django.conf import settings
from django.core.management.base import BaseCommand
from django.core.mail import send_mass_mail
from django.contrib.auth.models import User
from django.db.models import Count


class Command(BaseCommand):
    """
    Отправляет напоминание по электронной почте пользователям,
    зарегистрировавшимся более N дней, но еще не записанным
    на какие-либо курсы

    """

    help = 'Отправляет напоминание по электронной почте \
        пользователям, зарегистрировавшимся более N дней,\
        но еще не записанным на какие-либо курсы'

    def add_arguments(self, parser):
        parser.add_argument('--days', dest='days', type=int)

    def handle(self, *args, **options):
        emails = []
        subject = 'Записаться на курс'
        date_joined = datetime.date.today() - \
            datetime.timedelta(days=options['days'])
        users = User.objects.annotate(course_count=Count('courses_joined'))\
            .filter(course_count=0, date_joined__lte=date_joined)
        for user in users:
            message = f'Уважаемый {user.first_name},\n\n Мы\
                заметили, что вы еще не записались\
                ни на какие курсы. Чего же ты ждешь?'
            emails.append((subject,
                           message,
                           settings.DEFAULT_FROM_EMAIL,
                           [user.email]))
        send_mass_mail(emails)
        self.stdout.write(f'Отправлено {len(emails)} напоминаний')
