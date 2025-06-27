function changeImage() {
    const imgElement = document.getElementById('loadedImage');
    if (imgElement.src.includes("cat1.jpg")) {
        imgElement.src = "/static/images/cat2.jpg"; // switch to cat2
    } else {
        imgElement.src = "/static/images/cat1.jpg"; // switch back to cat1
    }
}
