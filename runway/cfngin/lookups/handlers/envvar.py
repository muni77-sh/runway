"""Environment variable lookup."""
# pylint: disable=unused-argument,arguments-differ
import os
from typing import Any

from ....lookups.handlers.base import LookupHandler
from ...util import read_value_from_path

TYPE_NAME = "envvar"


class EnvvarLookup(LookupHandler):
    """Environment variable lookup."""

    @classmethod
    def handle(cls, value: str, **_: Any) -> str:
        """Retrieve an environment variable.

        Args:
            value: Parameter(s) given to this lookup.

        Example:
            ::

                # With CFNgin we would reference the environment variable like this:
                conf_key: ${envvar ENV_VAR_NAME}

            You can optionally store the value in a file, ie::

                $ cat envvar_value.txt
                ENV_VAR_NAME

            and reference it within CFNgin (NOTE: the path should be relative
            to the CFNgin config file)::

                conf_key: ${envvar file://envvar_value.txt}

                # Both of the above would resolve to
                conf_key: ENV_VALUE

        """
        value = read_value_from_path(value)

        try:
            return os.environ[value]
        except KeyError:
            raise ValueError('EnvVar "{}" does not exist'.format(value))
