# Subtitle Extractor with Whisper

![image](https://github.com/user-attachments/assets/870ea965-f8a6-407a-b485-8cebd4a1769e)

An interactive application for **extracting subtitles from video files** using `OpenAI Whisper`, `moviepy`, and `gradio`.

![image](https://github.com/user-attachments/assets/0968f994-4439-422b-9a8c-94a663ab33a2)
## 🚀 Features
* ✅ Upload **single or multiple video files** (`.mp4`)
* ✅ Automatic audio extraction from videos
* ✅ Speech recognition using **OpenAI Whisper**
* ✅ Generate `.srt` (time-coded subtitles) and `.txt` files
* ✅ Automatic language detection
* ✅ Package all subtitles as downloadable ZIP archive
* ✅ JSON summary with language detection and previews
* ✅ Choose Whisper model size (`tiny`, `base`, `small`, `medium`, `large`)
* ✅ Clean modern interface with Gradio
* ✅ Local deployment and easy setup

## 🛠️ Installation
1. Clone this repository:
```bash
git clone https://github.com/mvulcu/whispercraft.git
cd whispercraft
```
2. Install dependencies:
```bash
pip install openai-whisper gradio moviepy
```
3. Make sure **ffmpeg** is installed:
   * **Windows**: Download from https://www.gyan.dev/ffmpeg/builds/
   * **Ubuntu/Debian**: `sudo apt install ffmpeg`
   * **MacOS**: `brew install ffmpeg`

## 🧠 Technologies Used
| Library | Purpose |
|---------|---------|
| `whisper` | Speech recognition |
| `moviepy` | Audio extraction from video files |
| `gradio` | Web interface for user interaction |
| `ffmpeg` | Support for video/audio formats |
| `zipfile` | Bundling output files for download |
| `shutil`, `os` | File and path operations |

## ⚙️ Project Structure
### Main Function: `extract_subtitles_batch(...)`
* Loads the appropriate Whisper model
* Processes multiple video files in sequence
* Extracts audio using MoviePy
* Performs speech recognition with error handling
* Saves `.srt` and `.txt` files
* Bundles all outputs in a ZIP archive
* Returns structured JSON results with preview text

### Gradio Interface
Built with `gr.Blocks`:
* Clean, modern user interface
* Multi-file upload component
* Model selection dropdown
* JSON display for easy result review
* Single-click ZIP download of all outputs

## 🖼 Interface Elements
* 🎞 **Upload Videos** — upload multiple `.mp4` files
* 🧠 **Whisper Model** — select model size (`tiny`, `base`, etc.)
* 🪄 **Extract Subtitles** — primary action button
* 📋 **Result Summary** — structured JSON display with previews
* 📦 **Download All Subtitles** — complete ZIP bundle

## 🔄 How to Run
```bash
python subtitle_app.py
```
Gradio will launch at:
```
http://127.0.0.1:7860
```

## 📁 Results
For each processed video:
* A `.srt` file with timestamped subtitles
* A `.txt` file with complete transcription
* JSON summary with language detection
* A sample preview of the transcription
* All files bundled in a downloadable ZIP archive

## ⚠️ Tips
* If you encounter `PermissionError`, make sure the video is **not open** in another application.
* Larger models (like "medium" and "large") provide better accuracy but are slower and require more memory.
* The "tiny" model is fastest but may have more transcription errors.
* Whisper runs on CPU by default, but you can use GPU with CUDA for faster processing.

## 💡 Future Development Ideas
* Subtitle translation capabilities
* Built-in video player with subtitle overlay
* Support for more video formats (`.avi`, `.mov`, `.mkv`, etc.)
* Advanced language filtering and editing options
* Custom subtitle styling and formatting
* Batch processing optimization for large collections

## 👨‍💻 Author
Created with ❤️ as a pet project for automating work with video and educational content.

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
