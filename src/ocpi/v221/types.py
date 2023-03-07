from dataclasses import dataclass, field
from typing import Optional, List

from ocpi.v221.enums import TokenType, AuthMethod, ConnectorType, ConnectorFormat, PowerType, TariffType, DayOfWeek, \
    ReservationRestrictionType, TariffDimensionType, EnergySourceCategory, EnvironmentalImpactCategory, \
    CdrDimensionType, VersionNumber


@dataclass(frozen=True)
class CdrToken:
    uid: str  # CiString(36)
    type: TokenType
    contract_id: str  # CiString(36)


@dataclass(frozen=True)
class GeoLocation:
    latitude: str  # str(10) Latitude of the point in decimal degree. Example: 50.770774. Decimal separator: "." Regex: -?[0-9]{1,2}\.[0-9]{5,7}
    longitude: str  # str(11) Longitude of the point in decimal degree. Example: -126.104965. Decimal separator: "." Regex: -?[0-9]{1,3}\.[0-9]{5,7}

@dataclass(frozen=True)
class CdrLocation:
    id: str  # CiString(36)
    address: str   # string(45)
    city: str    # string(45)
    postal_code: str # str(10)
    country: str  # str(3) ISO 3166-1 alpha-3 code for the country of this location.
    evse_uid: str  # CiString(36) Uniquely identifies the EVSE within the CPO’s platform (and suboperator platforms). For example a database unique ID or the actual EVSE ID. This field can never be changed, modified or renamed. This is the technical identification of the EVSE, not to be used as human readable identification, use the field: evse_id for that.
    evse_id: str # CiString(48) Compliant with the following specification for EVSE ID from "eMI3 standard version V1.0" (http://emi3group.com/documents-links/) "Part 2: business objects.".
    connector_id: str # CiString(36)
    coordinates: GeoLocation
    connector_standard: ConnectorType
    connector_format: ConnectorFormat
    connector_power_type: PowerType
    name: Optional[str] = None # string(255)


@dataclass(frozen=True)
class DisplayText:
    language: str = field(metadata={"length": 2})  # string(2) Language Code ISO 639-1
    text: str = field(metadata={"length": 512})  # string(512) No markup, html etc allowed


@dataclass(frozen=True)
class URL:
    url: str  # from urllib.parse import urlparse; urlparse("scheme://netloc/path;parameters?query#fragment")


@dataclass(frozen=True)
class Price:
    excl_vat: float  # JSON numbers, 4 decimals and a sufficiently large number of digits
    incl_vat: Optional[float]  # JSON numbers, 4 decimals and a sufficiently large number of digits


@dataclass(frozen=True)
class TariffRestrictions:
    day_of_week: List[DayOfWeek] = field(default_factory=list)
    start_time: Optional[str] = None   # string(5) Start time of day in local time, the time zone is defined in the time_zone field of the Location, for example 13:30, valid from this time of the day. Must be in 24h format with leading zeros. Hour/Minute separator: ":" Regex: ([0-1][0- 9]|2[0-3]):[0-5][0-9]
    end_time: Optional[str] = None  # string(5) End time of day in local time, the time zone is defined in the time_zone field of the Location, for example 19:45, valid until this time of the day. Same syntax as start_time. If end_time < start_time then the period wraps around to the next day. To stop at end of the day use: 00:00.
    start_date: Optional[str] = None  # string(10) Start date in local time, the time zone is defined in the time_zone field of the Location, for example: 2015-12-24, valid from this day (inclusive). Regex: ([12][0-9]{3})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])
    end_date: Optional[str] = None  # string(10) End date in local time, the time zone is defined in the time_zone field of the Location, for example: 2015-12-27, valid until this day (exclusive). Same syntax as start_date.
    min_kwh: Optional[float] = None  # number
    max_kwh: Optional[float] = None  # number
    min_current: Optional[float] = None  # number
    max_current: Optional[float] = None  # number
    min_power: Optional[float] = None  # number
    max_power: Optional[float] = None  # number
    min_duration: Optional[int] = None
    max_duration: Optional[int] = None
    reservation: Optional[ReservationRestrictionType] = None


@dataclass(frozen=True)
class PriceComponent:
    type: TariffDimensionType
    price: float # number
    step_size: int
    vat: Optional[float] = None  # number


@dataclass(frozen=True)
class TariffElement:
    price_components: PriceComponent  # + cardinality
    restrictions: Optional[TariffRestrictions]


@dataclass(frozen=True)
class EnergySource:
    source: EnergySourceCategory
    percentage: float  # number


@dataclass(frozen=True)
class EnvironmentalImpact:
    category: EnvironmentalImpactCategory
    amount: float # number (in g/kWh)


@dataclass(frozen=True)
class EnergyMix:
    is_green_energy: bool
    energy_sources: List[EnergySource]
    environ_impact: List[EnvironmentalImpact]
    supplier_name: Optional[str] = None # string(64)
    energy_product_name: Optional[str] = None # string(64)


@dataclass(frozen=True)
class Tariff:
    country_code: str  # CiString(2) ISO-3166 alpha-2 country code of the CPO that owns this Tariff.
    party_id: str  # CIString(3)  CPO ID of the CPO that owns this Tariff (following the ISO-15118 standard).
    id: str  # CiString(36)
    currency: str  # string(3)  ISO-4217 code of the currency of this tariff.
    last_updated: str
    type: Optional[TariffType] = None
    tariff_alt_text: List[DisplayText] = field(default_factory=list) # * Cardinality
    tariff_alt_url: Optional[URL] = None
    min_price: Optional[Price] = None
    max_price: Optional[Price] = None
    elements: TariffElement = field(default_factory=list) # + Cardinality
    start_date_time: Optional[str] = None  # UTC
    end_date_time: Optional[str] = None  # UTC
    energy_mix: Optional[EnergyMix] = None


@dataclass(frozen=True)
class CdrDimension:
    type: CdrDimensionType
    volume: float  # number


@dataclass(frozen=True)
class ChargingPeriod:
    start_date_time: str # use a proper str class
    dimensions: CdrDimension  # + Cardinality
    tariff_id: str  # CiString(36)


@dataclass(frozen=True)
class SignedValue:
    nature: str  # CiString(32)
    plain_data: str  # CiString(512)
    signed_data: str  # CiString(512)


@dataclass(frozen=True)
class SignedData:
    encoding_method: str  # CiString(36)
    url: str
    signed_values: List[SignedValue] = field(default_factory=list)  # + cardinality
    encoding_method_version: Optional[int] = None
    public_key: Optional[str] = None  # CiString(512)


@dataclass(frozen=True)
class CDR:
    country_code: str  # CiString(2) ISO-3166 alpha-2 country code of the CPO that 'owns' this CDR.
    party_id: str  # CiString(3) CPO ID of the CPO that 'owns' this CDR (following the ISO-15118 standard).
    id: str  # CiString(39)  Uniquely identifies the CDR within the CPO’s platform (and suboperator platforms). This field is longer than the usual 36 characters to allow for credit CDRs to have something appended to the original ID. Normal (non-credit) CDRs SHALL only have an ID with a maximum length of 36.
    start_date_time: str  # string(25) following RFC 3339, with some additional limitations. All should be in UTC. No time zone designator = UTC timestamp. Examples: 2015-06-29T20:39:09Z 2015-06-29T20:39:09 2016-12-29T17:45:09.2Z 2016-12-29T17:45:09.2 2018-01-01T01:08:01.123Z 2018-01-01T01:08:01.123
    end_date_time: str
    cdr_token: CdrToken
    auth_method: AuthMethod
    last_updated: str  # DateTime
    cdr_location: CdrLocation
    currency: str  # str(3) Currency of the CDR in ISO 4217 Code.
    tariffs: List[Tariff]
    charging_periods: List[ChargingPeriod] # +  cardinality
    total_cost: Price
    total_energy: float # number
    total_time: float # number
    session_id: Optional[str] = None  # CiString(36). Can be omitted if the CPO has not implemented the Sessions module or the CDR is a result of a reservation that never became a charging session (tehrefore no OCPI session)
    authorization_reference: Optional[str] = None  # CiString(36)
    meter_id: Optional[str] = None  # str(255)
    signed_data: Optional[SignedData] = None
    total_fixed_cost: Optional[Price] = None
    total_energy_cost: Optional[Price] = None
    total_time_cost: Optional[Price] = None
    total_parking_time: Optional[float] = None  # number
    total_parking_cost: Optional[Price] = None
    total_reservation_cost: Optional[Price] = None
    remark: Optional[str] = None # str(255)
    invoice_reference_id: Optional[str] = None  # CiString(39)
    credit: Optional[bool] = None
    credit_reference_id: Optional[str] = None  # CiString(39)


@dataclass
class Version:
    version: VersionNumber
    url: URL

