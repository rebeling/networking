# -*- coding: utf-8 -*-
import pylab as plt
from networkx.drawing.nx_agraph import graphviz_layout
from jinja2 import Template
# from collections import Counter


def draw_graph(G):
    nx.draw(G, pos=graphviz_layout(G), node_size=300, cmap=plt.cm.Blues,
            node_color=range(len(G)), prog='dot')
    plt.show()


def stat_graph(G, nodes, links):
    """
        count task and pattern for same jobs with different names
        find most jobs as single apps ..vs service
    """
    jobs = [x['node_name'] for x in nodes if x['leaf']]

    instances = sum([x.get('instances', 0) for x in nodes])
    string = "nodes: %s<br>edges: %s<br>instances: %s" % (
        G.number_of_nodes(), len(links), instances)

    # print Counter(jobs)
    # job_string = ["%s: %s" % (x, y) for x, y in Counter(jobs).items()]
    # string += "jobs:<br>%s" % "<br>".join(job_string)
    return string


def render_info(data):
    """
    """
    info = """{% if labels_data %}
    <h5>labels</h5>
    <ul class="list-unstyled">
    {% for n, m in labels_data %}
        <li>{{ n }}:<br><i>{{ m }}</i></li>
    {% endfor %}
    </ul>
    {% endif %}
    {% if env_data %}
    <h5>env</h5>
    <ul class="list-unstyled">
    {% for n, m in env_data %}
        <li>{{ n }}:<br><i>{{ m }}</i></li>
    {% endfor %}
    </ul>
    {% endif %}
    {% if settings_data %}
    <h5>settings</h5>
    <ul class="list-unstyled">
    {% for n, m in settings_data %}
        <li>{{ n }}: <i>{{ m }}</i></li>
    {% endfor %}
    </ul>
    {% endif %}
    """
    data_keys = [
        'instances',
        'mem',
        'tasks_running',
        'tasks_staged',
        'tasks_healthy',
        'tasks_unhealthy',
        'instances',
        'cpus']
    data['env_data'] = [(x, y) for (x, y) in data['env'].items() if y]
    data['settings_data'] = [(x, y) for x, y in data.items() if x in data_keys and y]
    data['labels_data'] = [
        ('HAPROXY_0_VHOST', data['labels'].get('HAPROXY_0_VHOST', None)),
        ('HAPROXY_GROUP', data['labels'].get('HAPROXY_GROUP', None))]
    data['labels_data'] = [(x, y) for x, y in data['labels_data'] if y]
    t = Template(info)
    return t.render(data)


def connection_details(data):
    connections = {
        'HAPROXY_0_VHOST': data['labels'].get('HAPROXY_0_VHOST', ""),
        'env': data['env']
    }
    instances = data.get('instances', 0)
    return connections, instances
