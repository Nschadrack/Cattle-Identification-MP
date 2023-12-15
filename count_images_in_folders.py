import os

PATHS = ["D:\CMU\Fall 23\Capstone\project\Cattle-Identification-MP\data\LOW_QUALITY_WITH_NO_OG",
         "D:\CMU\Fall 23\Capstone\project\Cattle-Identification-MP\data\LOW_QUALITY_WITH_OG"]


with open("Statistics.txt", "w+") as f:
    for path in PATHS:
        images_classes = sorted(os.listdir(path))
        dir_name = path.split("\\")[-1]
        print("\n\n")
        f.write(f'\nSTATISTICS FOR {dir_name}\n===================================\n')
        print(f'\nSTATISTICS FOR {dir_name}\n===================================\n')
        for image_class in images_classes:
            line = f"{image_class}: {len(os.listdir(os.path.join(path, image_class)))} Images\n"
            f.write(line)
            print(line)
