import sounddevice as sd
import numpy as np
import inflect

def matrix_to_words(matrix):
    p = inflect.engine()

    words = []
    for row in matrix:
        row_words = [p.number_to_words(num) for num in row]
        words.append(" ".join(row_words))

    return words

def detect_sound():
    # Set the sample rate and duration for capturing audio
    sample_rate = 44100  # Hz
    duration = 5  # seconds

    # Capture audio
    print("Listening for sound...")
    audio_data = sd.rec(int(sample_rate * duration), samplerate=sample_rate, channels=1, dtype='int16')
    sd.wait()

    # Analyze audio data (you can customize this based on your specific requirements)
    audio_mean = np.mean(audio_data)
    audio_max = np.max(audio_data)

    # Adjust the threshold based on your environment and microphone sensitivity
    threshold = 5000

    # Trigger action if the sound exceeds the threshold
    if audio_max > threshold:
        print("Sound detected!")
        print(f"Max amplitude: {audio_max}")
        print(f"Mean amplitude: {audio_mean}")
        print("Sound data:")
        # print(audio_data)
        # Add your desired action here

        resulting_words = matrix_to_words(audio_data)
        for row_words in resulting_words:
            print(row_words)

if __name__ == "__main__":
    detect_sound()
