# python-video2text
> 利用 python 将视频转换为文本。

## 使用方式
请使用这个目录结构：
![[dir_img.png]]
## 立即使用
软件路径存放在 `./video2text.exe` 中，安装前请阅读 `readme.txt`
> 	暂时仅支持 .mp4 转 .txt
> 	仅有 window11 版，window 其他版本可以自行测试。

## 思路
> 1. 视频 -> 音频：利用 FFmpeg 将视频转化成音频文件。
> 2. 音频 -> 文本：利用 Speech-recognition 将音频转化为文本。

## 视频 -> 音频
```python
from ffmpy3 import FFmpeg
r = sr.Recognizer() # 创建一个识别器实例
changefile = ''; # 视频文件, ./Video/video.mp4
outputfile = ''; # 音频文件, ./Audio/audio.wav
ff = FFmpeg(
	executable=r'D:\Users\admin\Desktop\ffmpeg-2022-10-10-git-f3b5277057-full_build\ffmpeg\bin\ffmpeg', # 配置ffmpeg 地址
	inputs={changefile: None},
	outputs={outputfile: '-vn -ar 44100 -ac 2 -ab 192 -f wav'}
	)
ff.run();
```
> 出现错误请查询参考文档。

## 音频 -> 文本
利用 google 识别。
```python
changefile = ''; # 音频文件, ./Audio/audio.wav
outputfile = ''; # 文本文件, ./Text/text.text
with sr.AudioFile(changefile) as source:
	audio_text = r.record(source)
	text = r.recognize_google(audio_text); # 音频 -> 文本
file = open(outputfile, 'w');
file.write(text);
file.close();
print(audio_name);
```

## 参考文档
1. [语音识别教程](https://zhuanlan.zhihu.com/p/157179730#:~:text=AI%E6%95%99%E7%A8%8B%E5%B7%A5%E5%85%B7%E7%AE%B1%E7%B3%BB%E5%88%97%7C%20%E4%BD%BF%E7%94%A8Python%E5%B0%86%E8%AF%AD%E9%9F%B3%E8%BD%AC%E6%8D%A2%E4%B8%BA%E6%96%87%E6%9C%AC%201%20%E4%BD%9C%E8%80%85%EF%BC%9ABehic%20Guven%202%20%E7%BC%96%E8%AF%91%EF%BC%9AFlorence%20Wong,4%20%E8%AE%A9%E6%88%91%E4%BB%AC%E5%BC%80%E5%A7%8B%E7%BC%96%E7%A0%81%E5%90%A7%EF%BC%81%205%20%E5%88%9B%E5%BB%BA%E4%B8%80%E4%B8%AA%E8%AF%86%E5%88%AB%E5%99%A8%206%20%E5%AE%9A%E4%B9%89%E4%BD%A0%E7%9A%84%E9%BA%A6%E5%85%8B%E9%A3%8E%207%20%E6%9C%80%E5%90%8E%E4%B8%80%E6%AD%A5%EF%BC%9A%E5%AF%BC%E5%87%BA%E7%BB%93%E6%9E%9C)
2. [用 Python 轻松实现语音转文本](https://www.agora.io/cn/community/blog/21942)
3. [利用Python如何将视频转换为音频](https://www.yisu.com/zixun/156548.html)
4.  [ffmpeg](http://ffmpeg.org/)
5. [python使用speech_recognition进行语音识别及响应超时的解决办法](https://blog.csdn.net/weixin_47597012/article/details/118797607)

------------
