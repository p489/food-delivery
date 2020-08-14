var UpdateBtns = document.getElementsByClassName('update-cart')
console.log(UpdateBtns.length)
 for (var i=0;i<UpdateBtns.length;i++)
 {
     UpdateBtns[i].addEventListener('click',function(){
         var productId = this.dataset.product
         var action = this.dataset.action
         console.log(productId, action)

         console.log('USER:', user)
         if(user == 'AnonymousUser'){
             console.log('User not authenticated')
         }else{
            updateUserOrder(productId, action)
         }
     })
 }
 function updateUserOrder(productId, action){
    console.log('User is authenticated')
    var url = '/home/update_item/'
    fetch(url, {
        method: 'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'productId':productId, 'action':action})

    })
    .then((response) =>{
        return response.json();
     

    })
     .then((data) => {
         location.reload();
         

     });
 }