# scripts/test_api_endpoints.py

import requests
import json

# Base URL of the Flask API
BASE_URL = "http://localhost:5001/api"

# Endpoints to test
ENDPOINTS = [
    {"path": "/", "method": "GET", "description": "Main welcome route"},
    {"path": "/helloworld", "method": "GET", "description": "Hello World route"},
    {"path": "/todos", "method": "GET", "description": "List all todos"},
    {"path": "/todos/{id}", "method": "GET", "description": "Get a todo by ID", "sample_data": {"id": 1}},
    {"path": "/todos", "method": "POST", "description": "Create a new todo", "sample_data": {"title": "New Todo"}},
    {"path": "/todos/{id}", "method": "PUT", "description": "Update a todo by ID", "sample_data": {"id": 1, "title": "Updated Todo"}},
    {"path": "/todos/{id}", "method": "DELETE", "description": "Delete a todo by ID", "sample_data": {"id": 1}},
]

def test_endpoint(endpoint, base_url=BASE_URL):
    """Tests an API endpoint with the given method and path."""
    path = endpoint["path"]
    method = endpoint["method"]
    description = endpoint["description"]
    sample_data = endpoint.get("sample_data", {})

    # Replace placeholders in path with sample data
    for key, value in sample_data.items():
        path = path.replace(f"{{{key}}}", str(value))

    url = f"{base_url}{path}"
    print(f"\nTesting {method} {url} - {description}")

    try:
        if method == "GET":
            response = requests.get(url)
        elif method == "POST":
            response = requests.post(url, json=sample_data)
        elif method == "PUT":
            response = requests.put(url, json=sample_data)
        elif method == "DELETE":
            response = requests.delete(url)
        else:
            raise ValueError(f"Unsupported method: {method}")

        if response.status_code in (200, 201):
            try:
                # Try parsing JSON
                content = response.json()
                print(f"Status: {response.status_code}")
                print("Response:", json.dumps(content, indent=4))
            except json.JSONDecodeError:
                print(f"Status: {response.status_code}")
                print("Response: Response is not valid JSON")
        elif response.status_code == 404:
            print(f"Status: {response.status_code}")
            print("Response: No data found")
        else:
            print(f"Status: {response.status_code}")
            print("Response:", response.text)
    except requests.RequestException as e:
        print(f"Status: ERROR")
        print(f"Response: Request failed: {e}")

def main():
    for endpoint in ENDPOINTS:
        test_endpoint(endpoint)

if __name__ == "__main__":
    main()
