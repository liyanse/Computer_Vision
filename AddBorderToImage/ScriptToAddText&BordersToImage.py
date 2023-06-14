#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from PIL import Image, ImageDraw, ImageFont

base_dir = os.path.realpath(os.path.dirname(__file__))

if __name__ == '__main__':
    lat = 39.7420
    lon = -104.9915
    width = 2040
    height = 3000
    city = "Vail"
    state = "Colorado"

    print(f'{lat} {lon}')
    print(f'{width} {height}')
    print(f'{city} {state}')

    static_image_file = os.path.join(base_dir, f'{state}_{city}_{width}_{height}.jpeg')
    static_image_file_upd = os.path.join(base_dir, f'{state}_{city}_{width}_{height}_upd.jpeg')

    # Open the original image
    static_image = Image.open(static_image_file)

    # Define the font and font size for the text
    font_city = ImageFont.truetype("arial.ttf", 80)
    font_state = ImageFont.truetype("arial.ttf", 70)
    font_location = ImageFont.truetype("arial.ttf", 30)

    # Define the text to be added
    coord_letter_lat = ''
    if lat > 0:
        coord_letter_lat = 'N'
    else:
        coord_letter_lat = 'S'

    if lon > 0:
        coord_letter_lon = 'E'
    else:
        coord_letter_lon = 'W'

    location_text = f'{lat}°{coord_letter_lat} {lon}°{coord_letter_lon}'

    # Define the border width color
    outer_border_width = 15
    inner_border_width = 2
    border_color = (0, 0, 0)

    # Define the width and height of the new image
    new_width, new_height = static_image.size

    # Create a new image with a white background
    new_image = Image.new("RGB", (new_width + outer_border_width*2, new_height + outer_border_width*2), (255, 255, 255))

    # Add the original image to the new image
    new_image.paste(static_image, (outer_border_width, outer_border_width))

    # Add the borders to the new image
    draw = ImageDraw.Draw(new_image)
    draw.line((outer_border_width - inner_border_width, outer_border_width - inner_border_width, new_width + outer_border_width + inner_border_width, outer_border_width - inner_border_width), fill=border_color, width=inner_border_width)
    draw.line((outer_border_width - inner_border_width, outer_border_width - inner_border_width, outer_border_width - inner_border_width, new_height + outer_border_width + inner_border_width), fill=border_color, width=inner_border_width)
    draw.line((new_width + outer_border_width + inner_border_width, outer_border_width - inner_border_width, new_width + outer_border_width + inner_border_width, new_height + outer_border_width + inner_border_width), fill=border_color, width=inner_border_width)
    draw.line((outer_border_width - inner_border_width, new_height + outer_border_width + inner_border_width, new_width + outer_border_width + inner_border_width, new_height + outer_border_width + inner_border_width), fill=border_color, width=inner_border_width)
    draw.line((outer_border_width, outer_border_width + 2*inner_border_width, new_width + outer_border_width, outer_border_width + 2*inner_border_width), fill=border_color, width=outer_border_width)
    draw.line((outer_border_width, outer_border_width + 2*inner_border_width, outer_border_width, new_height + outer_border_width), fill=border_color, width=outer_border_width)
    draw.line((new_width + outer_border_width, outer_border_width + 2*inner_border_width, new_width + outer_border_width, new_height + outer_border_width), fill=border_color, width=outer_border_width)
    draw.line((outer_border_width, new_height + outer_border_width, new_width + outer_border_width, new_height + outer_border_width), fill=border_color, width=outer_border_width)

    # Add the white background to the corners of the image
    draw.rectangle((0, 0, outer_border_width, outer_border_width), fill=(255, 255, 255))
    draw.rectangle((new_width + outer_border_width, 0, new_width + 2*outer_border_width, outer_border_width), fill=(255, 255, 255))
    draw.rectangle((0, new_height + outer_border_width, outer_border_width, new_height + 2*outer_border_width), fill=(255, 255, 255))
    draw.rectangle((new_width + outer_border_width, new_height + outer_border_width, new_width + 2*outer_border_width, new_height + 2*outer_border_width), fill=(255, 255, 255))

    # Add the text to the new image
    draw.text((new_width / 2 + outer_border_width, new_height - 300 + outer_border_width), city.upper(), font=font_city, fill=(0, 0, 0), anchor="mm")
    draw.text((new_width / 2 + outer_border_width, new_height - 225 + outer_border_width), f'---- {state.upper()} ----', font=font_state, fill=(0, 0, 0), anchor="mm")
    draw.text((new_width / 2 + outer_border_width, new_height - 150 + outer_border_width), location_text, font=font_location, fill=(0, 0, 0), anchor="mm")

    # Save the new image
    new_image.save(static_image_file_upd)
