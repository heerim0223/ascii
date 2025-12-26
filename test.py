import cv2
import ascii_magic
import imgkit
import os

os.makedirs("images", exist_ok=True)
os.makedirs("ascii", exist_ok=True)
os.makedirs("html", exist_ok=True)

vidObj = cv2.VideoCapture("sample.mp4")
count = 0
flag = 1

while flag:
    flag, image = vidObj.read()
    try:
        cv2.imwrite("images/frame%d.jpg" % count, image)
    except:
        break
    count += 1

for i in range(count):
    s = "images/frame"+str(i)+".jpg"

    art = ascii_magic.from_image(s)

    art.to_html_file(
        'html/frame'+str(i)+'.html',
        columns=250,
        width_ratio=2,
        additional_styles='background: #222;'
    )

path = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltoimage.exe'
config = imgkit.config(wkhtmltoimage=path)

for i in range(count):
    imgkit.from_file(
        'html/frame'+str(i)+'.html',
        'ascii/frame'+str(i)+'.jpg',
        config=config
        )

frame = cv2.imread('ascii/frame0.jpg')
ih, iw, il = frame.shape
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video = cv2.VideoWriter(
    'asciiVideo.mp4', # 제목
    fourcc, 
    24.00, # 프레임
    (iw, ih) # 크기
)

for i in range(count):
    image = 'ascii/frame'+str(i)+'.jpg'
    video.write(cv2.imread(image))

cv2.destroyAllWindows()
video.release()
 
# ffmpeg -i sample.mp4 -q:a 0 -map a audio.mp3
# ffmpeg -i asciiVideo.mp4 -i audio.mp3 -c:v copy -c:a aac -shortest output.mp4