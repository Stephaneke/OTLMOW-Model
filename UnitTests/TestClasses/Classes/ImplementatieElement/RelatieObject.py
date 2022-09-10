# coding=utf-8
from abc import abstractmethod


# Generated with OTLClassCreator. To modify: extend, do not edit
from UnitTests.TestClasses.Classes.ImplementatieElement.AIMDBStatus import AIMDBStatus
from otlmow_model.BaseClasses.AttributeInfo import AttributeInfo
from otlmow_model.BaseClasses.DavieRelatieAttributes import DavieRelatieAttributes
from otlmow_model.BaseClasses.OTLObject import OTLObject


class RelatieObject(AIMDBStatus, AttributeInfo, DavieRelatieAttributes, OTLObject):
    """Abstracte die de relaties voorziet van gemeenschappelijk eigenschappen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#RelatieObject'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        AIMDBStatus.__init__(self)
        AttributeInfo.__init__(self)
        DavieRelatieAttributes.__init__(self)
        OTLObject.__init__(self)
