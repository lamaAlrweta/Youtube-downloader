import streamlit as st
from pytube import YouTube
import os

def get_download_path():
    """Returns the default downloads path for linux or windows"""
    if os.name == 'nt':
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:
        return os.path.join(os.path.expanduser('~'), 'downloads')

st.title(" YouTube Downloader")
# Enter the URL
link = st.text_input("Enter the link here")
options = {
    "format": "bestvideo+bestaudio"
}
submit = st.button("download")


def download(link):

    if submit:
        yt = YouTube(link)
        yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by(
            'resolution').desc().first().download(
            get_download_path())
        st.success("successfully downloaded in 'Downloads Folder' ")


if __name__ == '__main__':
    download(link)
