import pygame
import pygame.freetype
from minecraft_commands import MinecraftCommand

# Инициализация Pygame
pygame.init()

# Задаем размеры окна
SCREEN_WIDTH, SCREEN_HEIGHT = 1024, 768
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Minecraft Command Generator")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
LIGHT_BLUE = (173, 216, 230)
DARK_BLUE = (0, 102, 204)
GREEN = (0, 255, 0)

# Шрифты
FONT_LARGE = pygame.freetype.SysFont("Arial", 32)
FONT_MEDIUM = pygame.freetype.SysFont("Arial", 24)
FONT_SMALL = pygame.freetype.SysFont("Arial", 18)

# Инициализация командного генератора
mc_cmd = MinecraftCommand()

# Текущий режим генерации
current_mode = None

# Поля ввода и активные поля
input_fields = {}
active_input = None

# Генерация текста команд
generated_commands = ""

# Интерфейсные элементы
def create_button(text, x, y, width, height):
    return {"rect": pygame.Rect(x, y, width, height), "text": text, "color": LIGHT_BLUE}

buttons = {
    "Set Block": create_button("Set Block", 50, 100, 200, 60),
    "Teleport": create_button("Teleport", 270, 100, 200, 60),
    "Give Item": create_button("Give Item", 490, 100, 200, 60),
    "Summon Entity": create_button("Summon Entity", 50, 180, 200, 60),
    "Effect": create_button("Effect", 270, 180, 200, 60),
    "Clear Effect": create_button("Clear Effect", 490, 180, 200, 60),
    "Generate": create_button("Generate", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT - 100, 200, 60),
    "Back": create_button("Back", 50, SCREEN_HEIGHT - 100, 150, 60)
}

# Поля ввода по режимам
modes = {
    "Set Block": ["x", "y", "z", "block"],
    "Teleport": ["player", "x", "y", "z"],
    "Give Item": ["player", "item", "count"],
    "Summon Entity": ["entity", "x", "y", "z"],
    "Effect": ["player", "effect", "duration", "amplifier"],
    "Clear Effect": ["player", "effect"]
}

# Функция отображения текста
def draw_text(surface, text, pos, font=FONT_MEDIUM, color=BLACK):
    font.render_to(surface, pos, text, color)

# Функция отрисовки кнопки
def draw_button(surface, button, mouse_pos):
    color = GREEN if button["rect"].collidepoint(mouse_pos) else button["color"]
    pygame.draw.rect(surface, color, button["rect"], border_radius=10)
    pygame.draw.rect(surface, BLACK, button["rect"], 2, border_radius=10)
    text_rect = FONT_MEDIUM.get_rect(button["text"])
    pos = button["rect"].centerx - text_rect.width // 2, button["rect"].centery - text_rect.height // 2
    draw_text(surface, button["text"], pos)

# Функция отрисовки меню выбора режима
def draw_menu(mouse_pos):
    screen.fill(WHITE)
    draw_text(screen, "Minecraft Command Generator", (SCREEN_WIDTH // 2 - 200, 30), FONT_LARGE, DARK_BLUE)
    draw_text(screen, "Choose a mode:", (SCREEN_WIDTH // 2 - 70, 70))
    for button in buttons.values():
        if button["text"] not in ["Generate", "Back"]:
            draw_button(screen, button, mouse_pos)

# Функция отрисовки интерфейса для выбранного режима
def draw_mode_interface(mouse_pos):
    screen.fill(WHITE)
    draw_text(screen, f"Mode: {current_mode}", (50, 30), FONT_LARGE, DARK_BLUE)

    # Отображение полей ввода для текущего режима
    for i, field in enumerate(input_fields):
        pygame.draw.rect(screen, WHITE, pygame.Rect(250, 100 + i * 60, 300, 40))
        pygame.draw.rect(screen, BLACK, pygame.Rect(250, 100 + i * 60, 300, 40), 2)
        draw_text(screen, f"{field.capitalize()}:", (50, 105 + i * 60), FONT_MEDIUM)
        draw_text(screen, input_fields[field], (260, 105 + i * 60), FONT_MEDIUM, DARK_BLUE)

    # Кнопки "Generate" и "Back"
    draw_button(screen, buttons["Generate"], mouse_pos)
    draw_button(screen, buttons["Back"], mouse_pos)

    # Отображение сгенерированных команд
    pygame.draw.rect(screen, LIGHT_BLUE, (50, SCREEN_HEIGHT - 200, SCREEN_WIDTH - 100, 80), border_radius=10)
    draw_text(screen, "Generated Command:", (60, SCREEN_HEIGHT - 190), FONT_SMALL)
    draw_text(screen, generated_commands, (60, SCREEN_HEIGHT - 160), FONT_MEDIUM, DARK_BLUE)

# Функция обработки выбора режима
def select_mode(mode):
    global current_mode, input_fields
    current_mode = mode
    input_fields = {field: "" for field in modes[mode]}

# Основной цикл программы
running = True
while running:
    mouse_pos = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if current_mode is None:
                # Проверка нажатия на кнопки в меню
                for mode, button in buttons.items():
                    if button["rect"].collidepoint(event.pos) and mode in modes:
                        select_mode(mode)
            else:
                # Проверка нажатия на кнопки и поля ввода в режиме генерации
                if buttons["Generate"]["rect"].collidepoint(event.pos):
                    if current_mode == "Set Block":
                        mc_cmd.set_block(int(input_fields["x"]), int(input_fields["y"]), int(input_fields["z"]), input_fields["block"])
                    elif current_mode == "Teleport":
                        mc_cmd.teleport(input_fields["player"], int(input_fields["x"]), int(input_fields["y"]), int(input_fields["z"]))
                    elif current_mode == "Give Item":
                        mc_cmd.give_item(input_fields["player"], input_fields["item"], int(input_fields["count"]))
                    elif current_mode == "Summon Entity":
                        mc_cmd.summon_entity(input_fields["entity"], int(input_fields["x"]), int(input_fields["y"]), int(input_fields["z"]))
                    elif current_mode == "Effect":
                        mc_cmd.effect(input_fields["player"], input_fields["effect"], int(input_fields["duration"]), int(input_fields["amplifier"]))
                    elif current_mode == "Clear Effect":
                        mc_cmd.clear_effect(input_fields["player"], input_fields["effect"] if input_fields["effect"] else None)

                    generated_commands = mc_cmd.execute()

                # Проверка нажатия на кнопку "Назад"
                if buttons["Back"]["rect"].collidepoint(event.pos):
                    current_mode = None

                # Проверка нажатия на поля ввода
                for i, field in enumerate(input_fields):
                    if 250 <= event.pos[0] <= 550 and 100 + i * 60 <= event.pos[1] <= 140 + i * 60:
                        active_input = field

        if event.type == pygame.KEYDOWN and active_input:
            if event.key == pygame.K_BACKSPACE:
                input_fields[active_input] = input_fields[active_input][:-1]
            else:
                input_fields[active_input] += event.unicode

    # Отрисовка интерфейса
    if current_mode is None:
        draw_menu(mouse_pos)
    else:
        draw_mode_interface(mouse_pos)

    # Обновление экрана
    pygame.display.flip()

pygame.quit()