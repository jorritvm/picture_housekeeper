import os
import subprocess
import shlex
import json
import sys
import settings as s
import datetime

def string_partial_match_to_list(s, l):
    match = False
    for element in l:
        if element in s:
            match = True
    return match

def get_file_size_mb(fp, digits = -1):
    mbsize = os.stat(fp).st_size / 1024 / 1024  
    if digits >= 0:
        mbsize = round(mbsize, digits)
    return mbsize

def get_folder_size_mb(path, digits = -1):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    mbsize = total_size / 1024 / 1024
    if digits >= 0:
        mbsize = round(mbsize, digits)
    return mbsize

def get_video_meta(fp_video, fp_ffprobe):
    """get a subset of metadata from a video file

    Args:
        fp_video (string): full filepath to video file
        fp_ffprobe (string): full filepath to ffprobe.exe file (part of the ffmpeg installation)

    Returns:
        [dict]: metadata
    """
    
    meta = dict()

    # get system info
    meta["filesize"] = get_file_size_mb(fp_video)
    
    # run the ffprobe process, decode stdout into utf-8 & convert to JSON
    cmd = f"\"{fp_ffprobe}\" -v quiet -print_format json -show_streams"
    args = shlex.split(cmd)
    args.append(fp_video)

    try:
        ffprobeOutput = subprocess.check_output(args).decode('utf-8')
        ffprobeOutput = json.loads(ffprobeOutput)

        # extract video stream info
        videokeys = ["height", "width", "duration", "avg_frame_rate", "codec_long_name", "codec_name", "codec_tag_string", "bit_rate"] # codec_type = "video"
        video_stream_index = -1
        for i in range(len(ffprobeOutput['streams'])):
            if ffprobeOutput['streams'][i]['codec_type'] == "video":
                video_stream_index = i  

        if video_stream_index >= 0:
            for metakey in videokeys:
                try:
                    meta["video_" + metakey] = ffprobeOutput['streams'][video_stream_index][metakey]
                except KeyError:
                    # pass because if some key wasnt found
                    pass
        else:
            sys.exit("File %s does not have a video stream." % fp_video)   

        # extract audio stream info
        audiokeys = ["channel_layout", "bit_rate", "channels", "codec_long_name", "codec_name", "codec_tag_string"] # codec_type = "audio"
        audio_stream_index = -1
        for i in range(len(ffprobeOutput['streams'])):
            if ffprobeOutput['streams'][i]['codec_type'] == "audio":
                audio_stream_index = i  

        if audio_stream_index >= 0:
            for metakey in audiokeys:
                try:
                    meta["audio_" + metakey] = ffprobeOutput['streams'][audio_stream_index][metakey]
                except KeyError:
                    # pass because for example mono audio streams don't have channel_layout
                    pass
        else:
            #sys.exit("File %s does not have a audio stream." % fp_video)
            pass

        return meta
    
    except:
        # file unreadable
        return None

def ts(t = datetime.datetime.now()):
    ts = t.strftime("%Y-%m-%d-%H-%M-%S")
    return ts

