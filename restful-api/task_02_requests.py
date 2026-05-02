import requests
import json
import csv

def fetch_and_print_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        text = response.json()
        for post in text:
            print(post["title"])
    else:
        print("Failure")

def fetch_and_save_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        text = response.json()
        list = []
        for post in text:
            list.append({
                "id":post["id"],
                "title":post["title"],
                "body":post["body"]
            })
        with open("posts.csv", mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames = ["id", "title", "body"])
            writer.writeheader()
            writer.writerows(list)

        print("Posts successfully saved to posts.csv")
    else:
        print("Failed to fetch posts")
  
