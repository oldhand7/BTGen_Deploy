from fastapi import FastAPI
from prometheus_client import start_http_server, Gauge
import GPUtil
import time
import os

app = FastAPI()

# Metrics to expose
system_health = Gauge('system_health', 'Health of the system (1 = healthy, 0 = unhealthy)')
gpu_health = Gauge('gpu_health', 'Health of the GPU (1 = healthy, 0 = unhealthy)')

@app.get("/health")
def get_health():
    return {
        "system_health": check_system_health(),
        "gpu_health": check_gpu_health()
    }

def check_system_health():
    try:
        total, used, free = os.popen('df / --output=pcent').read().split()[1:4]
        free_percent = int(free.strip('%'))
        return 1 if free_percent > 10 else 0
    except Exception as e:
        print(f"Error checking system health: {e}")
        return 0

def check_gpu_health():
    try:
        gpus = GPUtil.getGPUs()
        if not gpus:
            return 0
        gpu = gpus[0]
        return 1 if gpu.load < 0.99 else 0
    except Exception as e:
        print(f"Error checking GPU health: {e}")
        return 0

if __name__ == "__main__":
    # Serve Prometheus metrics
    start_http_server(8001)
    # Serve FastAPI endpoints
    uvicorn.run(app, host="0.0.0.0", port=9090)
