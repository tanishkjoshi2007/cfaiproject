from flask import Flask, render_template, request
from PIL import Image, ImageDraw, ImageFont

app = Flask(__name__)

# 🔹 Function to wrap text into multiple lines
def wrap_text(draw, text, font, max_width):
    words = text.split()
    lines = []
    current_line = ""

    for word in words:
        test_line = current_line + word + " "
        width = draw.textlength(test_line, font=font)

        if width <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word + " "

    lines.append(current_line)
    return lines


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        text = request.form["text"]

        # 🔹 Create image
        img = Image.new('RGB', (800, 1000), color=(255, 255, 255))
        draw = ImageDraw.Draw(img)

        # 🔹 Load font
        try:
            font = ImageFont.truetype("handwriting.ttf", 32)
        except:
            print("Font not found, using default")
            font = ImageFont.load_default()

        # 🔹 Wrap text
        max_width = 760
        lines = wrap_text(draw, text, font, max_width)

        # 🔹 Draw text line by line
        x, y = 20, 50
        line_height = 40

        for line in lines:
            draw.text((x, y), line, fill=(0, 0, 0), font=font)
            y += line_height

        # 🔹 Save image
        img.save("static/output.png")

        return render_template("index.html", image=True)

    return render_template("index.html", image=False)


if __name__ == "__main__":
    app.run(debug=True)