import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "My First Arcade Screen"
TILE_SIZE = 40

def smiley():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.start_render()

    col = 5
    row = 3
    face_x = (col * TILE_SIZE) + (TILE_SIZE / 2)
    face_y = (row * TILE_SIZE) + (TILE_SIZE / 2)
    arcade.draw_circle_filled(face_x, face_y, 50, arcade.color.YELLOW)

    col = 4.3
    row = 3.3
    target_x = (col * TILE_SIZE) + (TILE_SIZE / 2)
    target_y = (row * TILE_SIZE) + (TILE_SIZE / 2)

    arcade.draw_circle_filled(target_x, target_y, 10, arcade.color.BLACK)

    col = 5.7
    row = 3.3
    target_x = (col * TILE_SIZE) + (TILE_SIZE / 2)
    target_y = (row * TILE_SIZE) + (TILE_SIZE / 2)

    arcade.draw_circle_filled(target_x, target_y, 10, arcade.color.BLACK)

    arcade.draw_arc_outline(face_x, face_y - 10,50,30, arcade.color.BLACK,200,340)
    arcade.finish_render()
    arcade.run()

if __name__ == "__main__":
    smiley()
