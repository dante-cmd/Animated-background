import numpy as np
from sklearn.cluster import KMeans
import cv2
import requests
import time


# METHOD #1: OpenCV, NumPy, and urllib
def url_to_image(url) -> np.ndarray:
	# download the image, convert it to a NumPy array, and then read
	# it into OpenCV format
    resp = requests.get(url)
    
    image = np.asarray(bytearray(resp.content), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    
	# return the image
    return image

def classification_img(image_map:np.ndarray) -> np.ndarray:
    
    # init kmeans
    kmeans = KMeans(n_clusters=10, random_state=0)
    
    # reshape the image to be a list of pixels
    map_array = image_map.reshape(image_map.shape[0]*image_map.shape[1], 3)
    
    # Take a sample of 400 the pixels
    np.random.seed(0)
    idx = np.random.randint(0, len(map_array), size = 400)
    sample_map_array = map_array[idx]

    # fit the model k-means
    kmeans.fit(sample_map_array)

    # predict the cluster for each pixel
    kmeans_labels = kmeans.predict(sample_map_array)
    classes, counts = np.unique(kmeans_labels, return_counts=True)
    colors = list(kmeans.cluster_centers_.astype(int))
    # argsort = np.argsort(counts).astype(int)
    a, b = np.argmin(counts), np.argmax(counts)
    # print(colors[argsort[-2:]])
    return (tuple(colors[a]), tuple(colors[b]))
    # print(tuple(colors[a]), tuple(colors[b]))
    # return colors[argsort]
    # print(colors[argsort])
    # print(colors[argmax])
    # print(counts, classes, colors)

def get_rgb(url):
    image = url_to_image(url)
    return classification_img(image)

if __name__ == "__main__":
    URL = "https://i0.wp.com/imagenesparapeques.com/wp-content/uploads/2021/05/Mario-Bros-png-transparente.png"
    time_start = time.time()
    map_array = url_to_image(URL)
    time_middle = time.time()
    print(time_middle - time_start)
    classification_img(map_array)
    print(time.time()- time_middle)
    
