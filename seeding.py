import csv
import requests

api_url = 'http://balatro.virtualized.dev:4931/api/stats/leaderboard/1'

response = requests.get(api_url)
print("API responded")

f = list(response.json().get('leaderboard'))
data = [['Player','User ID','Score']]
table_path = 'main.csv'
number = 0

for i in f:
  number += 1
  user_id = int(i.get('id'))
  mmr = float(i.get('mmr'))
  user = str('a') * number
  a = [user, user_id, mmr]
  data.append(a)
  print("User #" + str(number + 1) + " recieved")

print("Starting to write data...")
with open(table_path, mode = 'w', newline = '') as file:
  writer = csv.writer(file)
  writer.writerows(data)

b = input("Finished! Press Enter to close this window.")
