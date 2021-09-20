/*
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
*/
var csrftoken = $("input[name='csrfmiddlewaretoken']").val();


function makeSelectDropDown(){
    $(".dropdown-item").click(function(event) {
        $(this).parents('.dropdown').find('.dropdown-toggle').html($(event.target).html());
        
        console.log($(this).parents('.dropdown').find('.dropdown-toggle').attr('id'));

        varSelect = $(this).parents('.dropdown').find('.dropdown-toggle').attr('id');
        if(varSelect == 'dropdownMenuLink'){
            $('#dataOfCategory').attr('value',$(this).attr('categoryid'));
        }else if(varSelect == 'cityDropDown'){
            $('#dataOfcity').attr('value',$(event.target).html());
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




$('.cityElementSelect').click(function(){
    //Some code

    $('#dataOfRegion').attr('value','');
    console.log("Okcity");
    city = $(this).attr('city');
    getListOfRegions(city);
});



function getlistOfcities(){

        
            $.ajax({
                type: 'POST',
                url: '/en/getlistOfcities',
                data: { 
                   
                },
                headers:{
                    "X-CSRFToken": csrftoken
                     },
                dataType: 'json',
                cache: false,
                success: function(result) {
                    console.log(result);
                    $('#cityDropDown').html($('#cityDropDown').attr('mainName'));
                    $('#listOfcities').empty();
                   if(result['Result']=='Ok'){
            
                    result.data.forEach(element => {
                        $('#listOfcities').append('<li><a class="dropdown-item cityElementSelect" city="'+element.name+'">'+element.name+'</a></li>');
                    });
                   
            
            
                    makeSelectDropDown();
                   }else{
                    $('#listOfcities').append('<li><a class="dropdown-item cityElementSelect" city=""></a></li>');
                   }

                   
                    $('.cityElementSelect').click(function(){
                        //Some code

                        $('#dataOfRegion').attr('value','');
                        console.log("Ok");
                        city = $(this).attr('city');
                        getListOfRegions(city);
                    });


                },error: function (xhr, ajaxOptions, thrownError) {
                    console.log(thrownError)
                       }
            });
            
                }
            


                function goToSearchPage(language){
                    var category = $("#dataOfCategory").attr('value');
                      var city = $("#dataOfcity").attr('value');
                      var region = $("#dataOfRegion").attr('value');
                    url_Search = '/'+language+'/SearchPage/?category='+category+'&city='+city+'&region='+region;
                
                
                    // console.log(url_Search);
                    window.location.href = url_Search;
                  }

                
                  



                  function addReplaceLangCode( langCode) {
                    url = document.location.href;
                    
                        var a = document.createElement('a');
                        a.href = url; // or document.location.href;
            
                        var paths = a.pathname.split('/');
                        paths.shift();
            
                        if(paths[0].length == 2) {
                            paths[0] = langCode;
                        }else{
                            paths.unshift(langCode);
                        }
                        urlNew =  a.protocol + '//' +
                            a.host + '/' + paths.join('/') + 
                            (a.search != '' ?  a.search : '') + 
                            (a.hash != '' ?  a.hash : '');
            
                            window.location.href = urlNew;
                    }

                    


function getListOfRegions(city){

        
                    $.ajax({
                        type: 'POST',
                        url: '/en/getListOfRegions',
                        data: { 
                            'city': city
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








                        



