$(document).ready(function() {
	

  $('.owl-carousel').owlCarousel({
    loop:true,
      margin:10,
      nav:true,
      navText:[
          '<span aria-label="Previous"><i class="fas fa-chevron-circle-left"></i></span>','<span aria-label="Next"><i class="fas fa-chevron-circle-right"></i></span>'
        ],
     responsive:{
         0:{
        items:1,
        nav:false
         },
      600:{
          items:2,
          nav:false
        },
        1000:{
          items:3,
          nav:false
    },
    
    1200:
    {
       items:4
    }
            }
        });

            })
            
            






            $('.loop').owlCarousel({
              center: true,
              items:2,
              loop:true,
              margin:10,
              responsive:{
                  600:{
                      items:4
                  }
              }
          });
          $('.nonloop').owlCarousel({
              center: true,
              items:2,
              loop:false,
              margin:10,
              responsive:{
                  600:{
                      items:4
                  }
              }
          });














            