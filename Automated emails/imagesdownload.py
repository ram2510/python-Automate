from google_images_download import google_images_download # we will use this package to download images
response = google_images_download.googleimagesdownload() # class initialsiation
arguments = {"keywords":"motivational quotes","format":"png"}
paths = response.download(arguments)
print(paths)
