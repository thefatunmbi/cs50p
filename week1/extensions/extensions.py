def main():
    fileName = input("File name: ")
    f_fileName = fileName.strip().lower()

    if f_fileName.endswith(".gif"):
        print("image/gif")
    elif f_fileName.endswith(".jpg"):
        print("image/jpeg")
    elif f_fileName.endswith(".jpeg"):
        print("image/jpeg")
    elif f_fileName.endswith(".png"):
        print("image/png")
    elif f_fileName.endswith(".pdf"):
        print("application/pdf")
    elif f_fileName.endswith(".txt"):
        print("text/plain")
    elif f_fileName.endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")


main()






