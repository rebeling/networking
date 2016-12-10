#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import json
from graph import marathon_graph
from marathon import MarathonClient


def generate_network_graph():
    """
    1. connect to client, vpn must be on
    2. transform martahon app list into networkx graph
    3. save graph to file
    4. serve the graph with d3 frontend
    """
    from secrets import USERNAME, PASSWORD, MARATHON_URL

    mc = MarathonClient(MARATHON_URL, username=USERNAME, password=PASSWORD)
    print "Initilized {}\niterating apps...".format(mc)

    result = marathon_graph(mc.list_apps())
    result["MARATHON_URL"] = MARATHON_URL
    filename = 'graphFile.json'

    with open('visualization/{}'.format(filename), 'w') as f:
        json.dump(result, f, indent=4)
    print "Done."


if __name__ == "__main__":

    generate_network_graph()
