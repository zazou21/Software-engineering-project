if(document.readyState=="loading"){         //avoiding load delay
    document.addEventListener('DOMContentLoaded',ready)
}else{
    ready()
}
function ready(){
    let CartAlertButtons=document.getElementsByClassName('btn btn-primary')
    for(let i=0;i<CartAlertButtons.length;i++){
        let CartAlertBtn=CartAlertButtons[i];
        CartAlertBtn.addEventListener('click',function(){
            alert('This item has been added to your cart')
        })

    }
let removeCartButton =document.getElementsByClassName('btn-danger')
for(let i=0;i<removeCartButton.length;i++){
    let removeAction=removeCartButton[i];
    removeAction.addEventListener('click',removeItem)}
    let quantityArray=document.getElementsByClassName('cart-quantity-input');
    for(let i=0;i<quantityArray.length;i++){
        let input=quantityArray[i]
        input.addEventListener('change',changeQuantity)
    }
    let addToCart=document.getElementsByClassName('shop-item-button')
    for(let i=0;i<addToCart.length;i++){
        let addItem=addToCart[i]
        addItemButton.addEventListener('click',shopItem)
    }
}
function shopItem(event){
    let button=event.target
    let shop=button.parentElement.parentElement
    let title=shop.getElementsByClassName('shop-item-title')[0].innerText;
    let price=shop.getElementsByClassName('shop-item-price')[0].innerText;
    let image=shop.getElementsByClassName('shop-item-image')[0].src;
    addItemCart();
    updateTotal()



}
 function addItemCart(title,price,src){
    let cartRow=document.createElement('div')

    cartRow.classList.add('cart-row')
    let cartItems=document.getElementsByClassName('cart-items')[0]
    cartNames=cartItems.getElementsByClassName('cart-items-title')
    for(let i=0;i<cartNames.length;i++){
        if(cartNames[i].innerText==title){
            alert('Item already in cart!')
            return
        }
    }
    let cartRowContents=`
    <div class="cart-item cart-column">
        <img class="cart-item-image" src="${imageSrc}" width="100" height="100">
        <span class="cart-item-title">${title}</span>
    </div>
    <span class="cart-price cart-column">${price}</span>
    <div class="cart-quantidty cart-column">
        <input class="cart-quantity-input" type="number" value="1">
        <button class="btn btn-danger" type="button">REMOVE</button>
    </div>`
    cartRow.innerHTML=cartRowContents
    cartItems.append(cartRow)


}
function removeItem(event){
    let clicked=event.target;
        clicked.parentElement.parentElement.remove();
        updateTotal();
        
}
function changeQuantity(event){
    let input=event.target
    if(isNaN(input.value)||input.value<=0){
        input.value=1
    }
    updateTotal()
}
function updateTotal(){    //for changing price total
    let cartItemContainer = document.getElementsByClassName('cart-items')[0]
    let cartRows = cartItemContainer.getElementsByClassName('cart-row')
    let total = 0
    for (var i = 0; i < cartRows.length; i++) {
        let cartRow = cartRows[i]
        let priceElement = cartRow.getElementsByClassName('cart-price')[0]
        let quantityElement = cartRow.getElementsByClassName('cart-quantity-input')[0]
        let price = parseFloat(priceElement.innerText.replace('$', ''))
        let quantity = quantityElement.value
        total = total + (price * quantity)
    }
    total = Math.round(total * 100) / 100
    document.getElementsByClassName('cart-total-price')[0].innerText = '$' + total
        


    }
    
