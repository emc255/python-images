from PIL import Image


def cropping_image():
    mac = Image.open("resources/images/example.jpg")
    mac.show()
    print(mac.format)
    print(mac.format_description)
    halfway = round(1993 / 2)
    x = halfway - 110
    y = 840
    width = halfway + 150
    height = 1257
    computer = mac.crop((x, y, width, height))
    computer.show()
    mac.paste(im=computer, box=(0, 0))
    mac.show()


def cropping_image_v2():
    pencils = Image.open("resources/images/pencils.jpg")
    print(pencils.size)
    print("TOP PENCILS")
    x = 0
    y = 0
    width = round(1950 / 3)
    height = round(1300 / 10)
    pencils.crop((x, y, width, height)).show()

    print("BOTTOM PENCILS")
    x = 0
    y = 1100
    width = round(1950 / 3)
    height = 1300
    pencils.crop((x, y, width, height)).show()

    pencils.show()


def color_transparency():
    red = Image.open("resources/images/red_color.jpg")
    blue = Image.open("resources/images/blue_color.png")
    print(blue.mode)  # should print "RGBA" or "LA"

    # If the mode is not "RGBA" or "LA", you can convert the image to a compatible mode like this:
    blue = blue.convert("RGBA")
    red = red.convert("RGBA")
    blue.putalpha(128)
    red.putalpha(128)
    blue.paste(im=red, box=(0, 0), mask=red)
    # result of combining the 2 pictures and masking
    blue.show()
    blue.save("resources/images/purple.png")

    purple = Image.open("resources/images/purple.png")
    purple.show()


def practice():
    word_matrix = Image.open("resources/images/word_matrix.png")
    mask = Image.open("resources/images/mask.png").resize(word_matrix.size)
    mask.putalpha(128)
    word_matrix.paste(im=mask, box=(0, 0), mask=mask)
    word_matrix.show()


def divider(title: str):
    print(f"=========={title.upper()}==========")


if __name__ == '__main__':
    # divider("cropping image")
    # cropping_image()

    # divider("cropping image v2")
    # cropping_image_v2()

    # divider("color transparency")
    # color_transparency()

    divider("practice")
    practice()
