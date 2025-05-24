
진격의 거인 게임 만들기
# game-project-aot

진격의 거인 세계관을 기반으로 한 2D 스토리형 게임입니다.  
사용자는 벽 안쪽으로 후퇴하며 각 스테이지를 클리어해야 하며,  
각 단계는 오프닝 → 게임 진행 → 엔딩으로 구성됩니다.

---

## 🎮 게임 소개

| 항목       | 내용                          |
|------------|-------------------------------|
| 장르       | 스토리형 퍼즐 + 액션 요소     |
| 플랫폼     | PC (Python 실행 환경)         |
| 언어       | Python 3.10+, Pygame          |
| 개발 인원  | 3명 (진서, 승인, 도훈)        |

---

## 🔧 설치 및 실행 방법

1. 프로젝트 클론
```bash
git clone https://github.com/jinseo1222/aot-game-project.git
cd aot-game-project
````

2. 필요한 패키지 설치 (가상환경 권장)

```bash
pip install -r requirements.txt
```

3. 게임 실행

```bash
python main.py
```

---

## 📁 폴더 및 파일 설명

| 이름                 | 설명                         |
| ------------------ | -------------------------- |
| `main.py`          | 게임 실행 시작점 (전체 흐름 제어)       |
| `opening.py`       | 오프닝 화면 출력 및 버튼 처리          |
| `game.py`          | 본편 게임 로직 (맵, 캐릭터 이동 등)     |
| `ending.py`        | 엔딩 장면 출력                   |
| `graphics/`        | 게임 이미지 리소스 (배경, 캐릭터 등)     |
| `sounds/`          | 게임 사운드 리소스 (효과음, 배경음악)     |
| `fonts/`           | 폰트 리소스                     |
| `README.md`        | 프로젝트 설명 문서                 |
| `.gitignore`       | Git에서 제외할 파일 목록            |
| `requirements.txt` | 필요한 파이썬 패키지 목록 (예: pygame) |

---

## 👥 팀원 역할 분담

| 이름 | 담당 기능           |
| -- | --------------- |
| 진서 | 미니게임3,오프닝,스토리출력 |
| 승인 | 미니게임2,     |
| 도훈 | 미니게임1,   |

---

## 📌 협업 규칙 

### 🔀 브랜치 전략

* `main`: 최종 배포용 (건들지 않기)
* `develop`: 통합 작업 브랜치(request에서 팀원 코드 리뷰 후 업로드)
* `feature/기능명`: 각자 기능 개발용 (예: `feature/opening`)


### 💼 작업 흐름

```bash
git checkout -b feature/기능명
# 작업 후
git add .
git commit -m "작업 설명"
git push origin feature/기능명
```

### 🔁 Pull Request 규칙

* base: `develop`, compare: `feature/기능명`
* 제목 예시: `[feature/opening] 오프닝 버튼 기능 추가`
* 팀원 코드 리뷰 후 `develop`으로 병합

### 📝 커밋 메시지 규칙

| 이모지 | 의미      | 예시                    |
| --- | ------- | --------------------- |
| ✨   | 기능 추가   | `✨ 캐릭터 점프 기능 추가`      |
| 🐛  | 버그 수정   | `🐛 사운드 반복 버그 수정`     |
| ♻️  | 코드 리팩토링 | `♻️ opening.py 구조 개선` |

### 🎨 코드 스타일

* 들여쓰기: 공백 4칸 (space)
* 변수/함수명: 소문자 + 언더바 사용(ex.player_move, load_image)
* 클래스명: 단어마다 대문자(ex.GameManager, Stage1, OpeningScene)
* 상수명: 대문자+언더바(ex.SCREEN_WIDTH=1300, WHITE=(255,255,255)
* 줄바꿈: 함수, 클래스 사이 한 줄 이상 띄기
* 주석: 함수, 클래스 위에 간단히 기능 설명, 복잡한 로직 옆에 간단히 기능 설명
* 파일명: 소문자+언더바(ex.graphics_image.png), 대문자나 띄어쓰기 사용x, 클래스명과 파일명 통일(대문자는 소문자화)
* 문자열 따옴표: "쌍따옴표" 사용
* 코드 스타일 정리 도구 black: pip install black

### 🧠 기타 규칙

* `.gitignore` 파일은 삭제/수정 금지
* 리소스 경로 통일: `graphics/`, `sounds/`, `fonts/`
* 매일 `git pull origin develop`으로 최신 코드 받아오기
* 한 파일에는 하나의 클래스만

---

## 🏁 개발 목표 체크리스트

* [x] 오프닝 화면 구성
* [x] 캐릭터 이동 구현
* [ ] 충돌 감지 추가
* [ ] 사운드 효과 적용
* [ ] 엔딩 장면 구현
* [ ] 스테이지1
* [ ] 스테이지2
* [ ] 스테이지3
* [ ] 

---



