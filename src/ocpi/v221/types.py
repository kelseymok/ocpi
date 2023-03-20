from dataclasses import dataclass, field
from typing import Optional, List

from ocpi.v221.enums import TokenType, AuthMethod, ConnectorType, ConnectorFormat, PowerType, TariffType, DayOfWeek, \
    ReservationRestrictionType, TariffDimensionType, EnergySourceCategory, EnvironmentalImpactCategory, \
    CdrDimensionType, VersionNumber, ParkingType, Status, Capability, ParkingRestriction, ImageCategory, Facility, \
    AllowedType, WhitelistType, ProfileType, SessionStatus, CommandResponseType, CommandResultType, ChargingRateUnit, \
    ChargingProfileResultType, ChargingProfileResponseType, Role, ConnectionStatus, ModuleID, InterfaceRole


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
    language: str  # string(2) Language Code ISO 639-1
    text: str  # string(512) No markup, html etc allowed


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
    restrictions: Optional[TariffRestrictions] = None


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
    energy_sources: List[EnergySource] = field(default_factory=list)
    environ_impact: List[EnvironmentalImpact] = field(default_factory=list)
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
    tariff_alt_text: List[DisplayText] = field(default_factory=list)  # * Cardinality
    tariff_alt_url: Optional[str] = None  # URL
    min_price: Optional[Price] = None
    max_price: Optional[Price] = None
    elements: List[TariffElement] = field(default_factory=list)  # + Cardinality
    start_date_time: Optional[str] = None  # UTC
    end_date_time: Optional[str] = None  # UTC
    energy_mix: Optional[EnergyMix] = None


@dataclass(frozen=True)
class CdrDimension:
    type: CdrDimensionType
    volume: float  # number


@dataclass(frozen=True)
class ChargingPeriod:
    start_date_time: str  # use a proper str class
    dimensions: List[CdrDimension] = field(default_factory=list)  # + Cardinality
    tariff_id: Optional[str] = None # CiString(36)


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
    total_cost: Price
    total_energy: float # number
    total_time: float # number
    tariffs: List[Tariff] = field(default_factory=list)
    charging_periods: List[ChargingPeriod] = field(default_factory=list)  # +  cardinality
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

@dataclass(frozen=True)
class Endpoint:
    identifier: ModuleID
    role: InterfaceRole
    url: str

@dataclass(frozen=True)
class VersionDetailsData:
    version: VersionNumber
    endpoints: List[Endpoint]   # + Cardinality


@dataclass(frozen=True)
class Version:
    version: VersionNumber
    url: str   # URL

@dataclass(frozen=True)
class PublishTokenType:
    uid: Optional[str] = None  # CiString(26)
    type: Optional[TokenType] = None
    visual_number: Optional[str] = None  # str(64)
    issuer: Optional[str] = None # str(64)
    group_id: Optional[str] = None  # CiString(36)


@dataclass(frozen=True)
class AdditionalGeoLocation:
    latitude: str  # str 10  pattern:  -?[0-9]{1,2}\.[0-9]{5,7}
    longitude: str  # str(11) pattern:  -?[0-9]{1,3}\.[0-9]{5,7}
    name: DisplayText


@dataclass(frozen=True)
class StatusSchedule:
    period_begin: str  # datetime str(25)
    status: Status
    period_end: Optional[str] = None  # datetime str(25)


@dataclass(frozen=True)
class Connector:
    id: str  # CiString(36)
    standard: ConnectorType
    format: ConnectorFormat
    power_type: PowerType
    max_voltage: int
    max_amperage: int
    tariff_ids: List[str]  # CiString(36)
    last_updated: str  # datetime str(25)
    max_electric_power: Optional[int] = None
    terms_and_conditions: Optional[str] = None # URL


@dataclass(frozen=True)
class Image:
    url: str  # URL
    category: ImageCategory
    type: str  # CiString(4)
    thumbnail: Optional[str] = None  # URL
    width: Optional[int] = None  # int(5) can't check 5 in json
    height: Optional[int] = None  # int(5)


@dataclass(frozen=True)
class EVSE:
    uid: str  # CiString(36)
    status: Status
    last_updated: str  # str(25)
    status_schedule: List[StatusSchedule] = field(default_factory=list)
    capabilities: List[Capability] = field(default_factory=list)
    directions: List[DisplayText] = field(default_factory=list)
    parking_restrictions: List[ParkingRestriction] = field(default_factory=list)
    images: List[Image] = field(default_factory=list)
    evse_id: Optional[str] = None  # CiString(48)
    floor_level: Optional[str] = None  # str(4)
    coordinates: Optional[GeoLocation] = None
    physical_reference: Optional[str] = None  # str(16)
    connectors: List[Connector] = field(default_factory=list)  # + cardinality


@dataclass(frozen=True)
class BusinessDetails:
    name: str  # str(100)
    website: Optional[str] = None  # Url
    logo: Optional[Image] = None


@dataclass(frozen=True)
class RegularHours:
    weekday: int  # int(1) Monday (1) till Sunday (7)
    period_begin: str  # str(5)  pattern ([0-1][0-9]|2[0-3]):[0-5][0-9]
    period_end: str  # str(5)    pattern ([0-1][0-9]|2[0-3]):[0-5][0-9] (must be later than period begin)


@dataclass(frozen=True)
class ExceptionalPeriod:
    period_begin: str  # datetime str(25)
    period_end: str  # datetime str(25)


@dataclass(frozen=True)
class Hours:
    twentyfourseven: bool
    regular_hours: List[RegularHours] = field(default_factory=list)
    exceptional_openings: List[ExceptionalPeriod] = field(default_factory=list)
    exceptional_closings: List[ExceptionalPeriod] = field(default_factory=list)


@dataclass(frozen=True)
class Location:
    country_code: str  # CiString(2) ISO-3166 alpha-2 country code of the CPO that 'owns' this Location.
    party_id: str  # CiString(3) ID of the CPO that 'owns' this Location (following the ISO-15118 standard).
    id: str  # CiString(36)
    publish: bool  # When this is set to false, only tokens identified in the field: publish_allowed_to are allowed to be shown this Location. When the same location has EVSEs that may be published and may not be published, two 'Locations' should be created.
    address: str  # str(45)
    city: str  # str(45)
    country: str  # str(3) ISO 3166-1 alpha-3 code for the country of this location.
    coordinates: GeoLocation
    last_updated: str  # str(25)
    time_zone: str  # str(255)
    publish_allowed_to: List[PublishTokenType] = field(default_factory=list)  # This field may only be used when the publish field is set to false. Only owners of Tokens that match all the set fields of one PublishToken in the list are allowed to be shown this location.
    related_locations: List[AdditionalGeoLocation] = field(default_factory=list)
    evses: List[EVSE] = field(default_factory=list)
    directions: List[DisplayText] = field(default_factory=list)
    facilities: List[Facility] = field(default_factory=list)
    energy_mix: Optional[EnergyMix] = None
    opening_times: Optional[Hours] = None
    charging_when_closed: Optional[bool] = None
    images: List[Image] = field(default_factory=list)
    parking_type: Optional[ParkingType] = None
    operator: Optional[BusinessDetails] = None
    suboperator: Optional[BusinessDetails] = None
    owner: Optional[BusinessDetails] = None
    name: Optional[str] = None  # str(255)
    postal_code: Optional[str] = None  # str(10)
    state: Optional[str] = None # str(20)


@dataclass(frozen=True)
class EnergyContract:
    supplier_name: str  # str(64)
    contract_id: Optional[str] = None  # str(64)


@dataclass(frozen=True)
class Token:
    country_code: str  # CiString(2)
    party_id: str  # CiString(3)
    uid: str  # CiString(36)
    type: TokenType
    contract_id: str  # CiString(36)
    issuer: str  # str(64)
    valid: bool
    whitelist: WhitelistType
    last_updated: str  # datetime str(25)
    visual_number: Optional[str] = None  # str(64)
    group_id: Optional[str] = None # CiString(36)
    language: Optional[str] = None  # str: 2 Language Code ISO 639-1. This optional field indicates the Token owner’s preferred interface language.
    default_profile_type: Optional[ProfileType] = None
    energy_contract: Optional[EnergyContract] = None


@dataclass(frozen=True)
class LocationReferences:
    location_id: str  # CiString(36)
    evse_uids: List[str] = field(default_factory=list)  # CiString(36)


@dataclass(frozen=True)
class AuthorizationInfo:
    allowed: AllowedType
    token: Token
    location: Optional[LocationReferences] = None
    authorization_reference: Optional[str] = None # CiString(36)
    info: Optional[DisplayText] = None


@dataclass(frozen=True)
class Session:
    country_code: str  # CiString(2)
    party_id: str  # CiString(3)
    id: str  # CiString(36)
    start_date_time: str  # datetime str(25)
    kwh: float
    cdr_token: CdrToken
    auth_method: AuthMethod
    location_id: str  # CiString(36)
    evse_uid: str  # CiString(36)
    connector_id: str  # CiString(36)
    currency: str  # str(3) ISO 4217 code of the currency used for this session.
    status: SessionStatus
    last_updated: str  # datetime str(25)
    end_date_time: Optional[str] = None # datetime str(25)
    authorization_reference: Optional[str] = None  # CiString(36)
    meter_id: Optional[str] = None  # string(255)
    charging_periods: List[ChargingPeriod] = field(default_factory=list)
    total_cost: Optional[Price] = None


@dataclass(frozen=True)
class CancelReservation:
    response_url: str  # url
    reservation_id: str  # CiString(36)


@dataclass(frozen=True)
class CommandResponse:
    result: CommandResponseType
    timeout: int
    message: List[DisplayText] = field(default_factory=list)


@dataclass(frozen=True)
class CommandResult:
    result: CommandResultType
    message: List[DisplayText] = field(default_factory=list)


@dataclass(frozen=True)
class ReserveNow:
    response_url: str # url
    token: Token
    expiry_date: str  # datetime str(25)
    reservation_id: str  # CiString(36)
    location_id: str  # CiString(36)
    evse_uid: Optional[str]  # CiString(36)
    authorization_reference: Optional[str] # CiString(36)


@dataclass(frozen=True)
class StartSession:
    response_url: str  # URL
    token: Token
    location_id: str  # CiString(36)
    evse_uid: Optional[str] = None  # CiString(36)
    connector_id: Optional[str] = None  # CiString(36)
    authorization_reference: Optional[str] = None # CiString(36)


@dataclass(frozen=True)
class StopSession:
    response_url: str  # URL
    session_id: str  # CiString(36)


@dataclass(frozen=True)
class UnlockConnector:
    response_url: str
    location_id: str  # CiString(36)
    evse_uid: str  # CiString(36)
    connector_id: str  # CiString(36)


@dataclass(frozen=True)
class ChargingProfileResponse:
    result: ChargingProfileResponseType
    timeout: int


@dataclass(frozen=True)
class ChargingProfilePeriod:
    start_period: int # seconds
    limit: float


@dataclass(frozen=True)
class ChargingProfile:
    charging_rate_unit: ChargingRateUnit
    start_date_time: Optional[str] = None  # datetime str(25)
    duration: Optional[int] = None
    min_charging_rate: Optional[float] = None
    charging_profile_period: List[ChargingProfilePeriod] = field(default_factory=list)


@dataclass(frozen=True)
class ActiveChargingProfile:
    start_date_time: str  # datetime str(25)
    charging_profile: ChargingProfile


@dataclass(frozen=True)
class ActiveChargingProfileResult:
    result: ChargingProfileResultType
    profile: Optional[ActiveChargingProfile]


@dataclass(frozen=True)
class ChargingProfileResult:
    result: ChargingProfileResultType


@dataclass(frozen=True)
class ClearProfileResult:
    result: ChargingProfileResultType


@dataclass(frozen=True)
class SetChargingProfile:
    charging_profile: ChargingProfile
    response_url: str


@dataclass(frozen=True)
class CredentialsRole:
    role: Role
    business_details: BusinessDetails
    party_id: str  # CiString(3) CPO, eMSP (or other role) ID of this party (following the ISO-15118 standard).
    country_code: str  # CiString(2) ISO-3166 alpha-2 country code of the country this party is operating in.


@dataclass(frozen=True)
class Credentials:
    token: str  # str(64)
    url: str  # URL
    roles: List[CredentialsRole] = field(default_factory=list)  # + cardinality


@dataclass(frozen=True)
class ClientInfo:
    party_id: str  # CiString(3) CPO or eMSP ID of this party (following the 15118 ISO standard), as used in the credentials exchange.
    country_code: str  # CiString(2) ISO-3166 alpha-2 country code of the country this party is operating in.
    role: Role
    status: ConnectionStatus
    last_updated: str  # datetime str(25)
