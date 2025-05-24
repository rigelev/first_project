from Button import Button

SCREEN_WIDTH = 1534
SCREEN_HEIGHT = 950

# Define constants for file paths
GRAPHICS_PATHS = {
    "start_button": "graphics/game_start_button.png",#버튼 픽셀 그림판 200
    "yes_button": "graphics/yes_button.png",
    "no_button": "graphics/no_button.png"
}

class ButtonManager:
    def __init__(self):
        self.buttons = {}

    def load_buttons(self):
        self.buttons["start"] = Button(GRAPHICS_PATHS["start_button"], (SCREEN_WIDTH//2-150, 700))
        self.buttons["yes"]   = Button(GRAPHICS_PATHS["yes_button"], (SCREEN_WIDTH//2-100, 600))
        self.buttons["no"]    = Button(GRAPHICS_PATHS["no_button"],  (SCREEN_WIDTH//2-100, 700))

    def get(self, name):
        return self.buttons.get(name)

    def draw(self, screen, *names):
        for name in names:
            btn = self.get(name)
            if btn:
                btn.draw(screen)

    def check_click(self, events, name):
        btn = self.get(name)
        return btn.is_clicked(events) if btn else False
