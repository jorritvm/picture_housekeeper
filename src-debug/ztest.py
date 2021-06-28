

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


fpfn = "D:/pictures/2004/2004-08-03 Cine Twisted/Afbeelding 032.avi"
ffmpeg_path = "C:/Program Files/ffmpeg/bin/ffmpeg.exe"
convert_with_ffmpeg(fpfn, ffmpeg_path)
print("finished")
