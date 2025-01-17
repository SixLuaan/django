var updateBtns = document.getElementsByClassName('update-cart')

for (var i =0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productID:', productId, 'action:', action,)
        if(user=== 'AnonymousUser'){
            console.log('not')
        }else{
            updateUserOrder(productId, action)
        }
    })

}
function updateUserOrder(productId, action){
    console.log('sending data')
    var url = '/update_item/'
    fetch(url, {
        method: 'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'productId': productId, 'action': action})
    })
    .then((response)=>{
        return response.json()
    })
    .then((data)=>{
        console.log('data:', data)
        location.reload()
    })
}