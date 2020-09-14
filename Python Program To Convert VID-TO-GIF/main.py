import imageio
import os as os

video_location = os.path.abspath('VID_20200831_185046.mp4')
print('\nThe Location Of Your File Is :- ', video_location)

def Convert(inputPath, desired_format):
    outputPath = os.path.splitext(inputPath)[0] + desired_format

    print(f'Converting :: {inputPath} \n To {outputPath}')

    reader = imageio.get_reader(inputPath)
    fps = reader.get_meta_data()['fps']
    fps_to_be_used = fps-20
    writer = imageio.get_writer(outputPath, fps=fps_to_be_used)

    for frames in reader:
        writer.append_data(frames)
        print(f'Frame {frames}')

    print('Done!')
    writer.close()


Convert(video_location, '.gif')