from PIL import Image, ImageDraw, ImageFont, ImageFilter
import textwrap


def blank_poster(mode: str, size: tuple, color: str):
    # create a blank image
    poster = Image.new(mode=mode, size=size, color=color)
    return poster


# get a drawing context
# draw = ImageDraw.Draw(poster)

# def add_text(draw_object, text, font, position):
#     text_bbox = draw_object.textbbox((0, 0), text, font=font)

# # set up font and text, see  ~/Library/Fonts/ to see alternatives
# font = ImageFont.truetype("PlayfairDisplay-Regular.otf", 48)
# text = "Sierpínski Triangle"
#
# # calculate text size and position
# text_bbox = draw.textbbox((0, 0), text, font=font)
# x = (poster.width - text_bbox[2]) // 2
# y = 0  # (poster.height - text_bbox[3]) // 2
#
# # draw text
# draw.text((x, y), text, fill='black', font=font)




def include_figure(poster, figure, pos: tuple):
    # paste onto poster
    poster.paste(figure, pos)


if __name__ == '__main__':
    # get blank poster
    dpi = 300
    poster_width_px = int(80 * dpi / 2.54)  # Convert 80cm to pixels
    poster_height_px = int(120 * dpi / 2.54)  # Convert 120cm to pixels

    # width = 9450
    # height = 14172
    poster = blank_poster('RGB', size=(poster_width_px, poster_height_px), color='white')

    # load image file and set size
    figure = Image.open('triangle2.png')
    # Assuming the figure should take up most of the width but leave room for text and signature
    figure_width = int(poster_width_px * 0.9)  # 90% of the poster width
    figure_height = int(figure_width * figure.height / figure.width)  # Maintain aspect ratio

    # Resize figure image
    figure_image_resized = figure.resize((figure_width, figure_height), Image.ANTIALIAS)

    # Calculate figure position to be central
    figure_x = (poster_width_px - figure_width) // 2
    figure_y = (poster_height_px - figure_height) // 2 - 100  # Shift up slightly to leave space for text and signature

    # Paste the figure
    poster.paste(figure_image_resized, (figure_x, figure_y))

    # Add description text below the figure
    draw = ImageDraw.Draw(poster)
    # set up font and texts, see  ~/Library/Fonts/ to see alternatives
    title_font = ImageFont.truetype("PlayfairDisplay-BlackItalic.otf", 96*2)
    signature1_font = ImageFont.truetype("PlayfairDisplay-Regular.otf", 48*2)
    signature2_font = ImageFont.truetype("PlayfairDisplay-Italic.otf", 48*2)
    title = "Algorithm"
    signature1 = 'Mathematical Art'
    signature2 = 'Sierpínsky Triangle'

    # Title
    #title_width, title_height = draw.textsize(title, font=title_font)
    title_bbox = draw.textbbox((0, 0), title, font=title_font)
    title_x = (poster_width_px - title_bbox[2]) // 2
    title_y = figure_y + figure_height + 50  # Above the figure
    draw.text((title_x, title_y), title, fill="black", font=title_font)

    # Signature
    #signature1_width, signature1_height = draw.textsize(signature1, font=signature1_font)
    signature1_bbox = draw.textbbox((0,0), signature1, font=signature1_font)
    signature1_x = poster_width_px - signature1_bbox[2] - 100  # Right corner, with margin
    signature1_y = poster_height_px - signature1_bbox[3] - 50  # Bottom corner, with margin
    draw.text((signature1_x, signature1_y), signature1, fill="black", font=signature1_font)

    signature2_bbox = draw.textbbox((0, 0), signature2, font=signature2_font)
    signature2_x = poster_width_px - signature2_bbox[2] - 100  # Right corner, with margin
    signature2_y = poster_height_px - signature1_bbox[3] - signature2_bbox[3] - 50  # Below signature1
    draw.text((signature2_x, signature2_y), signature2, fill="black", font=signature2_font)

    # Save the poster
    poster.save('your_custom_poster2.jpg')

    # drawing context

    #include_figure(poster, figure, pos=(poster.width // 2, poster.height // 2))


    # calculate text size and position
    #title_bbox = draw.textbbox((0, 0), title, font=title_font)
    #x_title = (poster.width - title_bbox[2]) // 2
    #y_title = 100  # (poster.height - text_bbox[3]) // 2
    #draw.text((x_title, y_title), title, fill='black', font=title_font)

    # Paste the ornament onto the poster
    #poster.paste(ornament_blurred, (x, y), mask=ornament_blurred) # NOT WORKING

    # Save or display the modified poster
    #poster.show()
    #poster.save('poster_test.png')

