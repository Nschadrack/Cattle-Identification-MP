import os
import shutil


def merge_datasets(merge_dest, include_og=False):
    ROOT_DATA_PATH = os.path.join(os.path.dirname(os.getcwd()), "data")
    DATA_ROOT_CONTENT = os.listdir(ROOT_DATA_PATH)
    DESTINATION_PATH = os.path.join(ROOT_DATA_PATH, merge_dest)

    os.makedirs(DESTINATION_PATH, exist_ok=True)

    for temp in DATA_ROOT_CONTENT:  # each sub folders in the data root path

        if not include_og and temp.lower() == "og":  # skip OG folder
            continue
        if temp.lower().startswith('low_quality'):  # ignore created final destination folders
            continue

        temp_content = sorted(os.listdir(os.path.join(ROOT_DATA_PATH, temp)))  # list images folders
        for content in temp_content:  # each image folder
            content_images = os.listdir(os.path.join(ROOT_DATA_PATH, temp, content))

            os.makedirs(os.path.join(DESTINATION_PATH, content), exist_ok=True)
            count_images = 0
            for image_name in content_images:  # each image
                count_images += 1
                source_path = os.path.join(ROOT_DATA_PATH, temp, content, image_name)
                destination = os.path.join(DESTINATION_PATH, content, image_name)
                shutil.copy2(source_path, destination)

                print(f"COPY: {os.path.dirname(source_path)}  TO  {os.path.dirname(destination)}")
                if include_og and temp.lower() == "og" and count_images == 4:
                    break


if __name__ == "__main__":
    merge_datasets("LOW_QUALITY_WITH_NO_OG")
    merge_datasets("LOW_QUALITY_WITH_OG", include_og=True)
