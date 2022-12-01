import os


def remove_old_files():
    path_url = "app/static"
    for path in os.listdir(path_url):
        # check if current path is a file
        if os.path.isfile(os.path.join(path_url, path)):
            image_path = path_url + "/" + path
            os.remove(image_path)


def get_new_files():

    res = []

    # Iterate directory
    for path in os.listdir("app/static"):
        # check if current path is a file
        if os.path.isfile(os.path.join("app/static", path)):
            res.append(path)
    print(res)
    return res