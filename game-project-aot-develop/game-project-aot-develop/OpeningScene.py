import pygame
import sys
import os
from ButtonManager import ButtonManager

# 기본 설정
SCREEN_WIDTH = 1534
SCREEN_HEIGHT = 950
FPS = 60
FONT_PATH = "graphics/dunggeunmo.ttf"

# 스토리 텍스트
STORY_TEXTS = [
    "어느 날 갑자기 출현한 정체불명의 식인종 거인들에 의해 인류의 태반이 잡아 먹히며 인류는 절멸 위기에 처한다.",
    "목숨을 부지한 생존자들은 높이 50m의 거대한 삼중의 벽 월 로제, 월 마리아, 월 시나를 건설한다.",
    "그곳으로 도피, 방벽 내부에서 100여 년에 걸쳐 평화의 시대를 영위하게 된다.",
    "그러던 어느날...",
    "초대형 거인이 뚫은 월 마리아의 구멍으로 들어온 거인들에게 수많은 민간인들이 죽임을 당한다",
    "당신은 살아남기 위해 월 로제로 대피해야한다."
]

class OpeningScene:
    """게임 시작 전 오프닝 씬 관리"""
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("진격의 거인")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(FONT_PATH, 36)

        # 배경 이미지
        self.opening_img = pygame.image.load("graphics/opening1.png").convert()

        # 버튼 매니저 초기화 및 버튼 로드
        self.ButtonManager = ButtonManager()
        self.ButtonManager.load_buttons()

        # 상태 변수: start → story → select
        self.state = "start"
        self.story_index = 0

    def wrap_text(self, text, max_chars):
        """지정된 글자 수마다 줄바꿈하여 리스트 반환"""
        return [text[i:i+max_chars] for i in range(0, len(text), max_chars)]

    def draw_start(self):
        """게임 시작 화면 그리기"""
        self.screen.blit(self.opening_img, (0, 0))
        self.ButtonManager.draw(self.screen, "start")

    def draw_story(self):
        """스토리 설명 텍스트 출력 화면"""
        self.screen.fill((0, 0, 0))
        lines = self.wrap_text(STORY_TEXTS[self.story_index], 40)
        total_height = len(lines) * 45
        y0 = (SCREEN_HEIGHT - total_height) // 2

        for i, line in enumerate(lines):
            rendered = self.font.render(line, True, (255, 255, 255))
            rect = rendered.get_rect(center=(SCREEN_WIDTH // 2, y0 + i * 45))
            self.screen.blit(rendered, rect)

    def draw_select(self):
        """게임 시작 여부 선택 화면"""
        self.screen.fill((0, 0, 0))
        question = self.font.render("게임을 플레이 하시겠습니까?", True, (255, 255, 255))
        self.screen.blit(question, question.get_rect(center=(SCREEN_WIDTH // 2, 425)))
        self.ButtonManager.draw(self.screen, "yes", "no")

    def run(self):
        """오프닝 메인 루프"""
        while True:
            self.clock.tick(FPS)
            events = pygame.event.get()

            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # 시작 버튼 클릭 → 스토리 화면으로 이동
                if self.state == "start" and self.ButtonManager.check_click(events, "start"):
                    self.state = "story"

                # 스토리 진행: 엔터 키 → 다음 텍스트, 마지막 → 선택 화면
                elif self.state == "story" and event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.story_index += 1
                        if self.story_index >= len(STORY_TEXTS):
                            self.state = "select"

                # 선택 화면: 버튼 클릭으로 진행 여부 결정
                elif self.state == "select":
                    if self.ButtonManager.check_click(events, "yes"):
                        print("게임 시작!")
                        return  # game.py 실행으로 넘어갈 위치
                    elif self.ButtonManager.check_click(events, "no"):
                        pygame.quit()
                        sys.exit()

            # 현재 상태에 따라 화면 출력
            if self.state == "start":
                self.draw_start()
            elif self.state == "story":
                self.draw_story()
            elif self.state == "select":
                self.draw_select()

            pygame.display.update()


if __name__ == "__main__":
    OpeningScene().run()


