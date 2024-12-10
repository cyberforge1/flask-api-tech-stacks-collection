# scripts/manual_endpoint_test.py

import requests

BASE_URL = "http://127.0.0.1:5001"

def test_helloworld_endpoint():
    print("Testing HelloWorld endpoint...")
    response = requests.get(f"{BASE_URL}/helloworld/")
    print("Response:", response.json())
    print("Status Code:", response.status_code)

def test_main_endpoint():
    print("\nTesting Main endpoint...")
    response = requests.get(f"{BASE_URL}/main/")
    print("Response:", response.json())
    print("Status Code:", response.status_code)

def test_todos_endpoints():
    print("\nTesting Todos endpoints...")

    # Test GET /todos/
    print("\nGET /todos/")
    response = requests.get(f"{BASE_URL}/todos/")
    print("Response:", response.json())
    print("Status Code:", response.status_code)

    # Test POST /todos/
    print("\nPOST /todos/")
    new_todo = {"title": "Learn Flask"}
    response = requests.post(f"{BASE_URL}/todos/", json=new_todo)
    print("Response:", response.json())
    print("Status Code:", response.status_code)

    # Save the new todo ID for future tests
    todo_id = response.json().get("todo", {}).get("id")

    if todo_id:
        # Test GET /todos/<id>/
        print(f"\nGET /todos/{todo_id}/")
        response = requests.get(f"{BASE_URL}/todos/{todo_id}/")
        print("Response:", response.json())
        print("Status Code:", response.status_code)

        # Test PUT /todos/<id>/
        print(f"\nPUT /todos/{todo_id}/")
        updated_todo = {"title": "Learn Flask RestX"}
        response = requests.put(f"{BASE_URL}/todos/{todo_id}/", json=updated_todo)
        print("Response:", response.json())
        print("Status Code:", response.status_code)

        # Test DELETE /todos/<id>/
        print(f"\nDELETE /todos/{todo_id}/")
        response = requests.delete(f"{BASE_URL}/todos/{todo_id}/")
        print("Response:", response.json())
        print("Status Code:", response.status_code)

        # Test GET /todos/<id>/ after deletion
        print(f"\nGET /todos/{todo_id}/ after deletion")
        response = requests.get(f"{BASE_URL}/todos/{todo_id}/")
        print("Response:", response.json())
        print("Status Code:", response.status_code)

def main():
    test_helloworld_endpoint()
    test_main_endpoint()
    test_todos_endpoints()

if __name__ == "__main__":
    main()
