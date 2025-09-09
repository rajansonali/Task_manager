import requests

# Flask API endpoint
url = "http://127.0.0.1:5000/api/tasks/2/comments"

while True:
    # Ask for user input
    content = input("Enter comment content (or 'q' to quit): ")
    if content.lower() == "q":
        print("Exiting.")
        break

    author = input("Enter author name: ")

    # Prepare data
    data = {"content": content, "author": author}

    try:
        # Send POST request
        response = requests.post(url, json=data)

        if response.status_code in (200, 201):
            print("✅ Comment added successfully!")
            try:
                print("Response from server:", response.json())
            except:
                print("Response text:", response.text)
        else:
            print(f"⚠️ Failed to add comment. Status code: {response.status_code}")
            print("Server response:", response.text)

    except requests.exceptions.RequestException as e:
        print("❌ Error connecting to the server:", e)
