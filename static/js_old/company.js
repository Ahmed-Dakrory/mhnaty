

            function openModal() {
                document.getElementById("myModal").style.display = "block";
              }
              
              // Close the Modal
              function closeModal() {
                document.getElementById("myModal").style.display = "none";
              }
              
              
              
              // Next/previous controls
              function plusSlides(n) {
                showSlides(slideIndex += n);
              }
              
              // Thumbnail image controls
              function currentSlide(n) {
                showSlides(slideIndex = n);
              }
              
              function showSlides(n) {
                var i;
                var slides = document.getElementsByClassName("mySlides");
                var dots = document.getElementsByClassName("demo");
                var captionText = document.getElementById("caption");
                if (n > slides.length) {slideIndex = 1}
                if (n < 1) {slideIndex = slides.length}
                for (i = 0; i < slides.length; i++) {
                  slides[i].style.display = "none";
                }
                for (i = 0; i < dots.length; i++) {
                  dots[i].className = dots[i].className.replace(" active", "");
                }
                slides[slideIndex-1].style.display = "block";
                dots[slideIndex-1].className += " active";
                captionText.innerHTML = dots[slideIndex-1].alt;
              }
  
  
              
$('.column2 img').click(function(){
  //Some code

  numberOfImage = $(this).attr('numberOfImage');
  srcOfImage = $(this).attr('src');
  
  console.log(numberOfImage);

  $('#mainImage').attr('numberOfImage',numberOfImage);
  $('#mainImage').attr('src',srcOfImage);
  // openModal();
  // currentSlide(numberOfImage);
});


$('#mainImage').click(function(){
  //Some code

  numberOfImage = $(this).attr('numberOfImage');
  srcOfImage = $(this).attr('src');
  
  openModal();
  currentSlide(numberOfImage);
});
