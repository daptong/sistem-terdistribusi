# Distributed Systems Practice - Containerized

This repository demonstrates multiple distributed system communication patterns. Each section now has an isolated Docker / Docker Compose setup so the host Python environment remains untouched.

## Prerequisites
- Docker Engine + Docker Compose plugin

## Sections & How to Run

All compose files are under `compose/`.

| Pattern | Compose File | Run Command | Notes |
|---------|--------------|-------------|-------|
| REST (Flask) | `compose/rest.yml` | `docker compose -f compose/rest.yml up -d` | Manual exec inside |
| JSON-RPC | `compose/rpc.yml` | `docker compose -f compose/rpc.yml up -d` | Manual server/client |
| SOAP | `compose/soap.yml` | `docker compose -f compose/soap.yml up -d` | Exec zeep client |
| MQTT (Mosquitto) | `compose/mqtt.yml` | `docker compose -f compose/mqtt.yml up -d` | Internal local broker |
| TCP Req/Resp | `compose/reqresp.yml` | `docker compose -f compose/reqresp.yml up -d` | Interactive echo |
| UDP One-way | `compose/udp.yml` | `docker compose -f compose/udp.yml up -d` | UDP send/recv |
| ZeroMQ | `compose/zmq.yml` | `docker compose -f compose/zmq.yml up -d` | REQ/REP + PUB/SUB |
| ZooKeeper Election | `compose/zookeeper_election.yml` | `docker compose -f compose/zookeeper_election.yml up -d` | Nodes auto run |
| Processes & Threads / Ice | `compose/code_process.yml` | `docker compose -f compose/code_process.yml up -d` | Demos + Ice |
| CORBA | `compose/corba.yml` | `docker compose -f compose/corba.yml up -d` | ORB only |
| Upcall Demo | `compose/upcall.yml` | `docker compose -f compose/upcall.yml up -d` | Manual client |
| Lamport Clock | `compose/lamport.yml` | `docker compose -f compose/lamport.yml up -d` | Manual client |

Stop with Ctrl+C or:
```bash
docker compose -f compose/<file>.yml down
```

## Container Details
Each service has its own image build (Python 3.11 slim) with minimal dependencies via per-module `requirements.txt` when needed.

## Logs & Interaction
Use a second terminal for logs or interactive runs:
```bash
docker compose -f compose/rpc.yml exec rpc-server python rpcserver.py
docker compose -f compose/rpc.yml exec rpc-client python rpcclient.py
```

## Extending
- Add healthchecks for production usage.
- Combine into a single multi-service `docker-compose.yml` if orchestration across patterns is desired.

## Manual Execution Cheat Sheet
All clients start idle (`tail -f`). Exec commands inside containers after `up -d`.

### REST
```bash
docker compose -f compose/rest.yml up -d
docker compose -f compose/rest.yml exec rest-server python server.py
docker compose -f compose/rest.yml exec rest-client python client.py --op both -a 2 -b 3
```

### JSON-RPC
```bash
docker compose -f compose/rpc.yml up -d
docker compose -f compose/rpc.yml exec rpc-server python rpcserver.py
docker compose -f compose/rpc.yml exec rpc-client python rpcclient.py
```

### SOAP
```bash
docker compose -f compose/soap.yml up -d
docker compose -f compose/soap.yml exec soap-server python server.py
docker compose -f compose/soap.yml exec soap-client python client.py
```

### MQTT (internal broker service)
```bash
docker compose -f compose/mqtt.yml up -d
# Start subscriber (listens on topic)
docker compose -f compose/mqtt.yml exec mqtt-sub python sub.py
# Publish messages
docker compose -f compose/mqtt.yml exec mqtt-pub python pub.py
```

### TCP Req/Resp
```bash
docker compose -f compose/reqresp.yml up -d
docker compose -f compose/reqresp.yml exec reqresp-server python server.py
docker compose -f compose/reqresp.yml exec reqresp-client python client.py
```

### UDP One-way
```bash
docker compose -f compose/udp.yml up -d
docker compose -f compose/udp.yml exec udp-server python serverUDP.py
docker compose -f compose/udp.yml exec udp-client python clientUDP.py
```

### ZeroMQ
```bash
docker compose -f compose/zmq.yml up -d
docker compose -f compose/zmq.yml exec zmq-req python clientzmq.py
docker compose -f compose/zmq.yml exec zmq-sub python subzmq.py
# PUSH/PULL pattern (producer auto-runs). Open a worker:
docker compose -f compose/zmq.yml exec zmq-pull python pullzmq.py
```

### ZooKeeper Election
```bash
docker compose -f compose/zookeeper_election.yml up -d
docker compose -f compose/zookeeper_election.yml logs -f election-node-1
```

### Processes / Threads / Ice
```bash
docker compose -f compose/code_process.yml up -d
docker compose -f compose/code_process.yml exec multiprocess-demo python multiprcs.py
docker compose -f compose/code_process.yml exec multithread-demo python multithreads.py
docker compose -f compose/code_process.yml exec ice-server sh -c "slice2py Demo.ice || true; python ice_server.py"
docker compose -f compose/code_process.yml exec ice-client python ice_client.py
```

### CORBA (Naming Service only server currently)
The original example uses the CORBA Naming Service. Due to missing Python omniORB bindings in the base image, only the server stub (which attempts NameService binding) is present and runs for demonstration; a separate client script is not included.

Current state:
- `corba-server` container builds environment with omniORB tools.
- Server registers object with `NameService` (requires an external naming service to actually resolve).
- No working Python client provided (bindings unavailable in minimal container without heavier source build).

Run the container (server will start and then block):
```bash
docker compose -f compose/corba.yml up -d
docker compose -f compose/corba.yml exec corba-server python server.py
```
If you later add omniORBpy bindings, you can create a client that resolves the name `Hello` via the naming context.

### Upcall
```bash
docker compose -f compose/upcall.yml up -d
docker compose -f compose/upcall.yml exec upcall-server python servercall.py
docker compose -f compose/upcall.yml exec upcall-client python clientcall.py
```

### Lamport Clock
```bash
docker compose -f compose/lamport.yml up -d
docker compose -f compose/lamport.yml exec lamport-server python s_lamp.py
docker compose -f compose/lamport.yml exec lamport-client python c_lamp.py
```

## Limitations / Future Work
- Add healthchecks & simple retry loops (e.g. RPC client) instead of fixed sleeps.
- Security (TLS, auth) intentionally omitted for clarity.

## Cleanup
Remove all images:
```bash
docker image prune -f
```

## License
Educational use.
