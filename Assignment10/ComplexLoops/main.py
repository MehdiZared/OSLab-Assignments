import arcade
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500


arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "CopmlexLoops")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()

for i in range(15):
    for j in range(15):
        if j % 2 == 0:
            arcade.draw_rectangle_filled((j * 30) + 40 , (i * 30) +40 , 15, 15,arcade.color.BLUE, 45)
        elif j%2 == 1 :
            arcade.draw_rectangle_filled( (j * 30 )+40, (i * 30 )+40 , 15, 15,arcade.color.RED, 45)

arcade.finish_render()
arcade.run()