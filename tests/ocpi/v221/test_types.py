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

    def test_version(self):
        data = {
            "version": "2.2",
            "url": "https://www.server.com/ocpi/2.1.1/"
        }
        version = Version(**data)
        assert validator(version) is None


    def test_publish_token_type(self):
        data = {
            "visual_number": "0055375624",
            "issuer": "ANWB"
        }
        publish_token_type = PublishTokenType(**data)
        assert validator(publish_token_type) is None

    def test_additional_geo_location(self):
        display_text = DisplayText(
            language="en",
            text="2.00 euro p/hour including VAT."
        )
        geolocation = AdditionalGeoLocation(latitude="50.770774", longitude="-126.104965", name=display_text)
        assert validator(geolocation) is None

    def test_status_schedule(self):
        status_schedule = StatusSchedule(
            period_begin="2023-01-01T09:00:00",
            status=Status.available
        )
        assert validator(status_schedule) is None

    def test_connector(self):
        data = {
            "id": "1",
            "standard": "IEC_62196_T2",
            "format": "CABLE",
            "power_type": "AC_3_PHASE",
            "max_voltage": 220,
            "max_amperage": 16,
            "tariff_ids": ["11"],
            "last_updated": "2015-03-16T10:10:02Z"
        }
        connector = Connector(**data)
        assert validator(connector) is None

    def test_image(self):
        image = Image(
            url="https://example.com",
            category=ImageCategory.charger,
            type="type",
            width=100,
            height=100
        )
        assert validator(image) is None

    def test_evse(self):
        data = {
            "uid": "3256",
            "evse_id": "BE*BEC*E041503001",
            "status": "AVAILABLE",
            "capabilities": [
              "RESERVABLE"
            ],
            "connectors": [
                {
                    "id": "1",
                    "standard": "IEC_62196_T2",
                    "format": "CABLE",
                    "power_type": "AC_3_PHASE",
                    "max_voltage": 220,
                    "max_amperage": 16,
                    "tariff_ids": ["11"],
                    "last_updated": "2015-03-16T10:10:02Z"
                },
                {
                    "id": "2",
                    "standard": "IEC_62196_T2",
                    "format": "SOCKET",
                    "power_type": "AC_3_PHASE",
                    "max_voltage": 220,
                    "max_amperage": 16,
                    "tariff_ids": ["13"],
                    "last_updated": "2015-03-18T08:12:01Z"
                }
            ],
            "physical_reference": "1",
            "floor_level": "-1",
            "last_updated": "2015-06-28T08:12:01Z"
        }
        evse = EVSE(**data)
        assert validator(evse) is None

    def test_business_details(self):
        data = {
            "name": "BeCharged"
        }
        business_details = BusinessDetails(**data)
        assert validator(business_details) is None

    def test_regular_hours(self):
        data = {
            "weekday": 1,
            "period_begin": "00:00",
            "period_end": "04:00"
        }
        regular_hours = RegularHours(**data)
        assert validator(regular_hours) is None

    def test_exceptional_period(self):
        data = {
            "period_begin": "00:00",
            "period_end": "04:00"
        }
        exceptional_period = ExceptionalPeriod(**data)
        assert validator(exceptional_period) is None

    def test_hours(self):
        data = {
            "twentyfourseven": False,
            "regular_hours": [
                {
                    "weekday": 1,
                    "period_begin": "00:00",
                    "period_end": "04:00"
                },
                {
                    "weekday": 2,
                    "period_begin": "00:00",
                    "period_end": "04:00"
                }
            ],
            "exceptional_openings": [
                {
                    "period_begin": "2018-12-25T05:00:00Z",
                    "period_end": "2018-12-25T06:00:00Z"
                }
            ]
        }
        hours = Hours(**data)
        assert validator(hours) is None

    def test_location(self):
        data = {
            "country_code": "BE",
            "party_id": "BEC",
            "id": "LOC1",
            "publish": True,
            "name": "Gent Zuid",
            "address": "F.Rooseveltlaan 3A",
            "city": "Gent",
            "postal_code": "9000",
            "country": "BEL",
            "coordinates": {
                "latitude": "51.047599",
                "longitude": "3.729944"
            },
            "parking_type": "ON_STREET",
            "evses": [
                {
                    "uid": "3256",
                    "evse_id": "BE*BEC*E041503001",
                    "status": "AVAILABLE",
                    "capabilities": [
                        "RESERVABLE"
                    ],
            "connectors": [
                {
                    "id": "1",
                    "standard": "IEC_62196_T2",
                    "format": "CABLE",
                    "power_type": "AC_3_PHASE",
                    "max_voltage": 220,
                    "max_amperage": 16,
                    "tariff_ids": ["11"],
                    "last_updated": "2015-03-16T10:10:02Z"
                },
                {
                    "id": "2",
                    "standard": "IEC_62196_T2",
                    "format": "SOCKET",
                    "power_type": "AC_3_PHASE",
                    "max_voltage": 220,
                    "max_amperage": 16,
                    "tariff_ids": ["13"],
                    "last_updated": "2015-03-18T08:12:01Z"
                }
            ],
            "physical_reference": "1",
            "floor_level": "-1",
            "last_updated": "2015-06-28T08:12:01Z"
        },
                {
                    "uid": "3257",
                    "evse_id": "BE*BEC*E041503002",
                    "status": "RESERVED",
                    "capabilities": [
                        "RESERVABLE"
                    ],
                    "connectors": [
                        {
                            "id": "1",
                            "standard": "IEC_62196_T2",
                            "format": "SOCKET",
                            "power_type": "AC_3_PHASE",
                            "max_voltage": 220,
                            "max_amperage": 16,
                            "tariff_ids": ["12"],
                            "last_updated": "2015-06-29T20:39:09Z"
                        }
                    ],
                    "physical_reference": "2",
                    "floor_level": "-2",
                    "last_updated": "2015-06-29T20:39:09Z"
                }
            ],
            "operator": {
                "name": "BeCharged"
            },
            "time_zone": "Europe/Brussels",
            "last_updated": "2015-06-29T20:39:09Z"
        }

        location = Location(**data)
        assert validator(location) is None

    def test_energy_contract(self):
        data = {
            "supplier_name": "Greenpeace Energy eG",
            "contract_id": "0123456789"
        }
        energy_contract = EnergyContract(**data)
        assert validator(energy_contract) is None

    def test_token(self):
        data = {
            "country_code": "DE",
            "party_id": "TNM",
            "uid": "12345678905880",
            "type": "RFID",
            "contract_id": "DE8ACC12E46L89",
            "visual_number": "DF000-2001-8999-1",
            "issuer": "TheNewMotion",
            "group_id": "DF000-2001-8999",
            "valid": True,
            "whitelist": "ALLOWED",
            "language": "it",
            "default_profile_type": "GREEN",
            "energy_contract": {
                "supplier_name": "Greenpeace Energy eG",
                "contract_id": "0123456789"
            },
            "last_updated": "2018-12-10T17:25:10Z"
        }
        token = Token(**data)
        assert validator(token) is None