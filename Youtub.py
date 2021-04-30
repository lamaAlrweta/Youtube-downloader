import streamlit as st
from pytube import YouTube
import os
from pathlib2 import Path

path_to_download_folder = str(os.path.join(Path.home(), "Downloads"))

st.title(" YouTube Downloader")
# Enter the URL
link = st.text_input("Enter the link here")
options = {
    "format": "bestvideo+bestaudio"
}
submit = st.button("download")


def download(link):
    if submit:
        # if link == YouTube:
            yt = YouTube(link)
            yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by(
                'resolution').desc().first().download(path_to_download_folder)
            st.success("successfully downloaded in Downloads Folder ")
        # else:
        #     st.error("Enter a valid YouTube link")


if __name__ == '__main__':
    download(link)

