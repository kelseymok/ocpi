from ocpi.v221.enums import *


class TestEnums:

    def test_auth_method(self):
        assert AuthMethod.auth_request == "AUTH_REQUEST"
        assert AuthMethod.command == "COMMAND"
        assert AuthMethod.whitelist == "WHITELIST"