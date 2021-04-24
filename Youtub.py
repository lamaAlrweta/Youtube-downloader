import streamlit as st
import youtube_dl
from pytube import YouTube


st.title(" YouTube Downloader")
#Enter the URL
link = st.text_input("Enter the link here")
options = {
			"format": "bestvideo+bestaudio"
	    }
submit = st.button("download")
def download(link):
	yt = YouTube(link)
	try:
		if submit:
			# with youtube_dl.YoutubeDL(options) as ydl:
			# 	ydl.download([link])
			out_file=yt.stream.filter(progressive=True,file_extension='mp4').order_by('resolution').desc().first().download('sample')
			st.success("successfully downloaded")

	except YouTube.utils.DownloadError:
		raise st.error('this URL is invalid')
if __name__ == '__main__':
	download(link)
