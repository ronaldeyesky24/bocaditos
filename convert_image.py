from PIL import Image
import sys

def convert_png_to_jpg(input_path, output_path):
    try:
        with Image.open(input_path) as img:
            rgb_img = img.convert('RGB')
            rgb_img.save(output_path, 'JPEG', quality=95)
        print(f"Successfully converted {input_path} to {output_path}")
    except Exception as e:
        print(f"Error during conversion: {e}")
        sys.exit(1)

if __name__ == "__main__":
    src = r"C:\Users\out\.gemini\antigravity\brain\c1fed8b2-3f57-4814-b627-02dae8e3399a\flyer_bocaditos_1775195280015.png"
    dst = r"c:\Users\out\Documents\NOTEBOOKLM\bocaditos\flyer_bocaditos.jpg"
    convert_png_to_jpg(src, dst)
