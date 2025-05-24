import pygame


class Button:
    """단일 버튼 클래스 (이미지 크기 고정, 클릭 시 어두운 효과)"""
    def __init__(self, image_path, pos):
        try:
            self.original_image = pygame.image.load(image_path).convert_alpha()
        except Exception as e:
            print(f"이미지 로드 실패: {image_path}, 에러: {e}")
            # 임시로 빨간 사각형 생성
            self.original_image = pygame.Surface((200, 80))
            self.original_image.fill((255, 0, 0))
        self.clicked_image = self._darken_image(self.original_image.copy(), amount=40)
        self.image = self.original_image
        self.rect = self.image.get_rect(topleft=pos)

    def _darken_image(self, image, amount):
        """클릭 시 어두워진 이미지 생성"""
        dark_surface = pygame.Surface(image.get_size()).convert_alpha()
        dark_surface.fill((0, 0, 0, amount))
        image.blit(dark_surface, (0, 0))
        return image

    def draw(self, screen):
        """버튼을 화면에 그림"""
        screen.blit(self.image, self.rect)

    def is_clicked(self, events):
        """클릭 감지"""
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.rect.collidepoint(event.pos):
                    return True
        return False
