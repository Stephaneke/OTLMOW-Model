# coding=utf-8
from abc import abstractmethod


# Generated with OTLClassCreator. To modify: extend, do not edit
from UnitTests.TestClasses.Classes.ImplementatieElement.RelatieObject import RelatieObject


class NietDirectioneleRelatie(RelatieObject):
    """Een abstracte die relaties groepeert waarbij de richting semantisch niet gedefinieerd is."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#NietDirectioneleRelatie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()
