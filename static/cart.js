



function AddtoCart(id,quantity=1, doSomething = null, button = null) {
  var cart = JSON.parse(localStorage.getItem('cart')) || {};
  if (cart[id] === undefined) { 
    console.log("Added to cart:", id);
    cart[id] = quantity;
  } else if (cart[id] !== undefined && doSomething === null) {
    cart[id] += 1;
  } else if (doSomething === "increment") {
    cart[id] += 1;
  } else if (doSomething === "decrement" && cart[id] > 1) {
    cart[id] -= 1;
  } else if (doSomething === "replace"){
    cart[id] = quantity;
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

    // Clear the existing content
    resultsDiv.empty();

    // Get the sorted array of product IDs
    var sortedProductIds = Object.keys(cart).sort(function(a, b) {
        return a - b;
    });
    console.log(sortedProductIds)
    // Loop through the sorted product IDs and create fetch requests
    for (const p_id of sortedProductIds) {
        try {
            // Fetch the product information for the current p_id
            const response = await fetch(`/get_product_info/${p_id}/`);
            if (response.ok) {
                const productData = await response.json();
                console.log("Product Data:", productData);
                var productPrice = productData.p_price - (productData.p_price * (productData.p_discount / 100));

                if (Object.keys(productData).length > 0 && "p_name" in productData) {
                    // Display the product name
                    resultsDiv.append(`
                        <div class="cartbox" id="cartbox-${p_id}">
                            <button class="cart-trash" onclick="removeFromCart(${productData["p_id"]})">
                                <ion-icon name="trash"></ion-icon>
                            </button>
                            <img src="" alt="">
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
                        </div>`
                    );
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
});





    



