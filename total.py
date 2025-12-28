# -*- coding: utf-8 -*-

import cv2
import ascii_magic
import imgkit
import os


class AsciiConverter:
    def __init__(self):
        os.makedirs("images", exist_ok=True)
        os.makedirs("ascii", exist_ok=True)
        os.makedirs("html", exist_ok=True)
        os.makedirs("result", exist_ok=True)

        self.wkhtml_path = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltoimage.exe"
        self.config = imgkit.config(wkhtmltoimage=self.wkhtml_path)

    def img_to_ascii_html(self, src, res):
        art = ascii_magic.from_image(f"{src}.jpg")

        html_path = f"result/{res}.html"
        jpg_path = f"result/{res}.jpg"

        art.to_html_file(
            html_path,
            columns=250,
            additional_styles="""
                background:#222;
                margin: 0;
                padding: 0;
                white-space: pre;
                display: block;
            """
        )
        imgkit.from_file(html_path, jpg_path, config=self.config)
        art.to_terminal()

    def video_to_ascii_video(self, video_path, res, fps=24.0):
        vid = cv2.VideoCapture(f"{video_path}.mp4")
        count = 0
        flag = True

        # 프레임 추출
        while flag:
            flag, image = vid.read()
            if not flag:
                break
            cv2.imwrite(f"images/frame{count}.jpg", image)
            count += 1

        # 각 프레임을 html로 변환
        for i in range(count):
            s = f"images/frame{i}.jpg"
            art = ascii_magic.from_image(s)
            art.to_html_file(
                f"html/frame{i}.html",
                columns=250,
                width_ratio=2,
                additional_styles="background:#222;"
            )

        # html을 jpg로 변환
        for i in range(count):
            imgkit.from_file(
                f"html/frame{i}.html",
                f"ascii/frame{i}.jpg",
                config=self.config
            )

        # 아스키 이미지 영상으로 병합
        frame0 = cv2.imread("ascii/frame0.jpg")
        ih, iw, _ = frame0.shape
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')

        video = cv2.VideoWriter(
            f"result/{res}.mp4",
            fourcc,
            fps,
            (iw, ih),
        )

        for i in range(count):
            frame = cv2.imread(f"ascii/frame{i}.jpg")
            video.write(frame)

        video.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    print("""
____________________________
|    [ASCII Convertor]     |
|--------------------------|
|                          |
| (1) Image -> ASCII Image |
| (2) Video -> ASCII Video |
|                          |
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
Plz select               
the conversion method    
as a number.
""")
    
    ins = input("""Conversion Method Number: """)

    conv = AsciiConverter()

    if ins == "1":
        print("""
____________________________
|     [ASCII Convertor]     |
|---------------------------|
| (1) Image --> ASCII-Image |
|                           |
| Source Image Name: [    ] |
| Result Image Name: [    ] |
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
Insert
Source·Result Image Name""")
        
        src = input("""Source(jpg): """)
        res = input("""Result(jpg): """)

        # 이미지 -> ASCII html
        conv.img_to_ascii_html(src, res) 
    
    elif ins == "2":
        print("""
____________________________
|     [ASCII Convertor]     |
|---------------------------|
| (2) Video --> ASCII-Video |
|                           |
| Source Video Name: [    ] |
| Result Video Name: [    ] |
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
Insert
Source·Result Video Name""")
        
        src = input("""Source(mp4): """)
        res = input("""Result(mp4): """)

        # 영상 -> ASCII 영상
        conv.video_to_ascii_video(src, res)

        # 참고
        # 원본 영상에서 오디오 추출
        # ffmpeg -i sample.mp4 -q:a 0 -map a audio.mp3
        # 아스키 영상 + 원본 영상 오디오 병합
        # ffmpeg -i asciiVideo.mp4 -i audio.mp3 -c:v copy -c:a aac -shortest output.mp4