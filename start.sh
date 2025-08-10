#!/bin/bash

# Start FastAPI backend in the background
uvicorn backend.main:app --host 0.0.0.0 --port 8000 &

# Start Streamlit frontend
streamlit run frontend/app.py --server.address 0.0.0.0 --server.port 8501 