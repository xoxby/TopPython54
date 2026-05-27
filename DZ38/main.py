import requests
import json
from datetime import UTC, datetime


url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)
posts = json.loads(response.text)

total_posts = len(posts)
posts_per_user = {}
body_lengths = []
title_lengths = []
top_longest_posts = []
max_total_length = 0

for post in posts:
    user_id = post["userId"]

    if user_id in posts_per_user:
        posts_per_user[user_id] += 1
    else:
        posts_per_user[user_id] = 1

    body_lengths.append(len(post["body"]))
    title_lengths.append(len(post["title"]))

    total_length = len(post["title"]) + len(post["body"])

    if total_length > max_total_length:
        max_total_length = total_length
        top_longest_posts = [
            {
                "id": post["id"],
                "userId": post["userId"],
                "total_length": total_length,
            }
        ]
    elif total_length == max_total_length:
        top_longest_posts.append(
            {
                "id": post["id"],
                "userId": post["userId"],
                "total_length": total_length,
            }
        )

most_active_user_id = 0
max_posts = 0

for user_id, count in posts_per_user.items():
    if count > max_posts:
        max_posts = count
        most_active_user_id = user_id

title_lengths.sort()
middle = len(title_lengths) // 2

if len(title_lengths) % 2 == 0:
    median_title_length = (title_lengths[middle - 1] + title_lengths[middle]) / 2
else:
    median_title_length = title_lengths[middle]

users = []

for user_id, count in sorted(posts_per_user.items()):
    users.append(
        {
            "userId": user_id,
            "posts_count": count,
        }
    )

report = {
    "generated_at": datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ"),
    "source": url,
    "summary": {
        "total_posts": total_posts,
        "avg_body_length": round(sum(body_lengths) / total_posts, 2),
        "most_active_user_id": most_active_user_id,
        "median_title_length": median_title_length,
    },
    "posts_per_user": users,
    "top_longest_posts": top_longest_posts,
}

with open("report.json", "w") as data_file:
    json.dump(report, data_file, indent=2)

print("Отчет сохранен в файл report.json")
print("Количество постов:", total_posts)
print("Средняя длина body:", report["summary"]["avg_body_length"])
print("Самый активный userId:", most_active_user_id)
print("Медианная длина title:", median_title_length)
