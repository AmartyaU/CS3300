import json

map_id_to_categories = {}
with open('./categories.json') as categories_file:
    categories = json.load(categories_file)
    for item in categories["items"]:
        map_id_to_categories.update({item["id"]: item["snippet"]["title"]})

with open('./map_id_to_categories.json', 'w') as json_file:
  json.dump(map_id_to_categories, json_file)
  print("successfully created map_id_to_categories")
    

dirs = ['./most_popular_youtube_videos_usa_page1.json',
        './most_popular_youtube_videos_usa_page2.json',
        './most_popular_youtube_videos_usa_page3.json',
        './most_popular_youtube_videos_usa_page4.json']

results = []

for dir in dirs:
    with open(dir) as youtube_videos:
        data = json.load(youtube_videos)
        results = results + data["items"]

for result in results:
    result["snippet"]["category"] = map_id_to_categories[result["snippet"]["categoryId"]]

print(results)

with open('./all_most_popular_youtube_videos_usa_page.json', 'w') as file_200:
  json.dump(results, file_200)
  print("successfully created all_most_popular_youtube_videos_usa_page.json")
