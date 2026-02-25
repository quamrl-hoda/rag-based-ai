import os
import subprocess
files = os.listdir("videos")
print(files)



for file in files:

  # Step 1: split by underscore
  parts = file.split('_')

  # Step 2: find tutorial number (after 'Tutorial')
  tutorial_number = parts[parts.index('Tutorial') + 1]
  file_name = file.split('.')[0].split('_Sigma_')[0]
  print(tutorial_number,file_name)

  subprocess.run(["ffmpeg", "-i", f"videos/{file}", f"audios/{tutorial_number}_{file_name}.mp3"])