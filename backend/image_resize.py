from PIL import Image

image = Image.open('backend/Madison.png')
image.thumbnail((612, 410))
image.save('frontend/static/styles/images/Madison.png')