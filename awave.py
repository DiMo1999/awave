import argparse
import numpy as np
import scipy.io.wavfile as wavfile
import cv2 as cv

CHUNK_SIZE = 10**4  

def process_waveform(input_path, zoom_factor, start_second):
    print("Reading the WAV file...")
    rate, waveform = wavfile.read(input_path)

    start = int(rate * start_second)
    end = start + int((rate * 10) / zoom_factor)

    zoomed_waveform = waveform[start:end]

    zoomed_waveform = zoomed_waveform if zoomed_waveform.ndim == 1 else zoomed_waveform[:, 0]

    if zoomed_waveform.size == 0:
        print('The zoomed waveform is empty. Please check the start_second or zoom_factor.')
        return

    print("Computing the scaling factor...")
    max_value = np.max(np.abs(zoomed_waveform))
    waveform_chunks = np.array_split(zoomed_waveform, range(0, len(zoomed_waveform), CHUNK_SIZE))

    results = []
    for waveform_chunk in waveform_chunks:
        if waveform_chunk.size == 0:
            continue
        normalised_waveform_chunk = waveform_chunk.astype(np.float32) / max_value
        theta = np.linspace(0, 2.*np.pi, len(waveform_chunk), endpoint=False)
        radius = 1.2 + 0.6 * normalised_waveform_chunk

        x = radius * np.cos(theta)
        y = radius * np.sin(theta)
        
        abs_values = np.abs(np.hstack((x, y)))
        scaling_factor = 500 / np.max(abs_values)
        
        output_chunk = (x, y)
        results.append(output_chunk)

    # Cambia la dimensione dell'output 1000x1000
    output = np.ones((2000, 2000, 3), dtype=np.uint8) * 255
    
    # Calcola il fattore di scala in modo che l'onda spezzata si adatti alla dimensione dell'output
    scaling_factor = min(output.shape[0], output.shape[1]) / np.max(np.abs(np.hstack((x, y)))) / 2 * 0.8

    print("Drawing waveform...")
    for output_chunk in results:
        x, y = output_chunk
        # Centra l'onda spezzata nell'output aggiungendo metà della dimensione dell'output alle coordinate x e y
        x = np.array(x * scaling_factor + output.shape[1] / 2, dtype=np.int32)
        y = np.array(y * scaling_factor + output.shape[0] / 2, dtype=np.int32)
    """
        for i in range(1, len(x)):
            cv.line(output, (x[i-1], y[i-1]), (x[i], y[i]), (0,0,0), 2)
    """
    for i in range(1, len(x)):
        poly_points = np.array([[(x[i-1], y[i-1]), (x[i], y[i])]], dtype=np.int32)
        cv.polylines(output, poly_points, isClosed=False, color=(0,0,0), thickness=2)    
            
    output_name = input_path.rsplit('.', 1)[0] + '.png'

    print("Saving the image...")
    cv.imwrite(output_name, output)

    print(f'Output image saved as {output_name}')


def main():
    print("start")
    #parser = argparse.ArgumentParser()
    #parser.add_argument('-i', '--input', required=True, help='Path to input wav file.')
    #parser.add_argument('-z', '--zoom', type=float, default=2.0, help='Zoom factor.')
    #parser.add_argument('-s', '--start', type=float, default=10, help='Start Second for zooming.')
    #args = parser.parse_args()

    #process_waveform(args.input, args.zoom, args.start)

if __name__ == '__main__':
    main()
