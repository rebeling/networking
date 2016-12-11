# -*- coding: utf-8 -*-
import json
import networkx as nx
from utils import stat_graph, render_info, connection_details
"""
    generate graph with networks http://networkx.github.io/
    and reformat this graph into d3 - nodes and links
"""


def add_nodes(nxDG, mcLA):
    """
    """
    mother_node = '/Applications'
    nxDG.add_node(mother_node,
                  name=mother_node,
                  node_name=mother_node[1:],
                  group=mother_node,
                  depth=1,
                  tooltip="root",
                  leaf=0,
                  is_app=0,
                  connections={},
                  instances=0
                  )

    for app in mcLA:
        mother = mother_node
        path = [x for x in app.id.split('/') if x]
        this_id = mother

        for i, node in enumerate(path):
            instances = 0
            this_id += '/' + node
            is_app = 0
            connections = {}

            if i+1 == len(path):
                data = app.json_repr()
                tooltip = render_info(data)
                connections, instances = connection_details(data)
                leaf = 1
            else:
                if i+2 == len(path):
                    is_app = 1
                tooltip = this_id
                leaf = 0

            nxDG.add_node(this_id,
                          name=this_id,
                          node_name=node,
                          group=mother,
                          depth=i+2,
                          tooltip=tooltip,
                          leaf=leaf,
                          is_app=is_app,
                          connections=connections,
                          instances=instances
                          )
            mother = this_id

    return nxDG


def calculate_edges(nodes):
    """
    """
    links = []
    for i, node in enumerate(nodes):
        if node['name'] != '/Applications':
            for j, node_two in enumerate(nodes):
                if node['group'] == node_two['name']:
                    links.append({"source": j,
                                  "target": i,
                                  "weight": node.get('depth', 1)
                                  })
                    break

    for a1, node in enumerate(nodes):
        cons = node['connections']
        if cons:
            cons2 = node['connections']['HAPROXY_0_VHOST']
            if cons2:
                hosts = node['connections']['HAPROXY_0_VHOST'].split(',')
                for a2, node2 in enumerate(nodes):
                    if node != node2:
                        cons2 = node2['connections']
                        if cons2:
                            envs2 = node2['connections']['env'].values()

                            for host in hosts:
                                for envi in envs2:
                                    if host in envi:
                                        links.append({"source": a2,
                                                      "target": a1,
                                                      "weight": 100
                                                     })
    return links


def marathon_graph(mcLA):
    """
    """
    nxDG = nx.DiGraph()
    nxDG = add_nodes(nxDG, mcLA)
    nodes = [n[1] for n in nxDG.nodes(data=True)]
    edges = calculate_edges(nodes)

    return {
        "stats": stat_graph(nxDG, nodes, edges),
        "nodes": nodes,
        "links": edges
    }
