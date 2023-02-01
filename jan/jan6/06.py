import json
from pprint import pprint

# 아래 코드 수정 금지
movies_json = open("data/movies.json", encoding="UTF8")
movies_list = json.load(movies_json)

# 이하 문제 해결을 위한 코드 작성

movie_spec = []

for i in range(len(movies_list)):
    movie_info = {}
    movie_info["id"] = movies_list[i]["id"]
    movie_info["title"] = movies_list[i]["title"]
    movie_info["vote_average"] = movies_list[i]["vote_average"]
    movie_info["overview"] = movies_list[i]["overview"]
    movie_info["genre_ids"] = movies_list[i]["genre_ids"]
    movie_spec.append(movie_info)

pprint(movie_spec)

