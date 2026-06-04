# Simple Python Docker Backend

This is a simple Python project that highlights basic skills of deploying backend applications locally using Docker and Nginx as a reverse proxy.

## Prerequisites

To start the application, you need a Linux machine with Docker and Docker Compose installed. Please follow the official Docker installation guidelines before proceeding.

## Getting Started

1. Clone the project to your local machine.
2. Navigate into the project root directory:
   ```bash
   cd tz
   ```
3. Start the application stack:
   ```bash
   docker compose up -d
   ```

Nothing else is required. The application stack will initialize automatically. 

## Testing the Application

To verify that the deployment was successful, execute a `curl` request against your localhost:

```bash
curl http://localhost
```

**Expected Response:**
```text
Hello from Effective Mobile!
```

## Architecture Under the Hood

Docker Compose initializes two dedicated services isolated inside a custom network (`frontend-net`):

* **my-backend**: A lightweight Python application compiled using a secure `python:3.12-slim` image. It listens internally on port `8080` to return the success string. The container is completely hidden from the local network and does not export any public ports.
* **my-nginx**: A high-performance reverse proxy server using a stable Alpine footprint (`nginx:1.26-alpine`). It binds strictly to the host's `localhost:80` interface to intercept incoming traffic and securely proxy requests down to the hidden backend container.

