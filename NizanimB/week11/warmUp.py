import arcade

window = arcade.Window(800, 600, "My first Arcade Screen")

arcade.draw_lbwh_rectangle_filled(400, 200, 32, 32, arcade.color.RED)
arcade.draw_circle_filled(400, 100, 20, arcade.color.GREEN)
arcade.draw_triangle_filled(375, 300, 400, 300, 387.5, 315, arcade.color.BLUE)

arcade.run()