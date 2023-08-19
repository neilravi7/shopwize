const cartTotal = document.querySelector('#cartTotal');
var summarySection = document.querySelector('#summarySection');

observer = new MutationObserver(function(mutationsList, observer) {
    summarySection.innerHTML = ''
    cartValue = parseFloat(cartTotal.innerText.replace('$', ''));
    if (cartValue != 0){
        summarySection.innerHTML = `<a href="{% url 'cart:checkout' %}" class="btn btn-lg btn-primary ms-auto">
        Checkout</a>`

    }else
    {
        summarySection.innerHTML = `<button id="checkoutButton" class="btn btn-lg btn-primary ms-auto" disabled>
        Checkout</button>`
    }
});

observer.observe(cartTotal, {characterData: false, childList: true, attributes: false});