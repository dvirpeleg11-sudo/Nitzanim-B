import arcade
import arcade.color

window = arcade.Window(800, 600, "dvir")

arcade.draw_circle_filled(100, 150, 20, arcade.color.RED)
arcade.draw_ellipse_filled(150, 150, 20, 20, arcade.color.BLUE)
arcade.draw_text("dvir", 125, 200)

arcade.run()