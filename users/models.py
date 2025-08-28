from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """
    Usuário customizado.
    Podemos adicionar campos extras depois (telefone, endereço etc.)
    """
    pass
