from PIL import Image

CYAN = '\033[36m'
RESET = '\033[0m'

def create_karakter_animek(image_path, output_width=100, chars="@%#*+=-:. "):
    img = Image.open(image_path).convert('L')
  
    aspect_ratio = img.height / img.width
    output_height = int(aspect_ratio * output_width * 0.55)
    
    img = img.resize((output_width, output_height))
    
    pixels = img.getdata()
    ascii_str = ''
    for i, pixel in enumerate(pixels):
        char = chars[int(pixel / 255 * (len(chars) - 1))]
        ascii_str += f"{CYAN}{char}{RESET}"
        if (i + 1) % output_width == 0:
            ascii_str += '\n'
    
    return ascii_str

image_path = input("Enter the path to your image: ")
output_width = int(input("Enter the desired width (default 100): ") or "100")

karakter_animek = create_karakter_animek(image_path, output_width)

print(karakter_animek)

with open("output.txt", "w") as f:
    f.write(karakter_animek)

print("Output berhasil)")
