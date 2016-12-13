# networking

A marathon orchestra overview in d3.

![Networking UI for Marathon](https://raw.githubusercontent.com/rebeling/networking/master/docs/networking-ui.png "Networking UI for Marathon")

The container orchestration platform [Marathon](https://mesosphere.github.io/marathon/) for [Apache Mesos](http://mesos.apache.org/) has a handy Web UI, but with growing size of applications and relations it becomes hard to track. This project take the app list from the Marathon API and transforms it into a graph to visualize the network in a browser.

<div><img src="https://raw.githubusercontent.com/rebeling/networking/master/docs/networking-ui-detail.png" alt="Networking UI Detail"/></div>

### Features
    
* Application details with link to maraton
* Internal app references based on urls
* Zoom graph, highlight node and neighbors

### Features for future

* Connection to external datastorages
* Update rendering on push - unhealthy, scaling
* Add traffic between containers and incoming from ha_proxy
* More d3 sugar for graph representation

## Dependencies

The project does not ship with an installer or requirements yet.
All dependecies so far:

* python 2.7
* Jinja2 (2.8)
* networkx (1.11)
* marathon (0.8.7)

Create a file secrets.py with the values of USERNAME, PASSWORD, MARATHON_URL
