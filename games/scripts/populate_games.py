from games.models import Game


def run():
    games = [
        # --- PlayStation ---
        {
            "title": "God of War: Ragnarök",
            "description": "Kratos and Atreus face the end of the world in Norse mythology.",
            "price": 69.99,
            "stock": 10,
            "platform": "PS",
            "cover": "games/covers/god_of_war_ragnarok.jpg",
        },
        {
            "title": "Spider-Man 2",
            "description": "Peter Parker and Miles Morales team up to protect New York.",
            "price": 69.99,
            "stock": 8,
            "platform": "PS",
            "cover": "games/covers/spider_man_2.jpg",
        },
        {
            "title": "Hollow Knight",
            "description": "Explore a vast, ruined kingdom of insects beneath the earth.",
            "price": 14.99,
            "stock": 15,
            "platform": "PS",
            "cover": "games/covers/hollow_knight.jpg",
        },

        # --- Xbox ---
        {
            "title": "Halo Infinite",
            "description": "Master Chief returns to save humanity once again.",
            "price": 59.99,
            "stock": 12,
            "platform": "XB",
            "cover": "games/covers/halo_infinite.jpg",
        },
        {
            "title": "Forza Horizon 5",
            "description": "Drive through the open world of Mexico in stunning detail.",
            "price": 59.99,
            "stock": 10,
            "platform": "XB",
            "cover": "games/covers/forza_horizon_5.jpg",
        },
        {
            "title": "Starfield",
            "description": "Explore the stars in Bethesda's next-generation RPG.",
            "price": 69.99,
            "stock": 7,
            "platform": "XB",
            "cover": "games/covers/starfield.jpg",
        },

        # --- Nintendo Switch ---
        {
            "title": "The Legend of Zelda: Tears of the Kingdom",
            "description": "Explore the skies and depths of Hyrule in this epic adventure.",
            "price": 69.99,
            "stock": 10,
            "platform": "NS",
            "cover": "games/covers/zelda_totk.jpg",
        },
        {
            "title": "Metroid Dread",
            "description": "Samus Aran faces new horrors on planet ZDR.",
            "price": 59.99,
            "stock": 9,
            "platform": "NS",
            "cover": "games/covers/metroid_dread.jpg",
        },
        {
            "title": "Hollow Knight: Silksong",
            "description": "Play as Hornet in the anticipated sequel to Hollow Knight.",
            "price": 29.99,
            "stock": 20,
            "platform": "NS",
            "cover": "games/covers/silksong.jpg",
        },
    ]

    for g in games:
        Game.objects.update_or_create(title=g["title"], defaults=g)

    print("✔️ Games seeded successfully!")
