from json import dumps, loads
import re

from oauthlib.common import to_unicode


def plentymarkets_compliance_fix(session):
    def _to_snake_case(n):
        return re.sub("(.)([A-Z][a-z]+)", r"\1_\2", n).lower()

    def _compliance_fix(r, text):
        # Plenty returns the Token in CamelCase instead of _
        if (
            "application/json" in r.headers.get("content-type", {})
            and r.status == 200
        ):
            token = loads(text)
        else:
            return r

        fixed_token = {}
        for k, v in token.items():
            fixed_token[_to_snake_case(k)] = v

        r._content = to_unicode(dumps(fixed_token)).encode("UTF-8")
        return r

    session.register_compliance_hook("access_token_response", _compliance_fix)
    return session