scene.setBackgroundColor(3)
let mySprite = sprites.create(img`
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
`, SpriteKind.Player)
game.onUpdateInterval(1000, function on_update_interval() {
    let projectile = sprites.createProjectileFromSprite(img`
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
    `, mySprite, randint(-25, 25), randint(-25, 25))
    projectile.lifespan = 10000
    if (projectile.vx < 0) {
        projectile.image.flipX()
    }
    
})
