function selectPlot() {
    var year = document.getElementById("year").value;
    var images = document.getElementsByClassName("myImage");
    for (var i = 0; i < images.length; i++) {
      if (images[i].id == year) {
        images[i].style.display = "block"
      }else{
        images[i].style.display = "none"
      }
    }
  }