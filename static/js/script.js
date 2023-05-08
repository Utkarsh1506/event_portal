let btn = document.querySelector(".menu_btn");
let sidebar = document.querySelector(".sidebar");


btn.onclick= function(){
    sidebar.classList.toggle("active");
}



function toggleTab(tabId) {
    var tab = document.getElementById(tabId);
    var content = document.getElementById("content" + tabId.slice(3));

    tab.classList.toggle("active");
    content.classList.toggle("active");

  }





const divToHide = document.getElementById("d_content");

// add an event listener to the window object
window.addEventListener("click", function(event) {
  // check if the clicked element is inside the div to hide
  if (!divToHide.contains(event.target)) {
    // if clicked outside, hide the div
    divToHide.style.display = "none";
  }
});



// -----------------------dropdown------------------------

function view(){
  if(document.getElementById("d_cont").style.display==="block"){
    document.getElementById("d_cont").style.display="none";
    
  }
  
  else{
    document.getElementById("d_cont").style.display="block";
    
  }
}






  // -----------------------dropdown------------------------



  // JavaScript code to switch images every 5 seconds and loop back to the beginning
  let currentImageIndex = 0;
  const carouselImages = document.querySelectorAll('.carousel-image');
  const numImages = carouselImages.length;
  setInterval(() => {
      carouselImages[currentImageIndex].classList.remove('active');
      currentImageIndex = (currentImageIndex + 1) % numImages;
      carouselImages[currentImageIndex].classList.add('active');
      const transformValue = `translateX(-${currentImageIndex * 100}%)`;
      document.querySelector('.carousel-image-wrapper').style.transform = transformValue;
      // Check if we have reached the end and loop back to the beginning
      if (currentImageIndex === 0) {
          for (let i = 0; i < numImages; i++) {
              carouselImages[i].classList.remove('active');
          }
          carouselImages[0].classList.add('active');
          document.querySelector('.carousel-image-wrapper').style.transform = 'translateX(0)';
          currentImageIndex = 0;
      }
  }, 4000);



