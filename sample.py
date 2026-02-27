import subprocess
import whisper
import  os

# Step 1: Extract 10s audio from video
video_file = "videos/Your_First_HTML_Website_Sigma_Web_Development_Course_-_Tutorial_2_720P.mp4"
audio_file = "audios/audio_10s.mp3"

subprocess.run([
    "ffmpeg", "-i", video_file,
    "-t", "10",
    "-map", "a",
    audio_file
])

# Step 2: Load Whisper model
model = whisper.load_model("large-v2")

# Step 3: Transcribe
result = model.transcribe(audio_file)

print("Transcription:")
print(result["text"])

os.makedirs(audio_folder, exist_ok=True)

# -------- Extract 10 seconds audio --------
subprocess.run([
    "ffmpeg",
    "-i", video_file,
    "-t", "10",
    "-map", "a",
    audio_file
])

# -------- Load Whisper model --------
model = whisper.load_model("small")

# -------- Transcribe --------
result = model.transcribe(audio_file)

print("Transcription:")
print(result["text"])