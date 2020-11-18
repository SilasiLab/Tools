import cv2
import os

'''
1. Make a project folder
2. Set project_path to the path to this folder
3. Put all the videos you want to be split up into one folder
4. Set input_dir_path to the path to the folder with the videos
5. Place this script in the project folder
6. Open a terminal and run python main.py
7. Navigate to project folder and check results in [project folder]/split_videos
'''

input_dir_path = '/home/gavin/zanna_vid_splitter/Aim 1a selection-20201117T210204Z-001/Aim 1a selection'
project_path = '/home/gavin/zanna_vid_splitter'

class split_vids:
    def __init__(self, input_dir_path, project_path):
        self.input_dir_path = input_dir_path
        self.project_path = project_path

    def video_file_splitter(self):
        # output avis will be stored in [your project dir]/split_videos

        output_dir = self.project_path + os.sep + 'split_videos'

        try:
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
        except OSError:
            print ('Error: Creating directory')
        
        vids2split = []
        num_vids = 0
        for f in os.listdir(self.input_dir_path):
            if f[-3:] == 'mp4' or f[-3:] == 'avi':
                vids2split.append(f)
                num_vids += 1
        if num_vids < 1:
            print('videos not found: please check path to videos folder and try again')
        else:
            print('splitting {} video(s)'.format(num_vids))
        
        while vids2split:
            curr = vids2split.pop()

            if not os.path.exists(self.project_path + os.sep + 'split_videos' + os.sep + curr[:-4]):
                os.mkdir(self.project_path + os.sep + 'split_videos' + os.sep + curr[:-4])
            
            curr_dir = self.project_path + os.sep + 'split_videos' + os.sep + curr[:-4]

            cap = cv2.VideoCapture(self.input_dir_path + os.sep + curr)

            # get height and width from opencv
            if cap.isOpened():
                w = cap.get(3) # 3 = cv2.CAP_PROP_FRAME_WIDTH
                h = cap.get(4) # 4 = cv2.CAP_PROP_FRAME_HEIGHT
                fps = cap.get(5) # 5 is FPS and returned 60 (correct)
                print('video height and width: {}, {}'.format(h, w))
                print('fps: ', fps)

            fn_01 = curr_dir + os.sep + '01_' + curr[:-4] + '.avi'
            fn_02 = curr_dir + os.sep + '02_' + curr[:-4] + '.avi'
            fn_03 = curr_dir + os.sep + '03_' + curr[:-4] + '.avi'
            fn_04 = curr_dir + os.sep + '04_' + curr[:-4] + '.avi'
            fn_05 = curr_dir + os.sep + '05_' + curr[:-4] + '.avi'
            fn_06 = curr_dir + os.sep + '06_' + curr[:-4] + '.avi'
            fn_07 = curr_dir + os.sep + '07_' + curr[:-4] + '.avi'
            fn_08 = curr_dir + os.sep + '08_' + curr[:-4] + '.avi'
            fn_09 = curr_dir + os.sep + '09_' + curr[:-4] + '.avi'
            fn_10 = curr_dir + os.sep + '10_' + curr[:-4] + '.avi'
            fn_11 = curr_dir + os.sep + '11_' + curr[:-4] + '.avi'
            fn_12 = curr_dir + os.sep + '12_' + curr[:-4] + '.avi'
            fn_13 = curr_dir + os.sep + '13_' + curr[:-4] + '.avi'
            fn_14 = curr_dir + os.sep + '14_' + curr[:-4] + '.avi'
            fn_15 = curr_dir + os.sep + '15_' + curr[:-4] + '.avi'
            fn_16 = curr_dir + os.sep + '16_' + curr[:-4] + '.avi'
            fn_17 = curr_dir + os.sep + '17_' + curr[:-4] + '.avi'

            fourcc = cv2.VideoWriter_fourcc(*'MJPG')
            w, h, fps = int(w), int(h), int(fps)

            vw_01 = cv2.VideoWriter(fn_01, fourcc, fps, (w, h))
            vw_02 = cv2.VideoWriter(fn_02, fourcc, fps, (w, h))
            vw_03 = cv2.VideoWriter(fn_03, fourcc, fps, (w, h))
            vw_04 = cv2.VideoWriter(fn_04, fourcc, fps, (w, h))
            vw_05 = cv2.VideoWriter(fn_05, fourcc, fps, (w, h))
            vw_06 = cv2.VideoWriter(fn_06, fourcc, fps, (w, h))
            vw_07 = cv2.VideoWriter(fn_07, fourcc, fps, (w, h))
            vw_08 = cv2.VideoWriter(fn_08, fourcc, fps, (w, h))
            vw_09 = cv2.VideoWriter(fn_09, fourcc, fps, (w, h))
            vw_10 = cv2.VideoWriter(fn_10, fourcc, fps, (w, h))
            vw_11 = cv2.VideoWriter(fn_11, fourcc, fps, (w, h))
            vw_12 = cv2.VideoWriter(fn_12, fourcc, fps, (w, h))
            vw_13 = cv2.VideoWriter(fn_13, fourcc, fps, (w, h))
            vw_14 = cv2.VideoWriter(fn_14, fourcc, fps, (w, h))
            vw_15 = cv2.VideoWriter(fn_15, fourcc, fps, (w, h))
            vw_16 = cv2.VideoWriter(fn_16, fourcc, fps, (w, h))
            vw_17 = cv2.VideoWriter(fn_17, fourcc, fps, (w, h))

            frame_cnt = 0
            while(True):
                ret, frame = cap.read()
                frame_cnt += 1
                if ret:
                    gray = cv2.cvtColor(src=frame, code=cv2.COLOR_BGR2GRAY)

                    if frame_cnt > fps*60*0 and frame_cnt <= fps*60*1:
                        vw_01.write(frame)
                    if frame_cnt > fps*60*1 and frame_cnt <= fps*60*2:
                        vw_02.write(frame)
                    if frame_cnt > fps*60*2 and frame_cnt <= fps*60*3:
                        vw_03.write(frame)
                    if frame_cnt > fps*60*3 and frame_cnt <= fps*60*4:
                        vw_04.write(frame)
                    if frame_cnt > fps*60*4 and frame_cnt <= fps*60*5:
                        vw_05.write(frame)
                    if frame_cnt > fps*60*5 and frame_cnt <= fps*60*6:
                        vw_06.write(frame)
                    if frame_cnt > fps*60*6 and frame_cnt <= fps*60*7:
                        vw_07.write(frame)
                    if frame_cnt > fps*60*7 and frame_cnt <= fps*60*8:
                        vw_08.write(frame)
                    if frame_cnt > fps*60*8 and frame_cnt <= fps*60*9:
                        vw_09.write(frame)
                    if frame_cnt > fps*60*9 and frame_cnt <= fps*60*10:
                        vw_10.write(frame)
                    if frame_cnt > fps*60*10 and frame_cnt <= fps*60*11:
                        vw_11.write(frame)
                    if frame_cnt > fps*60*11 and frame_cnt <= fps*60*12:
                        vw_12.write(frame)
                    if frame_cnt > fps*60*12 and frame_cnt <= fps*60*13:
                        vw_13.write(frame)
                    if frame_cnt > fps*60*13 and frame_cnt <= fps*60*14:
                        vw_14.write(frame)
                    if frame_cnt > fps*60*14 and frame_cnt <= fps*60*15:
                        vw_15.write(frame)
                    if frame_cnt > fps*60*15 and frame_cnt <= fps*60*16:
                        vw_16.write(frame)
                    if frame_cnt > fps*60*16 and frame_cnt <= fps*60*17:
                        vw_17.write(frame)

                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                else:
                    break

            cap.release()
            vw_01.release()
            vw_02.release()
            vw_03.release()
            vw_04.release()
            vw_05.release()
            vw_06.release()
            vw_07.release()
            vw_08.release()
            vw_09.release()
            vw_10.release()
            vw_11.release()
            vw_12.release()
            vw_13.release()
            vw_14.release()
            vw_15.release()
            vw_16.release()
            vw_17.release()
            cv2.destroyAllWindows()


def main():
    sv = split_vids(input_dir_path, project_path)
    sv.video_file_splitter()


if __name__ == '__main__':
    DEBUG = False

    if DEBUG:
        pass
    else:
        main()