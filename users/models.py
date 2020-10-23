from django.db import models

#importamos modelos user
#from django.contrib.auth.models import User
#importamos la clase AbstractUser
from django.contrib.auth.models import AbstractUser

#modelo User
class User(AbstractUser):
    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)


# Create your models here. agregar nuevas funcionalidades, moldelo que hereda de otro
#NO genera una nueva tabla en la base de datos
#heredera del modelo user
class Customer(User):
    class Meta:
        proxy = True
#retornar todos los productos adquiridos por el cliente
    def get_products(self):
        #retornamos una lista vacia
        return []

#si tenemos la necesidad de agregar nuevos campos y atrubutos osbre el modelo user, generamos una relacion uno a uno
#creamos un nuevo modelo
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)#CUANDO UN USUARIO SEA ELIMINADO TAMBIEN SE ELIMINE EL REGISTRO PROFILE
    bio = models.TextField()


#si no es sufiencte para nuestras necesedidades, tenemos que sobrescribir el modelo user, nos apoyamos
#de la clase AbstractUser ->username, first_name,last_name, email, password o AbstractBaseUser -> id, passdowrd, last_login
