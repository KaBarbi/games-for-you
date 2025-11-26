from games.models import Game


def run():
    games = [
        # --- Novos Jogos ---

        # Xbox
        {
            "title": "Gears 5",
            "description": "Kait Diaz searches for answers about the Locust origins in this action-packed Gears chapter.",
            "price": 29.99,
            "stock": 20,
            "platform": "XB",
            "cover": "gears_5.jpg",
        },

        # PlayStation
        {
            "title": "The Last of Us Part II",
            "description": "Ellie embarks on a harrowing journey driven by trauma, survival, and moral complexity.",
            "price": 39.99,
            "stock": 18,
            "platform": "PS",
            "cover": "the_last_of_us_2.jpg",
        },

        # Nintendo Switch
        {
            "title": "Super Mario Odyssey",
            "description": "Join Mario and Cappy as they travel across imaginative worlds to rescue Princess Peach.",
            "price": 49.99,
            "stock": 25,
            "platform": "NS",
            "cover": "super_mario_odyssey.jpg",
        },

    ]

    for g in games:
        Game.objects.update_or_create(title=g["title"], defaults=g)

    print("✔️ Games seeded successfully!")
