from pytube import Playlist
import os
import sys

# DOWNLOAD CLASS TO DOWNLOAD PLAYLIST
class StartPlaylistDownLoad:

    def __init__(self, playlist):
        self.videoUrlsLength = len(str(len(playlist.video_urls)))
        self.playlist = playlist

    # DOWNLOAD FUNCTION TO DOWNLOAD PLAYLIST
    def runPlaylist(self):
        i = 1

        for video in self.playlist.videos:
            print('Downloading : {} with url: {}'.format(video.title,video.watch_url))
            self.videoStreams = video.streams
            self.download()
            self.renameFile(i)
            i = i + 1

    def download(self):
        streamsFilter = self.videoStreams.filter(type='video', progressive=True, file_extension='mp4')
        filterOrderBy = streamsFilter.order_by('resolution')
        orderByDesc = filterOrderBy.desc()
        orderByDesc.first().download()

    def renameFile(self, index):
        rename = os.path.splitext(self.videoStreams.first().default_filename)
        strIndex = self.getIndexValue(index)
        os.rename(str(rename[0]) + '.mp4' , strIndex + '.' + rename[0] + '.mp4')

    def getIndexValue(self, index):
        strIndex = str(index)
        value = self.videoUrlsLength - len(strIndex)
        addZeroes = ''

        for i in range(0, value):
            addZeroes = addZeroes + '0'

        return addZeroes + strIndex



# ADD YOUR LINK HERE
vidLink = 'https://www.youtube.com/playlist?list=PLvRfcAN-QbYncGDzMiG34xTdCdbIXEq2a'

# Enter playlist-url in place of url
playlist = Playlist(vidLink)  

# CALLING DOWNLOAD FUNCTION
startPlaylistDownLoad = StartPlaylistDownLoad(playlist)
startPlaylistDownLoad.runPlaylist()
