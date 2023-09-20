
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



  document.getElementById("cart-btn").addEventListener("click", function() {
    var cart = JSON.parse(localStorage.getItem('cart'));
    var resultsDiv = $('#cart-container');
    
    // Clear the existing content
    resultsDiv.empty();
  
    for (var p_id in cart) {
      p_id = parseInt(p_id);
  
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
          var productPrice = productData.p_price - (productData.p_price * (productData.p_discount / 100));
          // 
          // Check if productData is not empty
          if (Object.keys(productData).length > 0) {
            if ("p_name" in productData) {
              // Display the product name
              resultsDiv.append('<li style="display: inline; white-space: nowrap;">Name: ' + productData["p_name"] + '  Quantity: <button class="quantity-button" style="display: inline; white-space: nowrap;">-</button> ' + cart[productData["p_id"]] + ' <button class="quantity-button" style="display: inline; white-space: nowrap;">+</button></li>');
           } else {
              resultsDiv.append('<p>No product name found.</p>');
            }
          } else {
            resultsDiv.append('<p>No results found.</p>');
          }
        })
        .catch(error => {
          console.error('Error:', error);
        });
    }
  });
  




    



