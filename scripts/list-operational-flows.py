#!/usr/bin/env python
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors:
#          - Beraldo Leal <beraldo AT ncc DOT unesp DOT br>
#
# -*- coding: utf-8 -*-
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

from odl.topology import ODLTopology
from odl.instance import ODLInstance

import os
import sys

if __name__ == "__main__":
    try:
        server = os.environ["ODL_URL"]
        user = os.environ["ODL_USER"]
        password = os.environ["ODL_PASS"]
    except KeyError:
        print "Please provide all environment vairables."
        print "Read the README.md for more information."
        sys.exit(1)

    credentials = (user, password)

    odl = ODLInstance(server, credentials)
    nodes = odl.get_nodes()
    for node in nodes.values():
        tables = node.get_tables()
        print "Node: ", node, node.ip_address," Tables: ", len(tables)
        for table in tables:
            flows = table.get_operational_flows()
            if len(flows) > 0:
                print "%20s %10s %5s %5s %10s %20s" % ("id",
                                                       "priority",
                                                       "idle",
                                                       "hard",
                                                       "bytes",
                                                       "packets")
                print "-"*80
                for flow in flows:
                    print "%20s %10s %5s %5s %10s %20s" % (flow.id,
                                                           flow.priority,
                                                           flow.idle_timeout,
                                                           flow.hard_timeout,
                                                           flow.get_byte_count(),
                                                           flow.get_packet_count())