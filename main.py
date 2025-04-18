import moviepy.editor as mp

clip = mp.ColorClip(size=(640, 480), color=(255, 0, 0), duration=3)
clip = clip.set_fps(24)
clip.write_videofile("output.mp4")
