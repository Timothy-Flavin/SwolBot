import pytube as pt 
from moviepy.editor import *

videosLeftToDowload='y'
while videosLeftToDowload=='y':
    print("Please past in a video link:")
    link=input()
    yt = pt.YouTube(link)
    print(yt.streams.filter(adaptive=True))
    print("enter tag you want to input ex: 137, or the letter 'y' if you simply want the highest resolution")
    itag = input()
    if(itag!='y' and itag!='Y'):
        yt.streams.get_by_itag(itag).download('./YoutubeData')
    else:
        yt.streams.get_highest_resolution().download('./YoutubeData')

    pickingClips='y'
    print("You will now choose subclips by entering a start and end time\nin seconds ex: 55,65 will record from 55 to 65 seconds.")
    while pickingClips == 'y':
        print("Start Time s: ",end='')
        startTime=input()
        print("End   Time s: ",end='')
        endTime=input()
        video = VideoFileClip("./YoutubeData/YouTube.mp4").subclip(startTime,endTime)
        print("save video clip as ex (good_pushup_1): ", end='')
        fileName=input()
        video.write_videofile("./YoutubeData/"+fileName+".mp4",fps=30)
        print("would you like to pick another clip from this video? 'y' or 'n': ", end='')
        pickingClips = input()
    print("would you like to pick another clip? 'y' or 'n': ", end='')
    videosLeftToDowload=input()