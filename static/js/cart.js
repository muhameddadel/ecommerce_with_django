let updateBtns = document.getElementsByClassName('update-cart')

for(let i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        let productId = this.dataset.product
        let action = this.dataset.action

        if (user === 'AnonymousUser'){
            console.log('User is not authenticated')
        }else {
            console.log('User is authenticated, sending data...')
        }
    })
}