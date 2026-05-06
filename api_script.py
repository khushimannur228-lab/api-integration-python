import requests
import datetime

# Logging function
def write_log(message):
    with open("api_log.txt", "a") as log_file:
        log_file.write(f"{datetime.datetime.now()} - {message}\n")

# Function to fetch data
def fetch_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    try:
        response = requests.get(url)
        response.raise_for_status()
        print("Data fetched successfully!\n")
        write_log("Fetched data successfully")
        return response.json()
    except Exception as e:
        print(f" Error: {e}")
        write_log(f"Error fetching data: {e}")
        return []

# Function to display posts
def display_posts(posts, limit=3):
    print(f"\nShowing first {limit} posts:\n")
    for i, post in enumerate(posts[:limit]):
        print(f"Post {i+1}:")
        print(f"ID: {post['id']}")
        print(f"Title: {post['title'][:50]}...")
        print(f"Body: {post['body'][:80]}...")
        print("-" * 30)

# Filter posts by userId
def filter_posts(posts, user_id):
    filtered = [post for post in posts if post['userId'] == user_id]
    write_log(f"Filtered posts for userId={user_id}")
    return filtered

# Main program
def main():
    posts = fetch_posts()

    if not posts:
        return

    print(f"Total posts fetched: {len(posts)}")

    # User input for number of posts
    try:
        limit = int(input("Enter number of posts to display: "))
    except:
        limit = 3

    display_posts(posts, limit)

    # User input for filtering
    choice = input("\nDo you want to filter by userId? (yes/no): ").lower()

    if choice == "yes":
        try:
            user_id = int(input("Enter userId (1-10): "))
            filtered = filter_posts(posts, user_id)

            print(f"\nPosts by userId {user_id}: {len(filtered)} found\n")
            display_posts(filtered, min(3, len(filtered)))
        except:
            print("Invalid input")

    print("\n Program completed.")
    write_log("Program completed")

# Run program
main()
