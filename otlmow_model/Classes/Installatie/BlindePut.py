# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.Abstracten.Put import Put
from otlmow_model.Classes.ImplementatieElement.AIMObject import AIMObject
from otlmow_model.Datatypes.KlPutMateriaal import KlPutMateriaal
from otlmow_model.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class BlindePut(AIMObject, Put, VlakGeometrie):
    """Een put waar de riolering op aangesloten is maar die niet meer zichtbaar is."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#BlindePut'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        Put.__init__(self)
        VlakGeometrie.__init__(self)

        self._materiaal = OTLAttribuut(field=KlPutMateriaal,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#BlindePut.materiaal',
                                       definition='Het materiaal waaruit de blinde put is vervaardigd.',
                                       owner=self)

    @property
    def materiaal(self) -> str:
        """Het materiaal waaruit de blinde put is vervaardigd."""
        return self._materiaal.get_waarde()

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)
