import os

DATA_PATH = os.path.join(os.getcwd(), "data", "LOW_QUALITY_WITH_OG")

cattle_classes = os.listdir(DATA_PATH)

total_images = 0
print("\n")
for cattle_class in cattle_classes:
    imag_path = os.path.join(DATA_PATH, cattle_class)
    images_num = len(os.listdir(imag_path))

    total_images += images_num
    if images_num != 52:
        print(f"{cattle_class}: {images_num}")

print("\n")
print(f"Total images: {total_images}\n\n")
print(f"Images num: {images_num}")

print(f"Total: {len(cattle_classes) * images_num}")