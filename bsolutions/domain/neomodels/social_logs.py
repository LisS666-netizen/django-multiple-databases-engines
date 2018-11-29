from datetime import datetime

from django_neomodel import DjangoNode
from neomodel import StructuredRel, StringProperty, DateTimeProperty, UniqueIdProperty
from neomodel.relationship_manager import RelationshipTo


class InteraccionRel(StructuredRel):
    fecha = DateTimeProperty(default=datetime.utcnow)
    mensaje = StringProperty()


class BeaconNode(DjangoNode):
    uid = UniqueIdProperty()
    creada = DateTimeProperty(default=datetime.utcnow)

    class Meta:
        app_label = 'logs'


class PersonaNode(DjangoNode):
    uid = UniqueIdProperty()
    nombre = StringProperty()
    creada = DateTimeProperty(default=datetime.utcnow)
    beacons = RelationshipTo('BeaconNode', 'INTERACCION', model=InteraccionRel)

    class Meta:
        app_label = 'logs'
