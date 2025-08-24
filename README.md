# whisper-amdgpu

Docker container to use Whisper with AMD GPUs.

The build process will take some time and will create a huge container (over 50gb in my case).

The build/download.py script will be invoked during the build process to pre-cache the Whisper model.

The files/script.py will run Whisper to transcribe a file named files/audio.mp3

For comparison, on tests, my GPU(rx 6750xt) transcribe an hour of audio .mp3 in approximately 5 minutes.

## PLEASE NOTE

You need to change in transcribe-audio.sh path to the folder with the archives you want to transcribe.

You might need to adapt the `--device` options to your system check `ls -l /dev/dri/by-path` and `lspci` to identify your card correctly.
