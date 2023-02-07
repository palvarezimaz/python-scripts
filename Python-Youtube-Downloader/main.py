from pytube import YouTube

def Download(link):
  youtubeObject = YouTube(link)
  youtubeObject = youtubeObject.streams.get_highest_resolution()
  try:
    youtubeObject.download()
  except:
    print("An error has occured")
  print("Download is successful")

link = input("Enter the YouTube video URL: ")
Download(link)