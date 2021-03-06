[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![](https://img.shields.io/badge/django-3.2.2-green)
![](https://img.shields.io/badge/HTML-pink)
![](https://img.shields.io/badge/CSS-blue)
![](https://img.shields.io/badge/JS-yellow)
![](https://img.shields.io/badge/Pillow-8.2.0-red)
![](https://img.shields.io/badge/Channels-3.0.3-pink)
![](https://img.shields.io/badge/ChannelsRedis-3.0.3-pink)


# Philo coder
CULTURE BOOK

## Contributor
- Likelion in Chungang University
 
|    Name    | Email                                        |
| :-----------: | :------------------------------------------------- |
|    최윤한(Leader)     |unusualc@likelion.org | 
|    인세훈(Developer)     | dlstpgns0406@gmail.com |
|    민정호(PM, Developer)     |alswjdgh5095@gmail.com |
|    박채연(Developer)     | pcy9472@gmail.com|
|    이성민(Developer)    | seongmin221@naver.com |
 
## Service
   
### Idea Description
- Our service provides information and booking system about Korean culture experiences. 
### Service Function
- Account : Supports `social login`
- Feed : show picture and review for customer to check experiences
- Finding : User can find experiences that they want using Kakao map API
- Reservation : Customer can book experience with payment system
### How to
```console
$ git clone https://github.com/LikeLion-CAU-9th/Philo-coders.git
$ git pull origin develop
$ python -m venv myvenv
$ source myvenv/scripts/activate  mac) source myvenv/bin/activate
$ cd Byurak
$ ./manage.py makemigrations
$ ./manage.py migrate
$ ./manage.py runserver
```
#### Module installation
```console
$ pip install -r requirements.txt
```
#### Set Module
```console
$ pip freeze > requirements.txt 
```

#### Docker
- if there is no `Redis` container
```bash
$ docker ps
```
```bash
$ docker run -p 6379:6379 -d redis:5
```

## Branch structure

### Main branch
* Master branch : It is Manage only the state that can be distributed
* Develop branch : It is Used to merge branches for feature development

### Secondary branch

* Feature branch : Branch to develop the function ex)feature/profile
* Fix branch : Branch to fix the function ex)fix/profile


## Commit rule
```console
git commit -m "text"
```

|    Keyword    | Description                                        |
| :-----------: | :------------------------------------------------- |
|    [feat]     | 코드나 테스트, 예제, 문서 등의 추가가 있을 때 사용 |
|  [refactor]   | 올바르지 않은 로직을 고친 경우에 사용              |
|    [style]    | 코드에 대한 스타일을 바꿀 때                       |
| [docs(guide)] | 문서 작업을 할 때                                  |
