import moviepy.editor as mp

video = mp.VideoFileClip(r"C:\Users\USUARIO\Desktop\channels\travelling channel\Austria\austria1.mp4")



logo = (mp.ImageClip(r"C:\Users\USUARIO\Desktop\logo.png")
    .set_start(3)  
    .set_end(10)  
    .set_pos(("right","top")))
    

logo = logo.crossfadein(2.0)
logo = logo.crossfadeout(2.0)

final = mp.CompositeVideoClip([video, logo])
final.write_videofile(r"C:\Users\USUARIO\Desktop\testes.mp4")

hey i am gay