import os

savFILE_NAME = "ICH.VENZ"


def save_file():
    if not os.path.isdir("./data"):
        os.mkdir("data")
        with open(f"./data/{savFILE_NAME}", "w") as f:
            f.write("0")

    else:
        if not os.path.isfile(f"./data/{savFILE_NAME}"):
            with open(f"./data/{savFILE_NAME}", "w") as f:
                f.write("0")

    with open(f"./data/{savFILE_NAME}", "r") as f:
        progress = f.read()
        print("welcome back player.")
        return progress


def write(number: int):
    if os.path.isfile(f"./data/{savFILE_NAME}"):
        with open(f"./data/{savFILE_NAME}", "w") as f:
            f.write(str(number))
            print(f"{number} saved")
