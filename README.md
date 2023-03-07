# OCPI

This repository contains JSON Schemas (to validate against as a contract test) and Python dataclasses to build OCPI types.

## v2.2.1 Modules
- [ ] Versions
- [ ] Credentials
- [ ] Locations
- [ ] Sessions
- [x] CDRs
- [ ] Tariffs
- [ ] Tokens
- [ ] Commands
- [ ] ChargingProfiles
- [ ] HubClientInfo

## Example Usage
```python
from ocpi.v221.types import CdrLocation, GeoLocation
from ocpi.v221.enums import ConnectorType, ConnectorFormat, PowerType

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
```