from .models import CriptoModel
from .views import CriptoView


class CriptoController:
    def __init__(self):
        self.modelo = CriptoModel()
        self.vista = CriptoView()


    def coo
