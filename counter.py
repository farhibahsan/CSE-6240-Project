import json
from collections import Counter
import numpy as np

def statistics(filename, outfile):
    f = open(filename)
    data = json.load(f)
    f.close()

    num_comments = 0
    users = set()
    comments_per_user = Counter()
    replies = 0
    comment_len = []

    for entry in data:
        # print(entry)
        if entry["retrieved_on"] == 0:
            continue

        if str(entry["link_id"]) == str(entry["parent_id"]):
            replies += 1

        num_comments += 1

        author = entry['author']
        users.add(author)
        
        comments_per_user[author] += 1
        comment_len.append(len(str(entry["body"])))

    num_users = len(users)
    vals = np.array(list(comments_per_user.values()))
    avg = np.mean(list(vals))
    avg_length = np.mean(np.array(comment_len))

    output = open(outfile, 'w')
    output.write("num_comments: ")
    output.write(str(num_comments))
    output.write("\n")
    output.write("num_users: ")
    output.write(str(num_users))
    output.write("\n")
    output.write("Average comments per user: ")
    output.write(str(avg))
    output.write("\n")
    output.write("Average length of comment: ")
    output.write(str(avg_length))
    output.write("\n")
    output.write("Number that are replies to another comment: ")
    output.write(str(replies))
    output.write("\n")
    output.close()

# statistics("test.json", "test.txt")
statistics("sandersforpresident.json", "sanders_stats.txt")