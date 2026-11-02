
# Cloud Server Monitoring Dashboard

A beginner Cloud/DevOps portfolio project built
using Python, Streamlit, Docker, and psutil.

## Features
- Live CPU, RAM, and disk monitoring
- Automatic refresh every 5 seconds
- Historical resource usage graphs
- Resource usage alerts
- Docker containerization

## Technologies
- Python
- Streamlit
- psutil
- Pandas
- Docker

## Run locally

pip install -r requirements.txt
streamlit run app.py

## Run with Docker

docker build -t cloud-monitor:v1 .
docker run --rm -p 8501:8501 cloud-monitor:v1

Open http://localhost:8501

## Monitoring limitations
When running inside Docker, metrics reflect the
Linux/container environment and may not represent
the Windows host's actual resource usage.

## Future Improvements
- Container-specific metrics
- Persistent monitoring history
- Automated tests and CI/CD
- Cloud deployment
