# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEGCTestType(KeuzelijstField):
    """Het test type van het geluidswerend scherm."""
    naam = 'KlLEGCTestType'
    label = 'Test type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEGCTestType'
    definition = 'Het test type van het geluidswerend scherm.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEGCTestType'
    options = {
        'geluidsabsorptie': KeuzelijstWaarde(invulwaarde='geluidsabsorptie',
                                             label='geluidsabsorptie',
                                             status='ingebruik',
                                             definitie='Proef : De ééngetalsaanduiding als waarde voor de geluidsabsorptie.',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCTestType/geluidsabsorptie'),
        'luchtgeluidsisolatie': KeuzelijstWaarde(invulwaarde='luchtgeluidsisolatie',
                                                 label='luchtgeluidsisolatie',
                                                 status='ingebruik',
                                                 definitie='Proef : De ééngetalsaanduiding voor luchtgeluidsisolatie.',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCTestType/luchtgeluidsisolatie')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

