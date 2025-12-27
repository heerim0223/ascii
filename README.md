# ASCII
ASCII(**A**merican **S**tandard **C**ode for **I**nformation **I**nterchange)

<img width="30%" height="30%" alt="ASCII_Code" src="https://github.com/user-attachments/assets/ec67a9fc-0947-4d28-9ccd-d4bc625c206e" />

+ 1963년 미국 ANSI에서 표준화된 정보 교환용 7비트 부호 체계
+ 16진법을 사용한 128개의 부호 - 000(0x00) ~ 127(0x7F)


# ASCII Art
<img width="30%" height="30%" alt="ASCII_Art" src="https://github.com/user-attachments/assets/0656fbc0-31dc-4798-b90b-aa394b5370fa" />

+ 컴퓨터를 활용한 그래픽 디자인 기법
+ ASCII Code를 조합한 시각적인 그림
+ 가장 오래된 ASCII Art는 1966년경 벨 연구소의 <a alt="Oldest_ASCII_Art" href="https://asciiville.dev/posts/Ascii-Art-History/">케네스 놀턴의 ASCII Art</a>

# Generate ASCII Image & Video
<img width="30%" height="30%" alt="제목 없는 다이어그램 drawio" src="https://github.com/user-attachments/assets/d918e083-134b-4569-8558-9195fc875355" />

### 1. ASCII Code
```text
Image(Original) -> HTML(ASCII) -> Text
```

### 2. ASCII Image
<img width="790" height="778" alt="Image" src="https://github.com/user-attachments/assets/fae82ea7-b646-4769-a437-d4749be326bf" />

```text
Image(Original) -> HTML(ASCII) -> Image
```

### 3. ASCII Video
https://github.com/user-attachments/assets/de566761-3913-4668-9106-7eaa8e6875cb

```text
Video(Original) -> Image(1 sheet per frame) -> HTML(ASCII) -> Image -> Video
```

---

```bash
# Extract Audio to Original Video
ffmpeg -i sample.mp4 -q:a 0 -map a audio.mp3

# Merge Audio into ASCII Video
ffmpeg -i asciiVideo.mp4 -i audio.mp3 -c:v copy -c:a aac -shortest output.mp4
```
