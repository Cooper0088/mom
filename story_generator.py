import random

settings = {
    "genres": ["fantasy", "sci-fi", "horror", "romance", "mystery"],
    "protagonists": ["a reluctant hero", "an exiled prince", "a rogue AI", "a small-town detective", "a time traveler"],
    "goals": ["save the world", "uncover the truth", "find a lost artifact", "escape a doomed city", "break a curse"],
    "twists": ["a trusted ally is the villain", "the mission was a lie", "they are not human", "time resets", "the enemy is future self"]
}


def generate_story():
    genre = random.choice(settings["genres"])
    protagonist = random.choice(settings["protagonists"])
    goal = random.choice(settings["goals"])
    twist = random.choice(settings["twists"])

    return f"In a {genre} world, {protagonist} must {goal}, only to discover that {twist}."


if __name__ == "__main__":
    for _ in range(5):
        print(generate_story())
