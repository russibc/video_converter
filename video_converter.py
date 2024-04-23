from pytube import YouTube
import moviepy.editor as mp
import os

def download_video(url, output_path):
    yt = YouTube(url)
    stream = yt.streams.filter(only_audio=True).first()
    filename = stream.default_filename
    file_path = os.path.join(output_path, filename)
    stream.download(output_path=output_path)
    return file_path

def convert_to_mp3(input_path, output_path):
    clip = mp.AudioFileClip(input_path)
    clip.write_audiofile(output_path)
    clip.close()

def main():
    youtube_url = ''
    output_path = os.getcwd()

    # Download video
    print('Downloading video...')
    file_path = download_video(youtube_url, output_path)

    # Convert to MP3
    print('Converting to MP3...')
    output_file = os.path.splitext(os.path.basename(file_path))[0] + '.mp3'
    output_path = os.path.join(output_path, output_file)
    convert_to_mp3(file_path, output_path)

    print('Conversion completed successfully!')

if __name__ == '__main__':
    main()
