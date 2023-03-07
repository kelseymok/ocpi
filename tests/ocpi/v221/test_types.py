from ocpi.v221.types import *
from test_utils import validator


class TestTypes:
    def test_geo_location(self):
        geolocation = GeoLocation(latitude="50.770774", longitude="-126.104965")
        assert validator(geolocation) is None

    def test_cdr_token(self):
        cdr_token = CdrToken(
            uid="64a0a89d-6252-4fbe-a04a-50695ba7351e",
            type=TokenType.rfid,
            contract_id="704ad85f-fa58-4cfc-8aa4-638619a0dfcc"
        )
        assert validator(cdr_token) is None

    def test_cdr_location(self):
        cdr_location = CdrLocation(
            id="LOC1",
            name="Gent Zuid",
            address="F.Rooseveltlaan 3A",
            city="Gent",
            postal_code="9000",
            country="BEL",
            coordinates=GeoLocation(latitude="3.729944", longitude="51.047599"),
            evse_uid="3256",
            evse_id="BE*BEC*E041503003",
            connector_id="1",
            connector_standard=ConnectorType.iec_62196_t2,
            connector_format=ConnectorFormat.socket,
            connector_power_type=PowerType.ac_1_phase
        )
        assert validator(cdr_location) is None

    def test_display_text(self):
        display_text = DisplayText(
            language="en",
            text="2.00 euro p/hour including VAT."
        )
        assert validator(display_text) is None

    def test_url(self):
        url = URL(url="https://company.com/tariffs/13")
        assert validator(url) is None

    def test_price(self):
        price = Price(
            excl_vat=4.00,
            incl_vat=4.40
        )
        assert validator(price) is None

    def test_tariff_restrictions(self):
        tariff_restrictions = TariffRestrictions(
            min_current=32.00,
            day_of_week=[DayOfWeek.monday, DayOfWeek.tuesday, DayOfWeek.wednesday, DayOfWeek.thursday, DayOfWeek.friday]
        )
        assert validator(tariff_restrictions) is None

    def test_price_component(self):
        data = {
            "type": "ENERGY",
            "price": 0.00,
            "vat": 20.0,
            "step_size": 1
        }
        price_component = PriceComponent(**data)
        assert validator(price_component) is None

    def test_tariff_element(self):
        data = {
            "price_components": [{
                "type": "ENERGY",
                "price": 0.00,
                "vat": 20.0,
                "step_size": 1
            }],
            "restrictions": {
                "max_duration": 1800
            }
        }

        tariff_element = TariffElement(**data)
        assert validator(tariff_element) is None

    def test_energy_source(self):
        data = {
            "source": "GENERAL_GREEN",
            "percentage": 35.9
        }
        energy_source = EnergySource(**data)
        assert validator(energy_source) is None

    def test_environmental_impact(self):
        data = {
            "category": "CARBON_DIOXIDE",
            "amount": 372
        }
        environmental_impact = EnvironmentalImpact(**data)
        assert validator(environmental_impact) is None

    def test_energy_mix(self):
        data = {
            "is_green_energy": False,
            "energy_sources": [
                {"source": "GENERAL_GREEN",  "percentage": 35.9},
                {"source": "GAS", "percentage": 6.3},
                {"source": "COAL", "percentage": 33.2},
                {"source": "GENERAL_FOSSIL", "percentage": 2.9},
                {"source": "NUCLEAR", "percentage": 21.7}
            ],
            "environ_impact": [
                {"category": "NUCLEAR_WASTE", "amount": 0.0006},
                {"category": "CARBON_DIOXIDE", "amount": 372}
            ],
            "supplier_name":       "E.ON Energy Deutschland",
            "energy_product_name": "E.ON DirektStrom eco"
        }
        energy_mix = EnergyMix(**data)
        assert validator(energy_mix) is None

    def test_tariff(self):
        data = {
            "country_code": "DE",
            "party_id": "ALL",
            "id": "1",
            "currency": "EUR",
            "type": "REGULAR",
            "elements": [
                {
                    "price_components": [
                    {
                      "type": "ENERGY",
                      "price": 0.20,
                      "vat": 20.0,
                      "step_size": 1
                    }
                    ],
                    "restrictions": {
                        "max_power": 16.00
                    }
                },
                {
                    "price_components": [
                        {
                        "type": "ENERGY",
                        "price": 0.35,
                        "vat": 20.0,
                        "step_size": 1
                        }
                    ],
                    "restrictions": {
                        "max_power": 32.00
                    }
                },
                {
                    "price_components": [
                        {
                            "type": "ENERGY",
                            "price": 0.50,
                            "vat": 20.0,
                            "step_size": 1
                        }
                    ]
                }
            ],
            "last_updated": "2018-12-05T12:01:09Z"
        }
        tariff = Tariff(**data)
        assert validator(tariff) is None

    def test_cdr_dimension(self):
        data = {
            "type": "ENERGY",
            "volume": 120
        }
        cdr_dimension = CdrDimension(**data)
        assert validator(cdr_dimension) is None

    def test_charging_period(self):
        data = {
            "start_date_time": "2015-06-29T22:39:09Z",
            "dimensions": [
                {
                    "type": "ENERGY",
                    "volume": 120
                },
                {
                    "type": "MAX_CURRENT",
                    "volume": 30
                }
            ],
            "tariff_id": "12"
        }
        charging_period = ChargingPeriod(**data)
        assert validator(charging_period) is None

    def test_signed_value(self):
        data = {
            "nature": "some-nature",
            "plain_data": "some-plain-data",
            "signed_data": "some-signed-data"
        }
        signed_value = SignedValue(**data)
        assert validator(signed_value) is None

    def test_signed_data(self):
        data = {
            "encoding_method": "some-encoding-method",
            "url": "https://example.com",
            "signed_values": [
                {
                    "nature": "some-nature",
                    "plain_data": "some-plain-data",
                    "signed_data": "some-signed-data"
                }
            ]
        }
        signed_data = SignedData(**data)
        assert validator(signed_data) is None

    def test_cdr(self):
        data = {
            "country_code": "BE",
            "party_id": "BEC",
            "id": "12345",
            "start_date_time": "2015-06-29T21:39:09Z",
            "end_date_time": "2015-06-29T23:37:32Z",
            "cdr_token": {
                "uid": "012345678",
                "type": "RFID",
                "contract_id": "DE8ACC12E46L89"
            },
            "auth_method": "WHITELIST",
            "cdr_location": {
                "id": "LOC1",
                "name": "Gent Zuid",
                "address": "F.Rooseveltlaan 3A",
                "city": "Gent",
                "postal_code": "9000",
                "country": "BEL",
                "coordinates": {
                    "latitude": "3.729944",
                    "longitude": "51.047599"
                },
                "evse_uid": "3256",
                "evse_id": "BE*BEC*E041503003",
                "connector_id": "1",
                "connector_standard": "IEC_62196_T2",
                "connector_format": "SOCKET",
                "connector_power_type": "AC_1_PHASE"
                },
            "currency": "EUR",
            "tariffs": [
                {
                    "country_code": "BE",
                    "party_id": "BEC",
                    "id": "12",
                    "currency": "EUR",
                    "elements": [
                        {
                            "price_components": [
                                {
                                  "type": "TIME",
                                  "price": 2.00,
                                  "vat": 10.0,
                                  "step_size": 300
                                }
                            ]
                        }
                    ],
                    "last_updated": "2015-02-02T14:15:01Z"
                }
            ],
            "charging_periods": [
                {
                    "start_date_time": "2015-06-29T21:39:09Z",
                    "dimensions": [
                        {
                            "type": "TIME",
                            "volume": 1.973
                        }
                    ],
                    "tariff_id": "12"
                }
            ],
            "total_cost": {
                "excl_vat": 4.00,
                "incl_vat": 4.40
            },
            "total_energy": 15.342,
            "total_time": 1.973,
            "total_time_cost": {
                "excl_vat": 4.00,
                "incl_vat": 4.40
            },
            "last_updated": "2015-06-29T22:01:13Z"
        }
        cdr = CDR(**data)
        assert validator(cdr) is None