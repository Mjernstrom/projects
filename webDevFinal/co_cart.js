"use strict";

/*
   New Perspectives on HTML5, CSS3, and JavaScript 6th Edition
   Tutorial 13
   Review Assigment

   Shopping Cart Form Script
   
   Author: Matthew Jernstrom
   Date:   
   
   Filename: co_cart.js
   
   Function List
   =============
   
   calcCart()
      Calculates the cost of the customer order
      
   formatNumber(val, decimals)
      Format a numeric value, val, using the local
      numeric format to the number of decimal
      places specified by decimals
      
   formatUSACurrency(val)
      Formats val as U.S.A. currency
   
*/ 

window.addEventListener("load", function(){
   calcCart();
   document.cart.elements.modelQty.onchange = calcCart;
   for (var i = 0; i < document.cart.elements.shipping.length; i++){
     document.cart.elements.shipping[i].addEventListener('click', calcCart);
   }
 });
 
 function calcCart() {
   var orderCost = document.cart.elements.modelCost.value * document.cart.elements.modelQty.value;
   document.cart.elements.orderCost.value = formatUSCurrency(orderCost, 2);
   var shipCost = document.cart.elements.shipping.value * document.cart.elements.modelQty.value;
   document.cart.elements.shippingCost.value = formatNumber(shipCost, 2)
   document.cart.elements.subTotal.value = formatNumber((shipCost + orderCost), 2);
   var salesTax = 0.05*(orderCost + shipCost);
   document.cart.elements.salesTax.value = formatNumber(salesTax, 2);
   document.cart.elements.cartTotal.value = formatUSCurrency((orderCost + shipCost + salesTax));
   document.cart.elements.shippingType.value = document.querySelector('input[name="shipping"]:checked').value;
 }

function formatNumber(val, decimals) {
   return val.toLocaleString(undefined, {minimumFractionDigits: decimals, 
                                         maximumFractionDigits: decimals});
}

function formatUSCurrency(val) {
   return val.toLocaleString('en-US', {style: "currency", currency: "USD"} );
}
