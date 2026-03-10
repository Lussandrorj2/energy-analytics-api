import re
from django.core.exceptions import ValidationError

class LetterNumberPasswordValidator:

    def validate(self, password, user=None):

        if not re.search(r'[A-Za-z]', password):
            raise ValidationError(
                "A senha precisa ter pelo menos uma letra."
            )

        if not re.search(r'[0-9]', password):
            raise ValidationError(
                "A senha precisa ter pelo menos um número."
            )

    def get_help_text(self):
        return "Sua senha deve ter pelo menos 8 caracteres contendo letras e números."