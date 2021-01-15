# USAGE
# python super_res_image.py --model models/LapSRN_x8.pb --image examples/zebra.png

# import the necessary packages
import argparse
import time
import cv2
import os


ap = argparse.ArgumentParser()
ap.add_argument("-m","--model",required=True,help="path to super resolution model")
ap.add_argument("-i", "--image", required = True, help= "path to the image we want to increase resolution")
args = vars(ap.parse_args())


# extract the model anme and model scale from file path

modelName = args["model"].split(os.path.sep)[-1].split("_")[0].lower()
modelScale = args["model"].split("_x")[-1]
modelScale = int(modelScale[:modelScale.find(".")])

# initialize OpenCV's super resolution DNN object, load the super
# resolution model from disk, and set the model name and scale

print("INFO: loading super resolution model: {}".format(args["model"]))
print ("INFO : model name {}".format(modelName))
print ("INFO : model scale {}".format(modelScale))
sr = cv2.dnn_superres.DnnSuperResImpl_create()
sr.readModel(args["model"])
sr.setModel(modelName,modelScale)

#load the input image from disk and siplay its spatial dimensions
image = cv2.imread(args["image"])
print("Info : w: {},h:{}".format(image.shape[1],image.shape[0]))

#use the super resolution model to upscale the image , timing how long it takes
start= time.time()
upscaled = sr.upsample(image)
end = time.time()
print("INFO: super resolution took {:.6f} seconds".format(end-start))

#show the spatial dimensions of the super resolution image
print("INFO : w:{},h:{}".format(upscaled.shape[1],upscaled.shape[0]))

start = time.time()
bicubic = cv2.resize(image,(upscaled.shape[1], upscaled.shape[0]), interpolation = cv2.INTER_CUBIC)

end = time.time()
print("[INFO] bicubic interpolation took {:.6f} seconds".format(
	end - start))

cv2.imshow("original", image)
cv2.imshow("Bicubic", bicubic)
cv2.imshow("Super Resolution" , upscaled)
cv2.waitKey(0)












