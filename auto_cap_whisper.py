import datetime
import whisper
import torch
import moviepy.editor as mp
import os
from datetime import timedelta

device = torch.device('cuda')

def video_to_audio(video_path, audio_path):
    video = mp.VideoFileClip(video_path)
    video.audio.write_audiofile(audio_path)

def transcribe_audio(audio_path, language="Cantonese"):
    model = whisper.load_model("large",device=device)  # 你可以選擇 "tiny", "base", "small", "medium", 或 "large"
    result = model.transcribe(audio_path, language=language)
    return result

def create_srt_file(result, output_path):
    with open(output_path, "w", encoding="utf-8") as file:
        for i, segment in enumerate(result["segments"], start=1):
            start_time = format_time(segment["start"])
            end_time = format_time(segment["end"])
            text = segment["text"].strip()
            
            file.write(f"{i}\n")
            file.write(f"{start_time} --> {end_time}\n")
            file.write(f"{text}\n\n")

def format_time(seconds):
    td = timedelta(seconds=seconds)
    hours, remainder = divmod(td.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    milliseconds = td.microseconds // 1000
    return f"{hours:02d}:{minutes:02d}:{seconds:02d},{milliseconds:03d}"

# 主程序
video_path = r"D:\Youtube\Movie\612\bullshit_jobs(1).mp4"
audio_path = r"temp_audio.wav"
srt_path = video_path.replace(".mp4", ".srt")

print("Start Time : {}".format(datetime.datetime.now().isoformat()))
video_to_audio(video_path, audio_path)
result = transcribe_audio(audio_path)
create_srt_file(result, srt_path)

#清理臨時音頻文件
os.remove(audio_path)

print("Finish Time : {}".format(datetime.datetime.now().isoformat()))
print(f"SRT 字幕文件已生成：{srt_path}")