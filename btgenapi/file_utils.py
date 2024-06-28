import base64
import datetime
from io import BytesIO
import os
import numpy as np
from PIL import Image
import uuid

output_dir = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', 'outputs', 'files'))
os.makedirs(output_dir, exist_ok=True)

static_serve_base_url = 'http://127.0.0.1:8887/files/'


def ndarray_to_base64(image_array):
    """
    Convert a numpy ndarray representing an image into a base64-encoded string.
    
    Parameters:
    image_array (np.ndarray): The numpy array representing the image.

    Returns:
    str: The base64-encoded string of the image.
    """
    # Convert numpy array to PIL Image
    image = Image.fromarray(image_array)
    
    # Save PIL Image to a bytes buffer
    buffer = BytesIO()
    image.save(buffer, format="PNG")
    buffer.seek(0)
    
    # Encode the bytes buffer into base64
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    
    return image_base64

def save_output_file(img: np.ndarray) -> str:
    current_time = datetime.datetime.now()
    date_string = current_time.strftime("%Y-%m-%d")

    filename = os.path.join(date_string, str(uuid.uuid4()) + '.webp')
    file_path = os.path.join(output_dir, filename)

    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    Image.fromarray(img).save(file_path, format='WEBP')
    return filename

def delete_output_file(filename: str):
    file_path = os.path.join(output_dir, filename)
    if not os.path.exists(file_path) or not os.path.isfile(file_path):
        return
    try:
        os.remove(file_path)
    except OSError:
        print(f"Delete output file failed: {filename}")


def output_file_to_base64img(filename: str | None) -> str | None:
    if filename is None:
        return None
    file_path = os.path.join(output_dir, filename)
    if not os.path.exists(file_path) or not os.path.isfile(file_path):
        return None

    img = Image.open(file_path)
    output_buffer = BytesIO()
    img.save(output_buffer, format='PNG')
    byte_data = output_buffer.getvalue()
    base64_str = base64.b64encode(byte_data)
    return base64_str


def output_file_to_bytesimg(filename: str | None) -> bytes | None:
    if filename is None:
        return None
    file_path = os.path.join(output_dir, filename)
    if not os.path.exists(file_path) or not os.path.isfile(file_path):
        return None

    img = Image.open(file_path)
    output_buffer = BytesIO()
    img.save(output_buffer, format='PNG')
    byte_data = output_buffer.getvalue()
    return byte_data


def get_file_serve_url(filename: str | None) -> str | None:
    if filename is None:
        return None
    return static_serve_base_url + filename.replace('\\', '/')
