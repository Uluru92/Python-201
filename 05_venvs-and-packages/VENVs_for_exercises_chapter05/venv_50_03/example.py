from PIL import Image
import pixelgreat as pg

# Open the image
selfie = Image.open("mirror_Jor.jpg")

# Call a single-use command to convert the image (slow)
image_out = pg.pixelgreat(
    image=selfie,
    pixel_size=20,
    output_scale=4
)

# Save the image
image_out.save("mirror_Jor_pixelated.png")

# Close the images
selfie.close()
image_out.close()