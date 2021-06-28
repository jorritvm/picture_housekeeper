import os
import subprocess
import shlex
import json
import sys
import settings as s
import datetime


def stringlist_pmatch_string(l, s):
    """returns true if any string in the stringlist partially matches string s

    Args:
        l (list): list of strings to partially match with
        s (string): string to match

    Returns:
        boolean: True if a partial match was found
    """
    match = False
    for element in l:
        if element in s:
            match = True
    return match


def string_pmatch_stringlist(s, l):
    match = False
    for element in l:
        if s in element:
            match = True
    return match


def stringlist_pmatch_stringlist(list1, list2):
    match = False
    for element1 in list1:
        for element2 in list2:
            if element1 in element2:
                match = True
    return match


def get_file_size_mb(fp, digits=-1):
    """returns the file size in megabyte

    Args:
        fp (string): filepath to file
        digits (int, optional): round to digits. Defaults to -1.

    Returns:
        float: size of the file in MB
    """
    mbsize = os.stat(fp).st_size / 1024 / 1024
    if digits >= 0:
        mbsize = round(mbsize, digits)
    return mbsize


def get_folder_size_mb(path, digits=-1):
    """returns the folder size (recursive) in MB

    Args:
        path (string): path to the folder
        digits (int, optional): round to digits. Defaults to -1.

    Returns:
        float: size of the folder in MB
    """
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
        videokeys = ["height", "width", "duration", "avg_frame_rate", "codec_long_name",
                     "codec_name", "codec_tag_string", "bit_rate"]  # codec_type = "video"
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
        audiokeys = ["channel_layout", "bit_rate", "channels", "codec_long_name",
                     "codec_name", "codec_tag_string"]  # codec_type = "audio"
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


def ts(t=datetime.datetime.now()):
    ts = t.strftime("%Y-%m-%d-%H-%M-%S")
    return ts


def ask_filepath(initial_dir):
    from tkinter import Tk
    from tkinter.filedialog import askopenfilename
    Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    # show an "Open" dialog box and return the path to the selected file
    fpfn = askopenfilename(initialdir=initial_dir)
    return fpfn


def compress_folder_with_7z(fp, compression_switch, zip7_path):
    import subprocess
    import os

    command = [zip7_path,
               "a",
               "-t7z",
               compression_switch,
               os.path.join(os.path.dirname(fp), os.path.basename(fp) + ".7z"),
               fp]

    # print(subprocess.list2cmdline(command))
    subprocess.run(command)


def convert_with_ffmpeg(fpfn, ffmpeg_path):
    import subprocess
    import os

    command = [ffmpeg_path,
               "-y",
               "-i",
               fpfn,
               "-c:v",
               "libx264",
               "-preset",
               "slow",
               "-crf",
               "23",
               "-codec:a",
               "aac",
               "-b:a",
               "96k",
               "-ac",
               "2",
               "-strict",
               "-2",
               os.path.join(os.path.dirname(fpfn), os.path.splitext(os.path.basename(fpfn))[0] + ".mkv")]

    print(subprocess.list2cmdline(command))
    subprocess.run(command)
