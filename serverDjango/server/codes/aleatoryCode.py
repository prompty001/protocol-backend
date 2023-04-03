import pyotp

from django.core.mail import send_mail

def totpGenerator() -> str:
    totp = pyotp.TOTP('base32secret3232')
    totp.interval = 300

    print(totp.now())
    return totp.now()


def emailSender() -> None:
        send_mail(
            'Código de Confirmação - UFPA Wireless',
            totpGenerator(),
            'djangoserver@ufpa.br',
            ['bob@gmail.com'],
        )


def validateTotp(clientCode) -> bool:
    totp = pyotp.TOTP('base32secret3232')
    totp.interval = 300

    return True if totp.verify(clientCode) is True else False