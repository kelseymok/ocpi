from enum import Enum


class TokenType(str, Enum):
    ad_hoc_user = "AD_HOC_USER"
    app_user = "APP_USER"
    other = "OTHER"
    rfid = "RFID"


class AuthMethod(str, Enum):
    auth_request = "AUTH_REQUEST"
    command = "COMMAND"
    whitelist = "WHITELIST"


class ConnectorType(str, Enum):
    chademo = "CHADEMO"  # The connector type is CHAdeMO, DC
    domestic_a = "DOMESTIC_A"  # Standard/Domestic household, type "A", NEMA 1-15, 2 pins
    domestic_b = "DOMESTIC_B"  # Standard/Domestic household, type "B", NEMA 5-15, 3 pins
    domestic_c = "DOMESTIC_C"  # Standard/Domestic household, type "C", CEE 7/17, 2 pins
    domestic_d = "DOMESTIC_D"  # Standard/Domestic household, type "D", 3 pin
    domestic_e = "DOMESTIC_E"  # Standard/Domestic household, type "E", CEE 7/5 3 pins
    domestic_f = "DOMESTIC_F"  # Standard/Domestic household, type "F", CEE 7/4, Schuko, 3 pins
    domestic_g = "DOMESTIC_G"  # Standard/Domestic household, type "G", BS 1363, Commonwealth, 3 pins
    domestic_h = "DOMESTIC_H"  # Standard/Domestic household, type "H", SI-32, 3 pins
    domestic_i = "DOMESTIC_I"  # Standard/Domestic household, type "I", AS 3112, 3 pins
    domestic_j = "DOMESTIC_J"  # Standard/Domestic household, type "J", SEV 1011, 3 pins
    domestic_k = "DOMESTIC_K"  # Standard/Domestic household, type "K", DS 60884-2-D1, 3 pins
    domestic_l = "DOMESTIC_L"  # Standard/Domestic household, type "L", CEI 23-16-VII, 3 pins
    iec_60309_2_single_16 = "IEC_60309_2_single_16"  # IEC 60309-2 Industrial Connector single phase 16 amperes (usually blue)
    iec_60309_2_three_16 = "IEC_60309_2_three_16"  # IEC 60309-2 Industrial Connector three phase 16 amperes (usually red)
    iec_60309_2_three_32 = "IEC_60309_2_three_32"  # IEC 60309-2 Industrial Connector three phase 32 amperes (usually red)
    iec_60309_2_three_64 = "IEC_60309_2_three_64"  # IEC 60309-2 Industrial Connector three phase 64 amperes (usually red)
    iec_62196_t1 = "IEC_62196_T1"  # IEC 62196 Type 1 "SAE J1772"
    iec_62196_t1_combo = "IEC_62196_T1_COMBO"  # Combo Type 1 based, DC
    iec_62196_t2 = "IEC_62196_T2"  # IEC 62196 Type 2 "Mennekes"
    iec_62196_t2_combo = "IEC_62196_T2_COMBO"  # Combo Type 2 based, DC
    iec_62196_t3a = "IEC_62196_T3A"  # IEC 62196 Type 3A
    iec_62196_t3c = "IEC_62196_T3C"  # IEC 62196 Type 3C "Scame"
    pantograph_bottom_up = "PANTOGRAPH_BOTTOM_UP"  # On-board Bottom-up-Pantograph typically for bus charging
    pantograph_top_down = "PANTOGRAPH_TOP_DOWN"  # Off-board Top-down-Pantograph typically for bus charging
    tesla_r = "TESLA_R"  # Tesla Connector "Roadster"-type (round, 4 pin)
    tesla_s = "TESLA_S"  # Tesla Connector "Model-S"-type (oval, 5 pin)


class ConnectorFormat(str, Enum):
    socket = "SOCKET"  # The connector is a socket; the EV user needs to bring a fitting plug.
    cable = "CABLE"  # The connector is an attached cable; the EV users car needs to have a fitting inlet.


class PowerType(str, Enum):
    ac_1_phase = "AC_1_PHASE"  # AC single phase
    ac_3_phase = "AC_3_PHASE"  # AC three phase
    dc = "DC"  # Direct Current


class TariffType(str, Enum):
    ad_hoc_payment = "AD_HOC_PAYMENT"
    profile_cheap = "PROFILE_CHEAP"
    profile_fast = "PROFILE_FAST"
    profile_green = "PROFILE_GREEN"
    regular = "REGULAR"


class DayOfWeek(str, Enum):
    monday = "MONDAY"
    tuesday = "TUESDAY"
    wednesday = "WEDNESDAY"
    thursday = "THURSDAY"
    friday = "FRIDAY"
    saturday = "SATURDAY"
    sunday = "SUNDAY"


class ReservationRestrictionType(str, Enum):
    reservation = "RESERVATION"
    reservation_expires = "RESERVATION_EXPIRES"


class TariffDimensionType(str, Enum):
    energy = "ENERGY"
    flat = "FLAT"
    parking_time = "PARKING_TIME"
    time = "TIME"


class EnergySourceCategory(str, Enum):
    nuclear = "NUCLEAR"
    general_fossil = "GENERAL_FOSSIL"
    coal = "COAL"
    gas = "GAS"
    general_green = "GENERAL_GREEN"
    solar = "SOLAR"
    wind = "WIND"
    water = "WATER"


class EnvironmentalImpactCategory(str, Enum):
    nuclear_waste = "NUCLEAR_WASTE"
    carbon_dioxide = "CARBON_DIOXIDE"


class CdrDimensionType(str, Enum):
    current = "CURRENT"
    energy = "ENERGY"
    energy_export = "ENERGY_EXPORT"
    energy_import = "ENERGY_IMPORT"
    max_current = "MAX_CURRENT"
    min_current = "MIN_CURRENT"
    max_power = "MAX_POWER"
    min_power = "MIN_POWER"
    parking_time = "PARKING_TIME"
    power = "POWER"
    reservation_time = "RESERVATION_TIME"
    state_of_charge = "STATE_OF_CHARGE"
    time = "TIME"

