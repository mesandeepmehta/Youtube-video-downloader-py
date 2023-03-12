from pytube import YouTube

while True:

    link = input("Enter link of the YouTube video: ")

    vd = YouTube(link)

    print("Title: ", vd.title)
    print("Length: ", vd.length, "seconds")
    print("Views: ", vd.views)
    print("Cahnnel Name: ", vd.author)

    try:
        option = input("Enter 1 to download video and 2 to download audio only. Press 0 to cancel: ")
    except ValueError:
        print("Enter 1 or 2 only")
        continue

    if option == str(1):
        vid = vd.streams.get_highest_resolution()
        vid.download(r'C:\Users\Sandeep Mehta\Downloads\YTdownloads')
        print("     \n"
              "Success!\n"
              "    ")
    elif option == str(2):
        vid = vd.streams.get_audio_only()
        vid.download(r'C:\Users\Sandeep Mehta\Downloads\YTdownloads')
        print("     \n"
              "Success!\n"
              "    ")
    elif option == str(0):
        print("     \n"
              "Thank You for using My project !")
        break
    else:
        print("Enter 1 or 2 only")

