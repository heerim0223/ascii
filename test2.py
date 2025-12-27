import ascii_magic
import imgkit
import os

os.makedirs("images", exist_ok=True)
os.makedirs("ascii", exist_ok=True)
os.makedirs("html", exist_ok=True)

art = ascii_magic.from_image("sample.jpg")

art.to_html_file(
    "result.html",
    columns=250,
    additional_styles="""
        background:#222;
        margin: 0;
        padding: 0;
        white-space: pre;
        display: block;
        """
)

path = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltoimage.exe"
config = imgkit.config(wkhtmltoimage=path)
options = {
    "format": "jpg",
    "margin-top": "0",
    "margin-bottom": "0",
    "margin-left": "0",
    "margin-right": "0"
}

# imgkit.from_file("result.html", "result.jpg", config=config)
art.to_terminal()