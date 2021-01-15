# Opencv-Super-Resolution

This project is about utilizing four pre-trained super resolution models which are listed below to  perform super resolution with OpenCV in images

1. EDSR_x4.pb: Model from the Enhanced Deep Residual Networks for Single Image Super-Resolution paper — increases the input image resolution by 4x

2. ESPCN_x4.pb: Super resolution model from Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network — increases resolution by 4x

3. FSRCNN_x3.pb: Model from Accelerating the Super-Resolution Convolutional Neural Network — increases image resolution by 3x

4. LapSRN_x8.pb: Super resolution model from Fast and Accurate Image Super-Resolution with Deep Laplacian Pyramid Networks — increases image resolution by 8x

To run this in command line:

--model: The path to the input OpenCV super resolution model

--image: The path to the input image that we want to apply super resolution to

Example:python super_res_image.py --model models/EDSR_x4.pb --image examples/adrian.png

More details about the Opencv libraries and explanation about the project are in the pdf file.

