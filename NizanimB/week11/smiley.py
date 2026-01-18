import arcade

# קבועים
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "My First Arcade Screen"
TILE_SIZE = 200

def smiley():

    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.start_render()

    # Write your code here

    arcade.finish_render()
    arcade.run()


if __name__ == "__main__":
    smiley()