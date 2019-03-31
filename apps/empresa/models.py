from django.db import models
from apps.core.models import UUIDModel
from django.utils.translation import gettext as _


class Entidad(UUIDModel):
    PERSONA = "PER"
    EMPRESA = "EMP"
    ORGANIZ = "ORG"
    ENTITY_TYPES = (
        (PERSONA, _("Persona")),
        (EMPRESA, _("Empresa")),
        (ORGANIZ, _("Organización")),
    )
    TD_DNI = "DNI"
    TD_RUC = "RUC"
    DOCUMENT_TYPES = (
        (TD_DNI, _("DNI - Documento nacional de identidad")),
        (EMPRESA, _("RUC - Registro único tributario")),
    )

    e_type = models.CharField(
        _("Tipo de entidad"), choices=ENTITY_TYPES, max_length=3)
    d_type = models.CharField(
        _("Tipo Documento"), choices=DOCUMENT_TYPES, max_length=3)
    document_number = models.CharField(
        _("Número de documento"), max_length=32, unique=True)


class EntidadCliente(models.Model):
    exiled = models.BooleanField(_("Exiliado"), default=False)
    customer = models.ForeignKey("cliente.Cliente", on_delete=models.CASCADE)
    entity = models.ForeignKey('empresa.Entidad', on_delete=models.CASCADE)
    exile_reason = models.TextField(_("Razón de exilio"))
