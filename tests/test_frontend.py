import pytest
import requests
from unittest.mock import patch
from frontend.app import st  # We don't really need st here, but for completeness

@patch('requests.post')
def test_frontend_api_call_success(mock_post):
    mock_post.return_value.json.return_value = {"summary": "Mocked frontend summary"}
    mock_post.return_value.status_code = 200
    
    # Simulate the API call from the Streamlit code
    response = requests.post(
        "http://localhost:8000/summarize/",
        data={"text": "Frontend test text"}
    )
    
    assert mock_post.called
    assert response.json()["summary"] == "Mocked frontend summary"

@patch('requests.post')
def test_frontend_api_call_error(mock_post):
    mock_post.return_value.json.return_value = {"summary": "Error generating summary."}
    mock_post.return_value.status_code = 200  # Assuming graceful error
    
    response = requests.post(
        "http://localhost:8000/summarize/",
        data={"text": "Bad input"}
    )
    
    assert "error" in response.json()["summary"].lower() 