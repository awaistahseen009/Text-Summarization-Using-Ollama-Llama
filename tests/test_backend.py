import pytest
from fastapi.testclient import TestClient
from backend.main import app
import requests_mock

client = TestClient(app)

@pytest.fixture
def mock_ollama():
    with requests_mock.Mocker() as m:
        yield m

def test_summarize_endpoint_success(mock_ollama):
    mock_ollama.post(
        "http://localhost:11434/api/generate",
        json={"response": "This is a mocked summary of the input text."}
    )
    response = client.post("/summarize/", data={"text": "Sample text to summarize. It's about foxes and dogs."})
    assert response.status_code == 200
    json_response = response.json()
    assert "summary" in json_response
    assert json_response["summary"] == "This is a mocked summary of the input text."

def test_summarize_endpoint_empty_input(mock_ollama):
    mock_ollama.post(
        "http://localhost:11434/api/generate",
        json={"response": ""}
    )
    response = client.post("/summarize/", data={"text": ""})
    assert response.status_code == 200
    assert response.json()["summary"] == ""  # Or handle as "No text provided" if you update the code

def test_summarize_endpoint_error(mock_ollama):
    mock_ollama.post(
        "http://localhost:11434/api/generate",
        status_code=500,
        json={"error": "Something went wrong"}
    )
    response = client.post("/summarize/", data={"text": "Test text"})
    assert response.status_code == 200  # FastAPI still returns 200, but summary might be error
    assert "error" in response.json()["summary"].lower()  # Adjust based on your error handling 