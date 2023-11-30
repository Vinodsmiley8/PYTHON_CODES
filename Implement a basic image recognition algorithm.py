# Using a simple pixel intensity threshold
def basic_image_recognition(image):
    threshold = 128
    for row in image:
        for pixel in row:
            if pixel > threshold:
                print("Object detected")
                return
    print("No object detected")

# Usage
image_data = [[150, 200, 50], [100, 30, 180], [80, 120, 200]]
basic_image_recognition(image_data)