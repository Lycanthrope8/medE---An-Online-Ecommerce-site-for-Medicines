
var cart = JSON.parse(localStorage.getItem('cart')) || {};

function AddtoCart(id, doSomething = null, button = null) {
  if (cart[id] === undefined) { 
    console.log("Added to cart:", id);
    cart[id] = 1;
  } else if (cart[id] !== undefined && doSomething === null) {
    cart[id] += 1;
  } else if (doSomething === "increment") {
    cart[id] += 1;
  } else if (doSomething === "decrement" && cart[id] > 1) {
    cart[id] -= 1;
  }

  // Update the quantity element directly if a button is provided
  if (button) {
    const quantityElement = button.parentElement.querySelector(".quantity-value");
    if (quantityElement) {
      quantityElement.textContent = cart[id];
    }
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

              resultsDiv.append(`
                                <div class="cartbox" id="cartbox-${p_id}">
                                  <button class="cart-trash">
                                    <ion-icon name="trash"></ion-icon>
                                  </button>
                                  <img src="" alt="">
                                  <div class="cart-content">
                                    <h3 id="productName-${p_id}">${productData["p_name"]}</h3>
                                    <div style="display: grid; grid-template-columns: 0.5fr 1fr; gap: 1px;">
                                      <span class="cart-content-price" id="productPrice-${p_id}"></span>
                                      <span class="quantity"> 
                                        Quantity:
                                        <button class="quantity-button decrement" style="display: inline; white-space: nowrap;"
                                          onclick="AddtoCart(${productData["p_id"]}, 'decrement', this)">-</button>
                                        <span class="quantity-value" id="quantity-${p_id}">${cart[productData["p_id"]]}</span>  
                                        <button class="quantity-button increment" style="display: inline; white-space: nowrap;"
                                          onclick="AddtoCart(${productData["p_id"]}, 'increment', this)">+</button>
                                      </span>
                                      <br>
                                      <span class="quantity">Days: 7</span>
                                    </div>
                                  </div>
                                </div>`
                              );

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







    



