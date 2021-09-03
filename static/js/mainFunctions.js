
 function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');



function makeSelectDropDown(){
    $(".dropdown-item").click(function(event) {
        $(this).parents('.dropdown').find('.dropdown-toggle').html($(event.target).html());
        
        console.log($(this).parents('.dropdown').find('.dropdown-toggle').attr('id'));

        varSelect = $(this).parents('.dropdown').find('.dropdown-toggle').attr('id');
        if(varSelect == 'dropdownMenuLink'){
            $('#dataOfCategory').attr('value',$(this).attr('categoryid'));
        }else if(varSelect == 'dropdownMenuLink2'){
            $('#dataOfProvider').attr('value',$(event.target).html());
        }else if(varSelect == 'countryDropDown'){
            $('#dataOfCountry').attr('value',$(event.target).html());
        }else if(varSelect == 'regionDropDown'){
            $('#dataOfRegion').attr('value',$(event.target).html());
        }

    });
}


function showLoader(){
    // $('#loading').fadeIn('fast');
    $('#loading').css({display:'block'});
    // console.log('Showennn');
}

function hideLoader(){
    $('#loading').css({display:'none'});
    // console.log('hide');
}


$('.categoryElementSelect').click(function(){
    //Some code

    console.log("Ok");
    $('#dataOfProvider').attr('value','');
    category = $(this).attr('categoryId');
    getServiceProviders(category);
});



$('.countryElementSelect').click(function(){
    //Some code

    $('#dataOfRegion').attr('value','');
    console.log("OkCountry");
    country = $(this).attr('country');
    getListOfRegions(country);
});


function getServiceProviders(category){

        
    $.ajax({
        type: 'POST',
        url: '/en/getServiceProviders',
        data: { 
            'category': category
        },
        headers:{
            "X-CSRFToken": csrftoken
             },
        dataType: 'json',
        cache: false,
        success: function(result) {
            console.log(result);
            $('#dropdownMenuLink2').html($('#dropdownMenuLink2').attr('mainName'));
            $('#listOfProviders').empty();
           if(result['Result']=='Ok'){
    
            result.data.forEach(element => {
                $('#listOfProviders').append('<li><a class="dropdown-item" provider="'+element.id+'">'+element.name+'</a></li>');
            });
           
    
    
            makeSelectDropDown();
           }else{
            $('#listOfProviders').append('<li><a class="dropdown-item" provider=""></a></li>');
           }
        },error: function (xhr, ajaxOptions, thrownError) {
            console.log(thrownError)
               }
    });
    
        }

        


function getListOfCountries(){

        
            $.ajax({
                type: 'POST',
                url: '/en/getListOfCountries',
                data: { 
                   
                },
                headers:{
                    "X-CSRFToken": csrftoken
                     },
                dataType: 'json',
                cache: false,
                success: function(result) {
                    console.log(result);
                    $('#countryDropDown').html($('#countryDropDown').attr('mainName'));
                    $('#listOfcountries').empty();
                   if(result['Result']=='Ok'){
            
                    result.data.forEach(element => {
                        $('#listOfcountries').append('<li><a class="dropdown-item countryElementSelect" country="'+element.name+'">'+element.name+'</a></li>');
                    });
                   
            
            
                    makeSelectDropDown();
                   }else{
                    $('#listOfcountries').append('<li><a class="dropdown-item countryElementSelect" country=""></a></li>');
                   }

                   
                    $('.countryElementSelect').click(function(){
                        //Some code

                        $('#dataOfRegion').attr('value','');
                        console.log("Ok");
                        country = $(this).attr('country');
                        getListOfRegions(country);
                    });


                },error: function (xhr, ajaxOptions, thrownError) {
                    console.log(thrownError)
                       }
            });
            
                }
            
function getListOfRegions(country){

        
                    $.ajax({
                        type: 'POST',
                        url: '/en/getListOfRegions',
                        data: { 
                            'country': country
                        },
                        headers:{
                            "X-CSRFToken": csrftoken
                             },
                        dataType: 'json',
                        cache: false,
                        success: function(result) {
                            console.log(result);
                            $('#regionDropDown').html($('#regionDropDown').attr('mainName'));
                            $('#listOfregions').empty();
                           if(result['Result']=='Ok'){
                    
                            result.data.forEach(element => {
                                $('#listOfregions').append('<li><a class="dropdown-item" region="'+element.name+'">'+element.name+'</a></li>');
                            });
                           
                    
                    
                            makeSelectDropDown();
                           }else{
                            $('#listOfregions').append('<li><a class="dropdown-item" region=""></a></li>');
                           }
                        },error: function (xhr, ajaxOptions, thrownError) {
                            console.log(thrownError)
                               }
                    });
                    
                        }



