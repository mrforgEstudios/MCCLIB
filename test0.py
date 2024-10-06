import pygame
import pygame.freetype
from minecraft_commands import MinecraftCommand

# Инициализация Pygame
pygame.init()

# Задаем размеры окна
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Minecraft Command Generator")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (0, 102, 204)

# Шрифты
FONT = pygame.freetype.SysFont("Arial", 24)

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
buttons = {
    "Set Block": pygame.Rect(50, 50, 200, 50),
    "Teleport": pygame.Rect(50, 110, 200, 50),
    "Give Item": pygame.Rect(50, 170, 200, 50),
    "Summon Entity": pygame.Rect(50, 230, 200, 50),
    "Effect": pygame.Rect(50, 290, 200, 50),
    "Clear Effect": pygame.Rect(50, 350, 200, 50),
    "Generate": pygame.Rect(300, 450, 200, 50),
    "Back": pygame.Rect(50, 500, 100, 50)  # Добавляем кнопку "Назад"
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
def draw_text(surface, text, pos, color=BLACK):
    FONT.render_to(surface, pos, text, color)

# Функция отрисовки меню выбора режима
def draw_menu():
    screen.fill(WHITE)
    draw_text(screen, "Choose a mode:", (300, 20))
    for text, rect in buttons.items():
        if text != "Generate" and text != "Back":  # Исключаем кнопки не из меню
            pygame.draw.rect(screen, GRAY, rect)
            draw_text(screen, text, (rect.x + 10, rect.y + 10))

# Функция отрисовки интерфейса для выбранного режима
def draw_mode_interface():
    screen.fill(WHITE)
    draw_text(screen, f"Mode: {current_mode}", (50, 20))

    # Отображение полей ввода для текущего режима
    for i, field in enumerate(input_fields):
        pygame.draw.rect(screen, WHITE, pygame.Rect(200, 70 + i * 50, 250, 30))  # Заливка белого фона
        pygame.draw.rect(screen, BLACK, pygame.Rect(200, 70 + i * 50, 250, 30), 2)  # Черная обводка
        draw_text(screen, f"{field.capitalize()}:", (50, 70 + i * 50))
        draw_text(screen, input_fields[field], (210, 75 + i * 50), BLUE)

    # Кнопка генерации и кнопка "Назад"
    pygame.draw.rect(screen, GRAY, buttons["Generate"])
    draw_text(screen, "Generate", (buttons["Generate"].x + 10, buttons["Generate"].y + 10))
    
    pygame.draw.rect(screen, GRAY, buttons["Back"])  # Кнопка "Назад"
    draw_text(screen, "Back", (buttons["Back"].x + 10, buttons["Back"].y + 10))

    # Отображение сгенерированных команд
    draw_text(screen, "Generated Command:", (150, 520))
    draw_text(screen, generated_commands, (150, 550), BLUE)

# Функция обработки выбора режима
def select_mode(mode):
    global current_mode, input_fields
    current_mode = mode
    input_fields = {field: "" for field in modes[mode]}

# Основной цикл программы
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if current_mode is None:
                # Проверка нажатия на кнопки в меню
                for mode in modes:
                    if buttons[mode].collidepoint(event.pos):
                        select_mode(mode)
            else:
                # Проверка нажатия на кнопки и поля ввода в режиме генерации
                if buttons["Generate"].collidepoint(event.pos):
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
                if buttons["Back"].collidepoint(event.pos):
                    current_mode = None  # Возвращаемся в меню

                # Проверка нажатия на поля ввода
                for i, field in enumerate(input_fields):
                    if 200 <= event.pos[0] <= 450 and 70 + i * 50 <= event.pos[1] <= 100 + i * 50:
                        active_input = field

        if event.type == pygame.KEYDOWN and active_input:
            if event.key == pygame.K_BACKSPACE:
                input_fields[active_input] = input_fields[active_input][:-1]
            else:
                input_fields[active_input] += event.unicode

    # Отрисовка интерфейса
    if current_mode is None:
        draw_menu()
    else:
        draw_mode_interface()

    # Обновление экрана
    pygame.display.flip()

pygame.quit()
