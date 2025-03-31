import whisper
import gradio as gr
from moviepy.video.io.VideoFileClip import VideoFileClip
import shutil
import os
import zipfile

available_models = ["tiny", "base", "small", "medium", "large"]

model_name = "base"
model = whisper.load_model(model_name)


def extract_subtitles_batch(video_files, model_size, progress=None):
    global model, model_name
    if progress is None:
        progress = gr.Progress()
    if model_size != model_name:
        progress(0.05, desc="🔄 Loading model...")
        model = whisper.load_model(model_size)
        model_name = model_size

    results = []
    zip_filename = "subtitles_bundle.zip"

    with zipfile.ZipFile(zip_filename, "w") as zipf:
        for index, video_file_path in enumerate(video_files):
            progress(
                (index / len(video_files)) * 0.9,
                desc=f"📁 Processing file {index + 1} of {len(video_files)}",
            )

            temp_video_path = f"uploaded_video_{index}.mp4"
            temp_audio_path = f"extracted_audio_{index}.wav"
            srt_output_path = f"subtitles_{index}.srt"
            txt_output_path = f"subtitles_{index}.txt"

            shutil.copy(video_file_path, temp_video_path)

            video = VideoFileClip(temp_video_path)
            video.audio.write_audiofile(temp_audio_path)
            try:
                video.reader.close()
                if video.audio and hasattr(video.audio, "reader"):
                    video.audio.reader.close()
            except Exception as e:
                print(f"⚠️ Error closing video: {e}")

            result = model.transcribe(temp_audio_path, verbose=False)
            detected_language = result.get("language", "unknown")

            def format_timestamp(seconds):
                h = int(seconds // 3600)
                m = int((seconds % 3600) // 60)
                s = int(seconds % 60)
                ms = int((seconds - int(seconds)) * 1000)
                return f"{h:02}:{m:02}:{s:02},{ms:03}"

            with open(srt_output_path, "w", encoding="utf-8") as f:
                for i, segment in enumerate(result["segments"]):
                    f.write(f"{i+1}\n")
                    f.write(
                        f"{format_timestamp(segment['start'])} --> {format_timestamp(segment['end'])}\n"
                    )
                    f.write(f"{segment['text'].strip()}\n\n")

            with open(txt_output_path, "w", encoding="utf-8") as f:
                f.write(result["text"])

            zipf.write(srt_output_path)
            zipf.write(txt_output_path)

            os.remove(temp_video_path)
            os.remove(temp_audio_path)

            results.append(
                {
                    "video": os.path.basename(video_file_path),
                    "language": detected_language,
                    "text_sample": result["text"][:200] + "...",
                    "srt": srt_output_path,
                    "txt": txt_output_path,
                }
            )

    progress(1.0, desc="✅ All Done!")
    return results, zip_filename


with gr.Blocks() as app:
    gr.Markdown(
        """
    # 🎬 Whisper Subtitle Extractor
    _Transcribe multiple videos with subtitles and language detection._
    """
    )

    with gr.Row():
        video_input = gr.File(
            label="🎞 Upload Videos",
            type="filepath",
            file_types=[".mp4"],
            file_count="multiple",
        )
        model_dropdown = gr.Dropdown(
            label="🧠 Whisper Model", choices=available_models, value="base"
        )

    extract_button = gr.Button("🪄 Extract Subtitles", variant="primary")
    result_json = gr.JSON(label="📋 Result Summary")
    zip_output = gr.File(label="📦 Download All Subtitles (.zip)")

    extract_button.click(
        fn=extract_subtitles_batch,
        inputs=[video_input, model_dropdown],
        outputs=[result_json, zip_output],
    )

app.launch()
