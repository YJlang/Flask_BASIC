# Flask와 MySQL을 활용한 웹 애플리케이션 🚀

## 프로젝트 소개
이 프로젝트는 Flask 프레임워크와 MySQL을 사용하여 구현한 간단한 사용자 관리 시스템입니다. 웹 개발의 기초를 학습하고 실습하기 위한 목적으로 제작되었습니다.

## 기술 스택
### Backend
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=Flask&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=MySQL&logoColor=white)

### Frontend
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=HTML5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=CSS3&logoColor=white)

## 주요 기능
- 사용자 등록
- 사용자 목록 조회
- 데이터베이스 연동

## 프로젝트 구조
```
project/
├── static/           # 정적 파일 (CSS)
│   └── style.css
├── templates/        # HTML 템플릿
│   ├── base.html    # 기본 템플릿
│   ├── index.html   # 메인 페이지
│   └── users.html   # 사용자 목록 페이지
├── app.py           # 메인 애플리케이션
├── requirements.txt  # 의존성 목록
└── README.md        # 프로젝트 설명
```

## 설치 방법
1. 저장소 클론
```bash
git clone https://github.com/[사용자명]/[저장소명].git
cd [저장소명]
```

2. 가상환경 설정
```bash
python -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\activate
```

3. 의존성 설치
```bash
pip install -r requirements.txt
```

4. MySQL 설정
```sql
CREATE DATABASE practice;
USE practice;
```

5. 환경 변수 설정
```
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=practice
```

## 실행 방법
```bash
python app.py
```
서버 실행 후 `http://localhost:5000`으로 접속

## 학습 내용
1. **Flask 기초**
   - 라우팅
   - 템플릿 엔진 (Jinja2)
   - 정적 파일 관리

2. **데이터베이스**
   - MySQL 연결 설정
   - 기본 CRUD 작업
   - 커서 활용

3. **웹 개발 기초**
   - HTTP 메소드 (GET, POST)
   - 폼 데이터 처리
   - 템플릿 상속

## 향후 개선 계획
- [ ] 사용자 정보 수정 기능
- [ ] 사용자 삭제 기능
- [ ] 로그인/회원가입 기능
- [ ] 페이지네이션 구현
- [ ] 검색 기능 추가

## 제작자
- 윤준하
- Email: [이메일 주소](sean111400@naver.com)
- Blog: [블로그 주소](https://velog.io/@wnsgk111400)

## 참고 자료
- [Flask 공식 문서](https://flask.palletsprojects.com/)
- [MySQL 공식 문서](https://dev.mysql.com/doc/)
- [Python MySQL Connector 문서](https://dev.mysql.com/doc/connector-python/en/)

---
⭐ 이 프로젝트가 도움이 되었다면 스타를 눌러주세요!
