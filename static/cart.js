
var cart = JSON.parse(localStorage.getItem('cart')) || {};

function AddtoCart(id) {
  console.log("Added to cart:", id);

  if (cart[id] === undefined) { 
    cart[id] = 1;
  } else { // If it's already in the cart, increment the quantity
    cart[id] += 1;
  }

  console.log(cart);
  localStorage.setItem('cart', JSON.stringify(cart));
}

function ClearCart() {
    console.log('clearing cart')
    localStorage.removeItem('cart');
    cart = {}
    console.log(cart)
  }


// When clicking the cart button
document.getElementById("cart-btn").addEventListener("click", function() {
  var cart = JSON.parse(localStorage.getItem('cart'));

  for (var p_id in cart) {
      p_id = parseInt(p_id);
      console.log("Product ID:", p_id);
      console.log("Quantity:", cart[p_id]);

      // Fetch the product information for the current p_id
      fetch(`get_product_info/${p_id}/`)
          .then(response => {
              if (response.ok) {
                  return response.json();
              }
              throw new Error('Network response was not ok.');
          })
          .then(productData => {
              console.log("Product Data:", productData);

              // Find the HTML elements to update based on the product ID
              var productNameElement = document.getElementById(`productName`);    //productName-${p_id}
              var productPriceElement = document.getElementById(`productPrice`);  //productPrice-${p_id}

              var productPrice = productData.p_price - (productData.p_price * (productData.p_discount / 100))
              console.log(productData.p_name);
              console.log(productPrice);

              
              // Update the HTML elements with the product information
              if (productNameElement && productPriceElement) {
                
                productNameElement.innerHTML = productData.p_name
                productPriceElement.innerHTML = productPrice
                  // Add similar code for other elements as needed
              }
          })
          .catch(error => {
              console.error('Error:', error);
          });
  }
});








