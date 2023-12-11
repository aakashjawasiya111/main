import subprocess  #used to run shell commands from the Python program.
import datetime
import os    # used for creating directories.

#records_rtsp_stream
class records_rtsp_stream:
    def __init__(self,rtsp_url,output_directory): #rtsp_url: The URL of the RTSP stream to record #output_directory: The directory where the recorded video segments will be saved.
        if not os.path.exists(output_directory): # for check directory
            os.makedirs(output_directory)  # for create directory



        segment_duration= 120 # Define the segment duration in seconds


        filename_pattern=os.path.join(output_directory,"video_%Y%m%d_%H%M%S.mp4")# Generate the filename pattern
        # frame_count=0
        



        try:      # Start recording
            output_file= datetime.datetime.now().strftime(filename_pattern) #output_file is generated using the current timestamp and the filename pattern
                # Build the ffmpeg command
            ffmpeg_cmd= [   
                'ffmpeg', 
                '-i',rtsp_url,   #input URL (-i),
                '-t', str(segment_duration),  #segment duration (-t), 
                '-c:v','copy', #video codec (-c:v), audio codec (-c:a),
                '-c:a','aac',
                output_file,
            ]
            # frame_count +=1
            # print(frame_count)
            subprocess.run(ffmpeg_cmd)#,stdout=subprocess.PIPE, stderr=subprocess.PIPE)  # Run ffmpeg using subprocess
        
        except KeyboardInterrupt:   # for manualy intruption
            print('Recording stopped')
    


# if __name__=='__main__':
rtsp_url= 'rtsp://aivid:aivid_2022@192.168.111.104:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif'
output_directory= '/home/aivid9/Desktop' # Change this to your desired output directory
#records_rtsp_stream(rtsp_url,output_directory)
result=records_rtsp_stream(rtsp_url,output_directory)
#result.records_rtsp_stream(rtsp_url,output_directory)


