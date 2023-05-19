$('.remove-button').click(function (e) { 
    e.preventDefault();
    console.log('added')
    let product_id= $(this).closest('.product_data').find('.prod_id').val();
    let token=$('input[name=csrfmiddlewaretoken]').val();
    $.ajax({
        type: "POST",
        url: "delete-item",
        data: {
            'product_id':product_id,
            csrfmiddlewaretoken:token
        },
        
        success: function (response) {
            
        }
    });
    
});
