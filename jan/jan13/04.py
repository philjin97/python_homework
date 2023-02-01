import requests
from pprint import pprint


def search_movie(title):
    pass
    # 여기에 코드를 작성합니다.
    api_key = 'cf32eb0e2978ac40e34b0ca072bb8599'
    url = f'https://api.themoviedb.org/3/search/movie/?api_key={api_key}'

    res = requests.get(url=url).json()
    result = res['results']
    for n in range(len(result)):
        if result[n]['title'] == title:
            return result[n]['id']

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id 반환
    검색한 결과 영화가 없다면 None을 반환
    """
    print(search_movie('기생충'))
    # 496243
    print(search_movie('그래비티'))
    # 959101
    print(search_movie('검색할 수 없는 영화'))
    # None
