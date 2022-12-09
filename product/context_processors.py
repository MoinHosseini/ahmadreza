from .models import material
import datetime

def access_mina(request):
    """
      The context processor must return a dictionary.
    """
    # w = messages.objects.latest('-id')


    mina = material.objects.latest('-id') #query the latest banner image
    return {'mina':mina} 