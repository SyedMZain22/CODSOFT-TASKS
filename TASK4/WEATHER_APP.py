import requests
from bs4 import BeautifulSoup
#Task 04
#syed muhammad zain bin faisal
def weather_app(query):
    try:
        url = f'https://www.google.com/search?q=wheater+{query}'
        req = requests.get(url)
        req.raise_for_status()
        soup = BeautifulSoup(req.text, 'html.parser')
        tem_element=soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'})
        desc_=soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'})

        if tem_element and desc_:
           weather_ = tem_element.text
           descrip = desc_.text

           return weather_,descrip
        else:
           return "Data not found", "Data not found"
    except requests.exceptions.RequestException as e:
        print("An error occurred while making the request:", e)
        return "N/A", "N/A"
    except Exception as e:
        print("An error occurred:", e)
        return "N/A", "N/A"

def extra_info(url):
    U_AGENT="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
    LAN = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = U_AGENT
    session.headers['Accept-Language'] = LAN
    session.headers['Content-Language'] = LAN
    html = session.get(url)
    soup = BeautifulSoup(html.text, "html.parser")
    result = {}
    result['precipitation']=soup.find("span", attrs={"id": "wob_pp"}).text
    result['humidity']=soup.find("span", attrs={"id": "wob_hm"}).text
    result['wind']=soup.find("span", attrs={"id": "wob_ws"}).text
    return result

if __name__ == "__main__":
    while True:
        query = input('enter the query:')
        URL = f'https://www.google.com/search?q=wheater+{query}'
        data = extra_info(URL)
        weather_, descrip = weather_app(query)
        print("________________________________")
        print('Temparature : ', weather_)
        print('Description: ', descrip)
        print("Precipitation:", data.get("precipitation", "N/A"))
        print("Humidity:", data.get("humidity", "N/A"))
        print("Wind:", data.get("wind", "N/A"))


