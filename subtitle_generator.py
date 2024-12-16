import speech_recognition as sr
import moviepy.editor as mp
import os
import flet as ft
from googletrans import Translator

# Sesin metne dönüştürülmesi
def extract_audio_and_transcribe(video_path, video_language="en-US"):
    video = mp.VideoFileClip(video_path)
    audio_path = "temp_audio.wav"
    video.audio.write_audiofile(audio_path)
    
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data, language=video_language)
    
    os.remove(audio_path)  # Geçici ses dosyasını siliyoruz
    return text

# Metni belirli uzunluklarda parçalara bölme
def split_text_into_subtitles(text, segment_duration=5):
    words = text.split()
    subtitles = []
    start_time = 0

    for i in range(0, len(words), 10):  # Her 10 kelimeyi bir altyazı olarak alıyoruz
        segment_text = ' '.join(words[i:i + 10])
        end_time = start_time + segment_duration
        subtitles.append(((start_time, end_time), segment_text))
        start_time = end_time
    
    return subtitles

# Altyazı dosyasını oluşturma (SRT formatında)
def create_srt_file(subtitles, output_path="output_subtitles.srt"):
    with open(output_path, "w", encoding="utf-8") as f:
        for idx, (times, text) in enumerate(subtitles):
            start_time, end_time = times
            start_time_str = format_time(start_time)
            end_time_str = format_time(end_time)
            
            f.write(f"{idx + 1}\n")
            f.write(f"{start_time_str} --> {end_time_str}\n")
            f.write(f"{text}\n\n")

# Zamanı SRT formatına dönüştürme
def format_time(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = int(seconds % 60)
    milliseconds = int((seconds % 1) * 1000)
    return f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"

# Metni çevirmek için translate modülü
def translate_text(text, target_language="tr"):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language).text
    return translated_text

# Flet arayüzü
def main(page: ft.Page):
    page.title = "Video Altyazı Dosyası Oluşturma ve Çeviri"
    page.window_width = 600
    page.window_height = 500

    # Arayüz elemanları
    video_path_input = ft.TextField(label="Video Dosyası Yolu")
    video_language_dropdown = ft.Dropdown(
        options=[
            ft.dropdown.Option("en-US", "English"),
            ft.dropdown.Option("tr-TR", "Turkish"),
            ft.dropdown.Option("es-ES", "Spanish"),
            # Farklı diller ekleyebilirsiniz
        ],
        label="Video Dili",
        value="en-US"
    )
    subtitle_language_dropdown = ft.Dropdown(
        options=[
            ft.dropdown.Option("en", "English"),
            ft.dropdown.Option("tr", "Turkish"),
            ft.dropdown.Option("es", "Spanish"),
            # Altyazı dillerini ekleyebilirsiniz
        ],
        label="Altyazı Dili",
        value="tr"
    )
    output_path_input = ft.TextField(label="Çıkış Dosyası Adı", value="output_subtitles.srt")
    result_text = ft.Text()
    process_button = ft.ElevatedButton(text="Altyazı Dosyasını Oluştur", on_click=lambda e: process_video(e))

    # İşleme fonksiyonu
    def process_video(event):
        video_path = video_path_input.value
        video_language = video_language_dropdown.value
        subtitle_language = subtitle_language_dropdown.value
        output_path = output_path_input.value

        result_text.value = "Altyazı hazırlanıyor, lütfen bekleyin..."
        page.update()

        try:
            # Videodan metni çıkar
            text = extract_audio_and_transcribe(video_path, video_language)
            # Altyazı diline çevir
            translated_text = translate_text(text, subtitle_language)
            # Çevrilmiş metni altyazı segmentlerine böl
            subtitles = split_text_into_subtitles(translated_text)
            # Altyazı dosyasını oluştur
            create_srt_file(subtitles, output_path)
            
            result_text.value = f"İşlem tamamlandı! Altyazı dosyası: {output_path}"
        except Exception as e:
            result_text.value = f"Hata oluştu: {e}"
        
        page.update()

    # Arayüz bileşenlerini ekleme
    page.add(
        video_path_input,
        video_language_dropdown,
        subtitle_language_dropdown,
        output_path_input,
        process_button,
        result_text,
    )

ft.app(target=main)
