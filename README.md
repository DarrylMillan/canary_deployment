# Canary Deployment Demo with Docker and NGINX

This project demonstrates a simple **Canary Deployment** strategy using two versions of a Flask application, Docker, Docker Compose, and NGINX.

## 📦 Project Structure

```
canary-demo/
├── v1/
│   └── app.py
├── v2/
│   └── app.py
├── nginx/
│   └── nginx.conf
├── docker-compose.yml
└── README.md
```

## 🚀 How It Works

- **aplication-v1**: Represents the stable production version.
- **aplication-v2**: Represents the new canary version.
- **NGINX**: Routes 80% of the traffic to v1 and 20% to v2 based on weights.
- **Docker Compose**: Orchestrates the services in a single command.

## 🧪 Running the Demo

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/DarrylMillan/canary_deployment.git
   cd canary-demo
   ```

2. **Start the Environment**:
   ```bash
   docker-compose up --build
   ```

3. **Test in Browser or Curl**:
   - The application will be available at [http://localhost:8080](http://localhost:8080)
   - Refresh multiple times to observe alternating responses from v1 and v2

4. **Stop the Environment**
   To stop the application, press `Ctrl+C` in the terminal where the containers are running, or use:

   ```bash
   docker-compose down
   ```

## 📝 Explanation of NGINX Canary Configuration

In `nginx/default.conf`:

```nginx
upstream backend {
    server app-v1:5000 weight=8;
    server app-v2:5000 weight=2;
}
```

This means:
- `app-v1` receives 80% of traffic
- `app-v2` receives 20% of traffic

## 📌 License

This project is licensed under the MIT License.
