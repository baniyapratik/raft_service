## Initial Setup 

#### Leader initiate, initiate()
Initiate leader, done at the initial stage of setting up the network
- set this node to be the leader
- add this node to the cluster
- start sending the heartbeat to the list of neighbors(null at the beginning)

#### Add nodes to the cluster, add_neighbor()
When the leader adds a node into the cluster
- add the leader node to the heartbeat list
- update the state of this node to follower
- call curl to follower node to execute added_to_cluster()

#### Update the added node, added_to_cluster()
When the node is added into the cluster
- start the heartbeat server, this is to track the heartbeat sent by the leader
- change the state of the node to the follower state
- update the neighbors list based off the leaders

## Load Balancing
```text
location /service  {
  if ($request_method = POST ) {
    fastcgi_pass 127.0.0.1:1234;
  }

  if ($request_method = GET ) {
     alias /path/to/files;
  }
}
```
Based on Loadbalance algorithm
```text
http {
    upstream backend {
        least_conn;
        server backend1.example.com max_fails=3;;
        server backend2.example.com max_fails=3;;
    }
    
    server {
        location / {
            proxy_pass http://backend;
        }
    }
}
```