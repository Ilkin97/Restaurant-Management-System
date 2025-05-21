from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_email_task(subject, message, recipient_list):
    """
    Sends an email asynchronously using Celery.

    This task is executed in the background by Celery, which allows the email to be sent without blocking 
    the main application. It uses Django's send_mail function to send the email to the specified recipients.

    Args:
        subject (str): The subject line of the email.
        message (str): The body content of the email.
        recipient_list (list): A list of email addresses to which the email will be sent.

    Returns:
        None
    """
    # Sends an email using the send_mail function from Django, using the default 'from' email set in settings
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)
