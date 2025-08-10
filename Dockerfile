FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/ backend/
COPY frontend/ frontend/

EXPOSE 8000 8501

# Create a script to run both FastAPI and Streamlit
COPY start.sh ./start.sh
RUN chmod +x start.sh

CMD ["./start.sh"] 