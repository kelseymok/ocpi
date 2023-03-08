from typing import Optional

import requests
import json
from ocpi.v221.types import CDR, Credentials, EnergyMix, Location, Hours, Session, Tariff, Token, \
    DisplayText, VersionData
from test_utils import validator


class TestOcpiExamples:

    def _read_and_validate(self, url, t, data_key: Optional[str] = None):
            data = json.loads(requests.get(url).text)
            o = t(**data) if data_key is None else t(**data[data_key])
            validator(o)

    def test_cdr(self):
        payloads = [
            "https://raw.githubusercontent.com/ocpi/ocpi/master/examples/cdr_example.json"
        ]

        for i in payloads:
            self._read_and_validate(i, CDR)

    def test_credentials(self):
        payloads = [
            "https://raw.githubusercontent.com/ocpi/ocpi/master/examples/credentials_example.json",
            "https://raw.githubusercontent.com/ocpi/ocpi/master/examples/credentials_example2.json",
            "https://raw.githubusercontent.com/ocpi/ocpi/master/examples/credentials_example3.json",
            "https://raw.githubusercontent.com/ocpi/ocpi/master/examples/credentials_example4.json",
        ]

        for i in payloads:
            self._read_and_validate(i, Credentials)

    def test_energy_mix(self):
        payloads = [
            "https://raw.githubusercontent.com/ocpi/ocpi/master/examples/location_energymix_example_complete.json",
            "https://raw.githubusercontent.com/ocpi/ocpi/master/examples/location_energymix_example_energy_provider.json",
            "https://raw.githubusercontent.com/ocpi/ocpi/master/examples/location_energymix_example_simple.json",
        ]

        for i in payloads:
            self._read_and_validate(i, EnergyMix, data_key="energy_mix")

    def test_location(self):
        payloads = [
            "https://raw.githubusercontent.com/ocpi/ocpi/master/examples/location_example.json",
            "https://raw.githubusercontent.com/ocpi/ocpi/master/examples/location_example_parking_garage_opening_hours.json",
            "https://raw.githubusercontent.com/ocpi/ocpi/master/examples/location_example_uc2_destination_charger.json",
            "https://raw.githubusercontent.com/ocpi/ocpi/master/examples/location_example_uc3_destination_charger_not_published.json",
            "https://raw.githubusercontent.com/ocpi/ocpi/master/examples/location_example_uc4_limited_visibility.json",
            "https://raw.githubusercontent.com/ocpi/ocpi/master/examples/location_example_uc5_home_charge_point.json",
        ]

        for i in payloads:
            self._read_and_validate(i, Location)

    def test_hours(self):
        payloads = [
            "https://raw.githubusercontent.com/ocpi/ocpi/master/examples/location_hours_247_open_exception_closing.json",
            "https://raw.githubusercontent.com/ocpi/ocpi/master/examples/location_hours_opening_hours_with_exceptional_closing.json",
            "https://raw.githubusercontent.com/ocpi/ocpi/master/examples/location_hours_opening_hours_with_exceptional_opening.json",
        ]

        for i in payloads:
            self._read_and_validate(i, Hours)

    def test_session(self):
        payloads = [
            "https://raw.githubusercontent.com/ocpi/ocpi/master/examples/session_example_1_simple_start.json",
            "https://raw.githubusercontent.com/ocpi/ocpi/master/examples/session_example_2_short_finished.json",
        ]

        for i in payloads:
            self._read_and_validate(i, Session)

    def test_tariff(self):
        payloads = [
            "https://raw.githubusercontent.com/ocpi/ocpi/master/examples/tariff_10_025kwh_parking_start.json",
            "https://raw.githubusercontent.com/ocpi/ocpi/master/examples/tariff_11_not_possible_alt_text.json",
            "https://raw.githubusercontent.com/ocpi/ocpi/master/examples/tariff_12_025kwh_min_price.json",
            "https://raw.githubusercontent.com/ocpi/ocpi/master/examples/tariff_13_simple_3hour_5parking.json",
            "https://raw.githubusercontent.com/ocpi/ocpi/master/examples/tariff_14_step_size.json",
            "https://raw.githubusercontent.com/ocpi/ocpi/master/examples/tariff_15_reservation_5_euro_per_hour.json",
            "https://raw.githubusercontent.com/ocpi/ocpi/master/examples/tariff_16_reservation_2_euro_fee_5_euro_per_hour.json",
            "https://raw.githubusercontent.com/ocpi/ocpi/master/examples/tariff_17_reservation_with_expire_fee.json",
            "https://raw.githubusercontent.com/ocpi/ocpi/master/examples/tariff_18_reservation_with_expire_time.json",
            "https://raw.githubusercontent.com/ocpi/ocpi/master/examples/tariff_1_simple_2hour.json",
            "https://raw.githubusercontent.com/ocpi/ocpi/master/examples/tariff_2_alt_text.json",
            "https://raw.githubusercontent.com/ocpi/ocpi/master/examples/tariff_3_alt_url.json",
            "https://raw.githubusercontent.com/ocpi/ocpi/master/examples/tariff_4_complex.json",
            "https://raw.githubusercontent.com/ocpi/ocpi/master/examples/tariff_3_alt_url.json",
            "https://raw.githubusercontent.com/ocpi/ocpi/master/examples/tariff_5_free_of_charge.json",
            "https://raw.githubusercontent.com/ocpi/ocpi/master/examples/tariff_6_025kwh_start_max_price.json",
            "https://raw.githubusercontent.com/ocpi/ocpi/master/examples/tariff_7_first_hour_kwh_free.json",
            "https://raw.githubusercontent.com/ocpi/ocpi/master/examples/tariff_8_simple_025kwh.json",
            "https://raw.githubusercontent.com/ocpi/ocpi/master/examples/tariff_9_025kwh_start.json",
            "https://raw.githubusercontent.com/ocpi/ocpi/master/examples/tariffrestriction_example_max_duration.json",
            "https://raw.githubusercontent.com/ocpi/ocpi/master/examples/tariffrestriction_example_max_power.json",
        ]

        for i in payloads:
            self._read_and_validate(i, Tariff)

    def test_token(self):
        payloads = [
            "https://raw.githubusercontent.com/ocpi/ocpi/master/examples/token_example_1_app_user.json",
            "https://raw.githubusercontent.com/ocpi/ocpi/master/examples/token_example_2_full_rfid.json",
        ]

        for i in payloads:
            self._read_and_validate(i, Token)

    def test_display_text(self):
        payloads = [
            "https://raw.githubusercontent.com/ocpi/ocpi/master/examples/type_displaytext_example.json",
        ]

        for i in payloads:
            self._read_and_validate(i, DisplayText)

    def test_version_data(self):
        payloads = [
            "https://raw.githubusercontent.com/ocpi/ocpi/master/examples/version_details_example.json",
            "https://raw.githubusercontent.com/ocpi/ocpi/master/examples/version_details_example2.json",
        ]

        for i in payloads:
            self._read_and_validate(i, VersionData)