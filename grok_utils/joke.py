import random

def get_joke():
    jokes = [
        "Почему программисты путают Хеллоуин и Рождество? Потому что Oct 31 == Dec 25!",
        "— Как называется группа программистов? — Код-код.",
        "Почему Python так популярен? Потому что он не требует ; в конце!"
    ]
    return random.choice(jokes)

if __name__ == "__main__":
    print("😂", get_joke())