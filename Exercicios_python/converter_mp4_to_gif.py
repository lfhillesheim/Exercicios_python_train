
# import the necessary module
import moviepy as mv
# load the video
clip = mv.VideoFileClip("my_video.mp4")

#.subclip('2:09:05', '2:09:17')

# getting only 3 first seconds from video
video = mv.CompositeVideoClip([clip])
# save the video clip as gif
video.write_gif("mygif.gif",  program='ffmpeg', fps=15)