from PIL import Image
import os

base_folder = ""
while base_folder == "":
    base_folder = str(input("Please specify the folder path that contain file(s) to convert (ex : C:/test/folder): "))
    if os.path.exists(base_folder) == False:
        print("This path doesn't exist.")
        base_folder = ""
    elif len(os.listdir(base_folder)) == 0:
        print("There's anything to convert here.")
        base_folder = ""

full_path = os.path.abspath(base_folder)
output_path = f"{os.path.split(full_path)[0]}/PDF_Output/"

if os.path.exists(output_path) == False:
    os.makedirs(output_path)

def existingFolderChecker(path):
    if os.path.exists(path) == False:
        os.makedirs(path)

for file_or_folder_name in os.listdir(base_folder):
    try:
        temp_path = f"{base_folder}/{file_or_folder_name}"
        if os.path.isfile(temp_path):
            image = Image.open(rf'{temp_path}')
            converted_img = image.convert('RGB')
            filename = file_or_folder_name.split(".")[0]
            output_temp_path = f'{output_path}/{filename}'
            existingFolderChecker(output_temp_path)
            converted_img.save(rf'{output_temp_path}/{filename}.pdf')
        elif os.path.isdir(temp_path):
            opened_img_list = []
            for file in os.listdir(temp_path):
                opened_img = Image.open(rf'{temp_path}/{file}')
                converted_img = opened_img.convert('RGB')
                opened_img_list.append(converted_img)
            output_temp_path = f'{output_path}/{file_or_folder_name}'
            existingFolderChecker(output_temp_path)
            opened_img_list[0].save(rf'{output_temp_path}/{file_or_folder_name}.pdf', save_all=True, append_images=opened_img_list[1:])
    except Exception as e:
        print(f"Error : {e}")