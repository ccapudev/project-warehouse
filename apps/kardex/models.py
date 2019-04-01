from django.db import models
from apps.core.models import UUIDModel
from django.utils.translation import gettext as _


class Kardex(UUIDModel):
    INGRESO = 'IN'
    SALIDA = 'OUT'
    TRANSACTION_TYPES = (
        (INGRESO, _("Ingreso")),
        (SALIDA, _("Salida")),
    )
    name = 'Kardex'
    almacen = models.ForeignKey("almacen.Almacen",
                                on_delete=models.SET_NULL, null=True)
    entidad = models.ForeignKey("empresa.Entidad",
                                on_delete=models.SET_NULL, null=True)
    almacen_name = models.CharField(_("Nombre de almacen"), max_length=128)
    entidad_name = models.CharField(_("Nombre de Entidad"), max_length=128)
    transaction_type = models.CharField(_("Tipo de Transacción"), max_length=5,
                                        choices=TRANSACTION_TYPES)
    tipo_documento = models.ForeignKey("almacen.TipoDocumento", null=True,
                                       verbose_name=_("Tipo Documento"),
                                       on_delete=models.SET_NULL)
    quantity = models.IntegerField(_("Cantidad"), default=0)
