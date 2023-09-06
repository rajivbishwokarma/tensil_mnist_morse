import sys
import subprocess

# Needed to run inference on TCU
import time
import numpy as np
import pynq
import cv2
import glob
import random

from pynq import Overlay
from tcu_pynq.driver import Driver
from tcu_pynq.architecture import ultra96
from pynq.lib import AxiGPIO
from morse_lib import morse_code

# global parameters
overlay = 'tensil_mnist_led.bit'
model = './e14_mnist_20_lr_0_001_onnx_ultra96v2.tmodel'


# DO NOT MODIFY
img_path = "webcam_img.jpg" 


def capture_image():
    # call fswebcam as a shell command
    subprocess.run(["/usr/bin/fswebcam --no-banner --save webcam_img.jpg -d /dev/video0 2> /dev/null"], shell=True)
    return img_path

def tensil_classify(img_path):
    img = cv2.imread(img_path, 0)
    img = cv2.resize(img, (28, 28), interpolation = cv2.INTER_AREA)
    inputs = {}
    inputs.update({"x:0" : img})

    time_start = time.time()
    outputs = tcu.run(inputs)
    time_end = time.time()
    
    classes = outputs['Identity:0'][:10]
    result_idx = np.argmax(classes)
    print(f"[INFO] Result = {result_idx}")
    print(f"[INFO] Inference time: {(time_end - time_start):.4f}s")
    # print(f"[INFO] Class weights: {classes}")
    return result_idx

def display_morse(led, num_list):
    print("[INFO] Morse Code: ", end='')
    for i in range(len(num_list)):
        led[0:8].write(num_list[i])
        if num_list[i] == 240:
            print(".", end='')
        elif num_list[i] == 255:
            print("-", end='')
        time.sleep(1)
        led[0:8].write(0x00)
        time.sleep(1)
    
    # reset at the end
    led[0:8].write(0x00)

if __name__ == '__main__':
    print(f"[INFO] Starting Execution")
    
    # Initial setup: import overlay and assign gpio class
    overlay = Overlay(overlay) 
    led = AxiGPIO(overlay.ip_dict['axi_gpio_0']).channel1
    led[0:8].write(0x00)

    print(f"[INFO] Loading the MNIST model")
    tcu = Driver(ultra96, overlay.axi_dma_0)
    tcu.load_model(model)
    
    print(f"[INFO] Capturing image") 
    # Pipeline: Capture -> Classify -> Output
    img = capture_image()
    
    print(f"[INFO] Classyfing the number")
    num = tensil_classify(img).tolist()
    

    print(f"[INFO] Displaying MOORSE Code")
    morse_dict = morse_code()
    display_morse(led,  morse_dict[num])
    print(f"\n[INFO] Execution Comleted!")

