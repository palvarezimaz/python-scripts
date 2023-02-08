from pytube import YouTube

def download(link):
  youtubeObject = YouTube(link)
  youtubeObject = youtubeObject.streams.get_highest_resolution()
  try:
    youtubeObject.download()
  except:
    print("An error has occured")
  print("Download is successful")

link = input("Enter the YouTube video URL: ")
download(link)