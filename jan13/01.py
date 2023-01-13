import requests


def popular_count():
    pass 
    # 여기에 코드를 작성합니다.  
    api_key = 'cf32eb0e2978ac40e34b0ca072bb8599'
    url = f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}'

    res = requests.get(url=url).json()
    result = res['results']
    popular = len(result)

    return popular


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
