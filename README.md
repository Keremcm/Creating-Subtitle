# Video Subtitle Generator and Translator

This project provides a Python-based tool to extract audio from videos, transcribe it into text, translate it into various languages, and generate subtitle files in SRT format. It also includes a user-friendly graphical interface built with [Flet](https://flet.dev/).

## Features

1. **Audio-to-Text Transcription**:
   - Extracts audio from video files.
   - Transcribes the audio using Google's Speech Recognition API.

2. **Subtitles Generation**:
   - Splits transcribed text into segments for subtitle creation.
   - Outputs subtitle files in the SRT format.

3. **Translation**:
   - Uses Google Translate API to translate the transcribed text into a target language.

4. **Graphical Interface**:
   - A simple and intuitive interface to process videos.
   - Options to select video language, subtitle language, and output file name.

## Requirements

- Python 3.8 or later
- Required Python packages:
  - `speechrecognition`
  - `moviepy`
  - `googletrans==4.0.0-rc1`
  - `flet`

## Installation

1. Clone this repository or download the script.
2. Install the required Python packages:
   ```bash
   pip install speechrecognition moviepy googletrans==4.0.0-rc1 flet
   ```

## Usage

### Running the Application

1. Run the script:
   ```bash
   python script_name.py
   ```
2. The graphical interface will open, allowing you to input:
   - Video file path
   - Video language (e.g., English, Turkish, Spanish)
   - Target subtitle language
   - Output file name

3. Click the "Create Subtitle File" button to process the video. The generated SRT file will be saved to the specified output path.

### Processing Example

- Input a video file (e.g., `sample.mp4`).
- Select the video language as English (`en-US`).
- Choose the subtitle language as Turkish (`tr`).
- Specify an output file name (e.g., `output_subtitles.srt`).
- Click the button to generate a Turkish subtitle file.

## Code Structure

1. **Audio Extraction and Transcription**:
   - Extracts audio from video using `moviepy`.
   - Converts audio to text using `speechrecognition`.

2. **Subtitle Segmentation**:
   - Splits transcribed text into fixed-duration segments for subtitle creation.

3. **SRT File Generation**:
   - Formats subtitles into SRT format, including time stamps.

4. **Text Translation**:
   - Translates text into the desired language using Google Translate.

5. **Flet-Based UI**:
   - Allows users to process videos through an easy-to-use interface.

## Example Output

Example SRT file:
```srt
1
00:00:00,000 --> 00:00:05,000
This is an example subtitle.

2
00:00:05,000 --> 00:00:10,000
Here is another line of subtitles.
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [MoviePy](https://zulko.github.io/moviepy/)
- [Google Translate](https://cloud.google.com/translate/docs)
- [Flet](https://flet.dev/)

