###############################################################################
# (C) Copyright 2020-2024 Andrea Sorbini
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
###############################################################################
from uno.middleware import Middleware

from .connext_condition import ConnextCondition
from .connext_participant import ConnextParticipant


class ConnextMiddleware(Middleware):
  CONDITION = ConnextCondition
  PARTICIPANT = ConnextParticipant

  @property
  def install_instructions(self) -> str | None:
    import uno_middleware_connext

    return """\
# Install RTI Connext DDS middleware
pip install git+https://github.com/mentalsmash/uno-middleware-connext@{version}
""".format(version=uno_middleware_connext.__version__)

  def define_uvn_instructions(self) -> str | None:
    return """\
# Point uno to a valid RTI license file
export RTI_LICENSE_FILE=/path/to/rti_license.dat
""".format()
