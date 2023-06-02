import pytesseract

# Get the image path
image_path = "1234.jpg"

# Read the text from the image
text = pytesseract.image_to_string(image_path)

# Print the text
print(text)
