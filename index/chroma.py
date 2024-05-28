import librosa

# Load the audio file
audio_file_path = '1.wav'
y, sr = librosa.load(audio_file_path, sr=None, duration=10)  # Load 10 seconds of audio

# Compute the chromagram
chromagram = librosa.feature.chroma_stft(y=y, sr=sr)

# Calculate the mean of the chroma bands across all frames
chromagram_mean = chromagram.mean(axis=1)

result = sum(chromagram_mean)/len(chromagram_mean)
print(result)
