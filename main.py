def on_on_overlap(projectile, enemy):
    projectile.destroy()
    enemy.destroy(effects.disintegrate, 1)
    info.change_score_by(100)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap)

# game loop and events

def on_a_pressed():
    global projectile2
    projectile2 = sprites.create_projectile_from_sprite(assets.image("""
            projectile
        """),
        player_plane,
        projectile_speed,
        0)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap2(player2, enemy2):
    game.over(False)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

enemy_plane: Sprite = None
running_animation = False
projectile2: Sprite = None
projectile_speed = 0
player_plane: Sprite = None
# sprites
player_plane = sprites.create(assets.image("""
    player plane
"""), SpriteKind.player)
controller.move_sprite(player_plane)
player_plane.set_stay_in_screen(True)
# setup
backgroud_one = sprites.create(assets.image("""
    myImage
"""), 0)
backgroud_one.set_position(80, 60)
backgroud_one.z = -10
# variables
enemy_speed = -75
projectile_speed = 150

def on_on_update():
    global running_animation
    if player_plane.vx > 10 or player_plane.vy > 10:
        running_animation = True
        animation.run_image_animation(player_plane,
            assets.animation("""
                plane
            """),
            200,
            False)
    else:
        running_animation = False
game.on_update(on_on_update)

def on_update_interval():
    global enemy_plane
    enemy_plane = sprites.create(assets.image("""
        enemy plane
    """), SpriteKind.enemy)
    enemy_plane.set_velocity(enemy_speed, 0)
    enemy_plane.set_position(160, randint(5, 155))
    enemy_plane.set_flag(SpriteFlag.AUTO_DESTROY, True)
game.on_update_interval(1000, on_update_interval)

def on_update_interval2():
    global enemy_plane
    for index in range(3):
        if info.score() == 100:
            enemy_plane = sprites.create(assets.image("""
                myImage0
            """), SpriteKind.enemy)
            enemy_plane.set_velocity(enemy_speed, 0)
            enemy_plane.set_position(160, randint(5, 155))
            enemy_plane.set_flag(SpriteFlag.AUTO_DESTROY, True)
game.on_update_interval(1000, on_update_interval2)

