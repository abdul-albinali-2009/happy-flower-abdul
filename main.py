scene.set_background_color(3)
mySprite = sprites.create(img("""
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . 5 . . . . . .
    . . . . . 5 . . . 5 . . . . . .
    . . . . . 5 5 5 5 5 5 . . . . .
    . . . . . . 5 5 e e 5 5 . . . .
    . . . . . . 5 e e e e 5 5 5 . .
    . . . 5 5 5 5 e e e e 5 5 . . .
    . . . . . . 5 e e e e 5 . . . .
    . . . . . . 5 5 5 5 5 5 5 . . .
    . . . . . . 5 . . 5 . . 5 5 . .
    . . . . . . 5 . . 5 . . . . . .
    . . . . . 5 . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
"""),
    SpriteKind.player)
def on_update_interval():
    
    projectile = sprites.create_projectile_from_sprite(img("""
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . 9 9 9 . . . . . . .
        . . f . . . 9 9 9 . . . . . . .
        . . f 5 f 5 5 f 5 5 f 5 . . . .
        . . . 5 f 5 5 f 5 5 f 5 . . . .
        . . . 5 f 5 5 f 5 5 f 5 . . . .
        . . . 5 f 5 5 f 5 5 f 5 . . . .
        . . . . . 5 5 f 5 5 . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
    """),
        mySprite,
        randint(-25,25),
        randint(-25,25))
    projectile.lifespan = 10000
    if projectile.vx < 0:
        projectile.image.flip_x()
game.on_update_interval(1000, on_update_interval)