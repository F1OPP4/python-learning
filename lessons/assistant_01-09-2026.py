# 01.09.2026
# Учебный класс Assistant: хранение и вывод истории сообщений.

class Assistant:
    def __init__(self, name, model):
        self.name = name
        self.model = model
        self.messages = []

    def add_message(self, message):
        # Добавляем новое сообщение в историю.
        self.messages.append(message)

    def show_history(self):
        # Выводим все сообщения из истории по одному.
        for message in self.messages:
            print(message)

    def answer(self, message):
        # Сохраняем сообщение пользователя.
        self.add_message("Пользователь: " + message)

        # Формируем и сохраняем ответ ассистента.
        self.add_message(f"{self.name}: Я получил сообщение: {message}")


assistant = Assistant("Миша", "GPT")

assistant.answer("Привет")
assistant.answer("Как дела?")
assistant.answer("Что такое Python?")

assistant.show_history()
