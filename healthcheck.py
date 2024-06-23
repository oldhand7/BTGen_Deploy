from fastapi import FastAPI
from pydantic import BaseModel
import subprocess

app = FastAPI()

class HealthCheckResponse(BaseModel):
    vps_status: str
    gpu_status: str

def check_gpu():
    try:
        # Execute the nvidia-smi command to check GPU status
        result = subprocess.run(['nvidia-smi'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode != 0:
            return 'error', result.stderr.decode('utf-8')
        
        # Process the output to determine GPU availability
        output = result.stdout.decode('utf-8')
        if 'No devices were found' in output:
            return 'unavailable', 'No GPU devices found'
        
        return 'available', output
    except Exception as e:
        return 'error', str(e)

@app.get("/health", response_model=HealthCheckResponse)
def health_check():
    vps_status = "healthy"
    gpu_status, gpu_details = check_gpu()
    return HealthCheckResponse(vps_status=vps_status, gpu_status=gpu_status)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8889)
