# app.py

from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# OpenWeatherMap API 키
weather_api_key = '37adc8129abdd68ca2d674bd5ca9c522'

# 지역 정보와 해당 지역의 좌표를 딕셔너리로 정의
locations = {
    '서울': {'lat': 37.5665, 'lon': 126.9780},
    '부산': {'lat': 35.1796, 'lon': 129.0756},
    '인천': {'lat': 37.4563, 'lon': 126.7052},
    '제주': {'lat': 33.4996, 'lon': 126.5312},
    '경주': {'lat': 35.8563, 'lon': 129.2245},
    '대전': {'lat': 36.3504, 'lon': 127.3845},
    '광주': {'lat': 35.1595, 'lon': 126.8526},
    '울산': {'lat': 35.5384, 'lon': 129.3114},
    '수원': {'lat': 37.2636, 'lon': 127.0286},
}

@app.route('/')
def index():
    return render_template('index.html', locations=locations)

@app.route('/weather/<location>')
def weather(location):
    # OpenWeatherMap API를 사용하여 현재 날씨 정보 가져오기
    lat = locations[location]['lat']
    lon = locations[location]['lon']
    weather_api_url = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={weather_api_key}&units=metric'
    weather_data = requests.get(weather_api_url).json()

    # 필요한 날씨 정보 가져오기
    temperature = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    precipitation = weather_data.get('rain', {}).get('1h', 0)  # 1시간 동안의 강수량, 없을 경우 0으로 처리
    weather_status = weather_data['weather'][0]['main']

    return render_template('weather.html', location=location, temperature=temperature, humidity=humidity, precipitation=precipitation, weather_status=weather_status)

@app.route('/travel_advice/<location>')
def travel_advice(location):
    # 실제 데이터를 이용한 여행 조언 정보
    travel_advice_data = get_travel_advice_data(location)

    return render_template('travel_advice.html', location=location, travel_advice_data=travel_advice_data)

def get_travel_advice_data(location):
    # 여행 조언 데이터를 가져오는 함수
    # 이 함수를 통해 각 지역에 맞는 관광지와 축제 일정을 반환하도록 구현
    if location == '서울':
        return {
            'tourist_attractions': ['경복궁', '남산 타워', '인사동'],
            'festivals_schedule': ['서울 빛초롱 축제 - 5월', '서울 국제 불빛 등불 축제 - 11월'],
        }
    elif location == '부산':
        return {
            'tourist_attractions': ['해운대 해수욕장', '범어사', '부산 국제 영화제'],
            'festivals_schedule': ['부산 세계불꽃놀이대회 - 10월', '부산 국제 영화제 - 10월'],
        }
    elif location == '인천':
        return {
            'tourist_attractions': ['인천 차이나타운', '운서 영종도 카페 거리', '인천 대공원'],
            'festivals_schedule': ['인천 세계 송년놀이 대회 - 12월', '인천 영화 소리바다 - 4월'],
        }
    elif location == '제주':
        return {
            'tourist_attractions': ['한라산', '성산일출봉', '우도'],
            'festivals_schedule': ['제주 제천대제 - 2월', '제주 벚꽃 축제 - 4월'],
        }
    elif location == '경주':
        return {
            'tourist_attractions': ['불국사', '석굴암', '경주 동궁과 월지'],
            'festivals_schedule': ['경주 연등 축제 - 10월', '경주 세계문화엑스포 - 8월'],
        }
    elif location == '대전':
        return {
            'tourist_attractions': ['대전 엑스포과학공원', '한밭수목원', '대전 동구 이월드'],
            'festivals_schedule': ['대전 불화로 축제 - 5월', '대전 서대전네축제 - 9월'],
        }
    elif location == '광주':
        return {
            'tourist_attractions': ['광주 국립아시아문화전당', '매곡리 원예예술촌', '광주 양림동 동물원'],
            'festivals_schedule': ['광주 대한민국만화축제 - 5월', '광주 세계수영선수권대회 - 7월'],
        }
    elif location == '울산':
        return {
            'tourist_attractions': ['울산 대왕암공원', '울산 울산대교', '울산 강동성당'],
            'festivals_schedule': ['울산 팔공산 영상아트페스티벌 - 9월', '울산 부드럽게 체험하기 페스티벌 - 4월'],
        }
    elif location == '수원':
        return {
            'tourist_attractions': ['수원 화성', '수원 한옥마을', '수원남문시장'],
            'festivals_schedule': ['수원 화성 불교 음악회 - 8월', '수원 대한민국 국제 영화제 - 10월'],
        }

    # 다른 지역에 대한 데이터도 추가 가능

    # 만약 데이터가 없는 경우, 빈 데이터 반환
    return {
        'tourist_attractions': [],
        'festivals_schedule': [],
    }
if __name__ == '__main__':
    app.run(debug=True)
