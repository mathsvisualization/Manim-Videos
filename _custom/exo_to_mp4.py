import subprocess
import os

def exo_to_mp4(input_exo):
    # Automatically generate output file name by replacing .exo with .mp4
    output_mp4 = os.path.splitext(input_exo)[0] + ".mp4"
    
    # FFmpeg command to convert .exo to .mp4
    command = ['ffmpeg', '-i', input_exo, '-c:v', 'libx264', '-preset', 'fast', '-crf', '22', output_mp4]
    
    try:
        subprocess.run(command, check=True)
        print(f"Conversion completed: {output_mp4}")
    except subprocess.CalledProcessError as e:
        print(f"Error during conversion: {e}")

# Example usage
input_exo_file = "input.exo"  # Replace this with your actual .exo file name

exo_to_mp4(input_exo_file)
