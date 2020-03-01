import json

dirs = ['./most_popular_youtube_videos_usa_page1.json',
        './most_popular_youtube_videos_usa_page2.json',
        './most_popular_youtube_videos_usa_page3.json',
        './most_popular_youtube_videos_usa_page4.json']

result = []

for dir in dirs:
    with open(dir) as data1:
        data = json.load(data1)
        result = result + data["items"]

with open('./all_most_popular_youtube_videos_usa_page.json', 'w') as file_200:
  json.dump(result, file_200)
  print("success")
