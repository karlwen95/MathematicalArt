from PIL import Image, ImageDraw, ImageFont

# create a blank image
poster = Image.new('RGB', (600, 900), color='white')

# get a drawing context
draw = ImageDraw.Draw(poster)

# set up font and text, see  ~/Library/Fonts/ to see alternatives
font = ImageFont.truetype("PlayfairDisplay-Regular.otf", 48)
text = "Sierpínski Triangle"

# calculate text size and position
text_bbox = draw.textbbox((0, 0), text, font=font)
x = (poster.width - text_bbox[2]) // 2
y = 0  # (poster.height - text_bbox[3]) // 2

# draw text
draw.text((x, y), text, fill='black', font=font)

# load image file and paste onto poster
figure = Image.open('triangle.png')
poster.paste(figure, (0, 100))

# save poster
#poster.save('python_poster.png')

# save poster
poster.save('python_poster.png')
