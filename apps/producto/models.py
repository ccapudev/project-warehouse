from django.db import models
from apps.core.models import UUIDModel
from django.utils.translation import gettext as _


class ProductoLinea(UUIDModel):
    """
    Ejemplo: Calzado, Cosmeticos, Consumibles
    """
    pass


class ProductoClase(UUIDModel):
    """
    Representa a una clase producto que va ligada a una linea
    Ejemplo:
        Botas => Calzado,
        Zapatos => Calzado,
        Sandalias => Calzado,
        Labiales => Cosmeticos,
        Polvos => Cosmeticos,
        Pinta uñas => Cosmeticos,
        Gaseosas => Consumibles,
        Galletas => Consumibles,
        Papa => Consumibles,
    """
    linea = models.ForeignKey('producto.ProductoLinea', null=True,
                              on_delete=models.SET_NULL)


class Proveedor(UUIDModel):
    ruc = models.CharField(_("RUC"), max_length=32, unique=True)


class Producto(UUIDModel):
    sku = models.CharField("SKU", max_length=64)