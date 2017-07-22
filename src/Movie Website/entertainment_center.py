import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and a toy that come to life.",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster-jpg",
                     "https://www.youtube.com/watch?=-9ceBgWV8io")

print(avatar.storyline)
