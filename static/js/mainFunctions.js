

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





function showLoader(){
    // $('#loading').fadeIn('fast');
    $('#loading').css({display:'block'});
    // console.log('Showennn');
}

function hideLoader(){
    $('#loading').css({display:'none'});
    // console.log('hide');
}




$('select#listOfcities.selectpicker.default').on('changed.bs.select', function (e, clickedIndex, isSelected, previousValue) {
                      
    $('#dataOfRegion').attr('value','');
    console.log("Okcity");
    city = $('#listOfcities').val();
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
                    $('#listOfcities').empty();
                   if(result['Result']=='Ok'){
            
                    result.data.forEach(element => {
                        $('#listOfcities').append('<option value="'+element.name+'">'+element.name+'</option>');
                    });
                   
            
                   }else{
                    $('#listOfcities').append('<option value="All">All</option>');
                   }

                   $('select').selectpicker('refresh');
                    
                    $('select#listOfcities.selectpicker.default').on('changed.bs.select', function (e, clickedIndex, isSelected, previousValue) {
                        //Some code

                        console.log("Ok");
                        
                        city = $('#listOfcities').val();
                        getListOfRegions(city);
                    });


                },error: function (xhr, ajaxOptions, thrownError) {
                    console.log(thrownError)
                       }
            });
            
                }
            


                function goToSearchPage(language){
                    var category = $("#dropdownMenuLink").val();
                      var city = $("#listOfcities").val();
                      var region = $("#listOfregions").val();
                    url_Search = '/'+language+'/SearchPage/?category='+category+'&city='+city+'&region='+region;
                
                
                    console.log(url_Search);
                    // window.location.href = url_Search;
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
                            'city':  "'"+city+"'"
                        },
                        headers:{
                            "X-CSRFToken": csrftoken
                             },
                        dataType: 'json',
                        cache: false,
                        success: function(result) {
                            console.log(result);
                            $('#listOfregions').empty();
                           if(result['Result']=='Ok'){
                    
                            result.data.forEach(element => {
                                $('#listOfregions').append('<option value="'+element.name+'">'+element.name+'</option>');
                            });
                           
                    
                    
                           }else{
                            $('#listOfregions').append('<option value="All">All</option>');
                           }

                           
                   $('select').selectpicker('refresh');
                        },error: function (xhr, ajaxOptions, thrownError) {
                            console.log(thrownError)
                               }
                    });
                    
                        }








                        





                        $( function() { 
                            $( "#searchInputMhnaty" ).autocomplete({
                                source: function( request, response ) {
                                $.ajax( {
                                    type: 'POST',
                                    url: "/en/getAllAdsByCategoriesJson",
                                    dataType: "json",
                                    headers:{
                                        "X-CSRFToken": csrftoken
                                         },
                                    data: {
                                    'category': request.term
                                    },
                                    success: function( data ) {
                                    response( $.map(data.data,function(item){
                                        console.log(data);
                                        return {
                                            id: item.id,
                                            value:item.name
                                        }
                                    }));
                                    }
                                } );
                                },
                                minLength: 1,
                                select: function( event, ui ) {
                                    LANGUAGE_CODE = $('#LANGUAGE_CODE').val();
                                window.location = "/"+LANGUAGE_CODE+"/CompanyPage/?id="+ ui.item.id; 
                    
                    
                                }
                            } );
                            } );
                


