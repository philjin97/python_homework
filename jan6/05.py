import json
from pprint import pprint

# 아래 코드 수정 금지
movie_json = open("data/movie.json", encoding="UTF8")
movie = json.load(movie_json)

# 이하 문제 해결을 위한 코드 작성
data = {}

data["id"] = movie["id"]
data["title"] = movie["title"]
data["vote_average"] = movie["vote_average"]
data["overview"] = movie["overview"]
data["genre_ids"] = movie["genre_ids"]

pprint(data)