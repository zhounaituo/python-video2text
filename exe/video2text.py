#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import time
import speech_recognition as sr # 创建 Google 识别器对象
from ffmpy3 import FFmpeg
from retrying import retry
from pip._vendor.distlib.compat import raw_input

r = sr.Recognizer()      # 创建一个识别器实例
video_dir = r'./Video';
text_dir  = r'./Text';   # 数据输出路径
audio_dir = r'./Audio';  # 待转换视频存放的路径 

def mkdirs(dirs): 
    '''创建/确认保存目录'''
    existence = os.path.exists(dirs) 
    if not existence: 
        print(f'创建 {dirs} 存放目录...........') 
        os.makedirs(dirs)  # 创建目录 audio_dir
        mkdirs(dirs);
    else: 
        print(f'{dirs} 目录创建成功！') 
        return True;

def to_audio(video_name):
    ''' 将视频转换为音频'''
    if os.path.exists(audio_dir):
        print(f'已确定 {audio_dir} 目录存在，继续执行...............');
        changefile = video_dir+"/"+video_name
        outputfile = audio_dir+"/"+video_name.replace("mp4","wav"); # 语音文件
        if not os.path.exists(outputfile):
            ff = FFmpeg(
                executable=r'D:\Users\admin\Desktop\ffmpeg-2022-10-10-git-f3b5277057-full_build\ffmpeg\bin\ffmpeg', # 配置ffmpeg 地址
                inputs={changefile: None},
                outputs={outputfile: '-vn -ar 44100 -ac 2 -ab 192 -f wav'}
                )
            ff.run();
            return to_audio(video_name)
        else:
            print(f'video2audio -> {outputfile} 转换成功..........')
            return outputfile;
                
    else:
        mkdirs(audio_dir);
        return to_audio(video_name);

@retry()
def to_text(audio_name):
    ''' 将音频转换成文字 '''
    if os.path.exists(text_dir):
        print(f'已确定 {text_dir} 目录存在，继续执行.........')
        changefile = audio_dir+'/'+audio_name; # ./Audio/videoplayback.wav
        outputfile = text_dir+'/'+audio_name.replace('wav','txt');
        if not os.path.exists(outputfile):
            with sr.AudioFile(changefile) as source:
                audio_text = r.record(source)
                text = r.recognize_google(audio_text)
            file = open(outputfile, 'w');
            file.write(text);
            file.close();
            print(audio_name);
            to_text(audio_name);
        else:
            print(f'audio2text -> {outputfile} 转换成功........')
            print(r'----------------------------')
            print(f'文件保存在 {outputfile} 中。')
            return True
    else:
        mkdirs(text_dir);
        to_text(audio_name);

for video_name in [videos for videos in os.listdir(video_dir) if videos.find('.mp4') >= 0]:
    audio_name = to_audio(video_name).split('/');
    to_text(audio_name[len(audio_name)-1]);
    
raw_input("Press");