function AddtoCart(id, quantity = 1, doSomething = null, button = null) {
  var cart = JSON.parse(localStorage.getItem('cart')) || {};

  // Assuming you make an API call to get the product data using the product ID
  fetch(`/get_product_info/${id}`)
    .then(response => response.json())
    .then(productData => {
      if (cart[id] === undefined) {
        console.log("Added to cart:", id);
        // Multiply the quantity by 'medPerStrip' from the API response
        cart[id] = parseInt(quantity * productData.medPerStrip);
      } else if (cart[id] !== undefined && doSomething === null) {
        cart[id] += quantity * productData.medPerStrip;
      } else if (doSomething === "increment") {
        cart[id] += 1;
      } else if (doSomething === "decrement" && cart[id] > 1) {
        cart[id] -= 1;
      } else if (doSomething === "replace") {
        cart[id] = parseInt(quantity * productData.medPerStrip);
      }

      // Update the quantity element directly if a button is provided
      if (button) {
        const quantityElement = button.parentElement.querySelector(".quantity-value");
        if (quantityElement) {
          quantityElement.textContent = cart[id];
        }
      }

      // Update the total price for this item in the cart
      const totalPriceElement = document.getElementById(`totalPrice-${id}`);
      if (totalPriceElement) {
        totalPriceElement.textContent = `${cart[id] * productData['p_price']} Taka`;
      }

      // Recalculate and update the total value for all items in the cart
      var totalValue = Object.keys(cart).reduce((acc, productId) => {
        const product = cart[productId];
        return acc + product * productData['p_price'];
      }, 0);

      // Display total value for all items in the cart
      const totalElement = document.querySelector('.total');
      if (totalElement) {
        totalElement.textContent = `Total: ৳${totalValue.toFixed(2)}`;
      }

      console.log(cart);
      localStorage.setItem('cart', JSON.stringify(cart));
    })
    .catch(error => {
      console.error('Error:', error);
    });
}




function removeFromCart(id) {
  
  let cart = JSON.parse(localStorage.getItem('cart')) || {};

  // Check if the item exists in the cart
  if (cart.hasOwnProperty(id)) {
    console.log('Removing Item: ', id);
    delete cart[id];
    localStorage.setItem('cart', JSON.stringify(cart));
  } else {
    console.log('Item not found in cart:', id);
  }
  // Hide the corresponding cartbox div
  let cartboxId = `cartbox-${id}`;
  let cartboxElement = document.getElementById(cartboxId);
  if (cartboxElement) {
    cartboxElement.style.display = 'none';
  }
}



function ClearCart() {
    console.log('clearing cart');
    localStorage.removeItem('cart');
    cart = {}
    console.log(cart)
  }


document.getElementById("cart-btn").addEventListener("click", async function() {
  var cart = JSON.parse(localStorage.getItem('cart'));
  var resultsDiv = $('#cart-container');
  var totalValue = 0; // Initialize total value to 0

  // Clear the existing content
  resultsDiv.empty();

  // Get the sorted array of product IDs
  var sortedProductIds = Object.keys(cart).sort(function(a, b) {
      return a - b;
  });

  // Loop through the sorted product IDs and create fetch requests
  for (const p_id of sortedProductIds) {
      try {
          // Fetch the product information for the current p_id
          const response = await fetch(`/get_product_info/${p_id}/`);
          if (response.ok) {
              const productData = await response.json();
              console.log("Product Data:", productData);
              var productPrice = parseFloat(productData.discounted_price).toFixed(2);
              
              if (Object.keys(productData).length > 0 && "p_name" in productData) {
                  // Display the product name
                  resultsDiv.append(`
                  <div class="cartbox" id="cartbox-${p_id}">
                            <button class="cart-trash" onclick="removeFromCart(${productData["p_id"]})">
                                <ion-icon name="trash"></ion-icon>
                            </button>
                            <img src="../../media/${productData["p_image"]}" alt="">
                            <div class="cart-content-${p_id}">
                                <h3 id="productName-${p_id}">${productData["p_name"]}</h3>
                                <div style="display: grid; grid-template-columns: 0.5fr 1fr; gap: 1px;">
                                <span class="cart-content-price" id="productPrice-${p_id}">${productPrice}</span>
                                    <span class="quantity"> 
                                        Quantity:
                                        <button class="quantity-button decrement" style="display: inline; white-space: nowrap;"
                                            onclick="AddtoCart(${productData["p_id"]},${cart[productData["p_id"]]}, 'decrement', this)">-</button>
                                        <span class="quantity-value" id="quantity-${p_id}">${cart[productData["p_id"]]}</span>  
                                        <button class="quantity-button increment" style="display: inline; white-space: nowrap;"
                                            onclick="AddtoCart(${productData["p_id"]},${cart[productData["p_id"]]}, 'increment', this)">+</button>
                                    </span>
                                </div>
                            </div>
                          <h6 id="totalPrice-${p_id}">${cart[productData["p_id"]] * productData['p_price']} Taka</h3>
                        </div>`
                  );

                  // Update total value
                  totalValue += cart[productData["p_id"]] * productData['p_price'];
              } else {
                  resultsDiv.append('<p>No product name found.</p>');
              }
          } else {
              resultsDiv.append('<p>No results found.</p>');
          }
      } catch (error) {
          console.error('Error:', error);
      }
  }

  // Display total value for all items in the cart
  if(cart!={}){
    resultsDiv.append(`<div class="total">Total: ৳${totalValue.toFixed(2)}</div>`);
  }
});



    



