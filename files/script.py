# set to trasnlate from portuguese, can change on line 56

import torch
import os
import time
from transformers import pipeline
import datetime
import warnings
import pathlib

warnings.filterwarnings("ignore")

print(f"number of GPUs: {torch.cuda.device_count()}")
print([torch.cuda.get_device_name(i) for i in range(torch.cuda.device_count())])

device = "cuda:0" if torch.cuda.is_available() else exit(1)

print("Device: ", torch.cuda.get_device_name(device))
print("Capabilities: ", torch.cuda.get_device_properties(device))

pipe = pipeline(
  "automatic-speech-recognition",
  model="openai/whisper-large-v3-turbo",
  chunk_length_s=30,
  device=device,
)



audio_folder = pathlib.Path("/audios")
# audio_folder = "/mnt/"

mp3_files = audio_folder.glob("*.mp3")
mp3_files = [os.path.join(audio_folder, f) for f in os.listdir(audio_folder) if f.lower().endswith('.mp3')]
mp3_files.sort()

print(f"\n{len(mp3_files)} archives found.")

for i, audio_file_path in enumerate(mp3_files):

  print(f"\n Processing {i + 1}/{len(mp3_files)}: {os.path.basename(audio_file_path)}")

  path = pathlib.Path(audio_file_path)
  base_name = path.stem
  full_path_text = pathlib.Path(f"/mnt/texts/{base_name}.txt")

  if full_path_text.exists():
    print(f" {base_name} already processed.")
    continue

  start = time.time()

  try:
    transcription = pipe(audio_file_path, generate_kwargs={"language": "portuguese"})['text']
  except Exception as e:
    print(f" Error Processing {base_name}\n")
    print(e)
    continue
  else:
    end = time.time()
    print(f" ({datetime.timedelta(seconds = end-start)})")

  with open(full_path_text, "w") as f:
    f.write(transcription)

