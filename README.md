# networking

A marathon orchestra overview in d3.

![Networking UI for Marathon](https://raw.githubusercontent.com/rebeling/networking/master/docs/networking-ui.png "Networking UI for Marathon")

[Marathon](https://mesosphere.github.io/marathon/), the container orchestration platform for [Apache Mesos](http://mesos.apache.org/), has a handy Web UI. But with growing size of images and relations it becomes hard to track. This project take the app list from the Marathon API and transforms it into a graph to visualize the network in a browser.

![Networking UI Detail](https://raw.githubusercontent.com/rebeling/networking/master/docs/networking-ui-detail.png "Networking UI Detail" =600x20)

<div style="text-align: center">
<img src="https://raw.githubusercontent.com/rebeling/networking/master/docs/networking-ui-detail.png" alt="Drawing" style="width:92%;"/>
</div>

### Features
    
* Application details with link to maraton
* Internal app references based on urls
* Zoom graph, highlight node and neighbors

### Features for future

* Connection to external datastorages
* Update rendering on push - unhealthy, scaling
* Traffic between containers and incoming
* More d3 sugar for graph representation
