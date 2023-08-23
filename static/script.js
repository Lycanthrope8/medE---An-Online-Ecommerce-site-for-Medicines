'use strict';



const mobileMenuOpenBtn = document.querySelectorAll('[data-mobile-menu-open-btn]');
const mobileMenu = document.querySelectorAll('[data-mobile-menu]');
const mobileMenuCloseBtn = document.querySelectorAll('[data-mobile-menu-close-btn]');

for (let i=0; i < mobileMenuOpenBtn.length; i++) {
    const mobileMenuCloseFunc = function () {
        mobileMenu[i].classList.remove('active');
    }
    mobileMenuOpenBtn[i].addEventListener('click', function () {
        mobileMenu[i].classList.add('active');
    });

    mobileMenuCloseBtn[i].addEventListener('click', mobileMenuCloseFunc);
}

// ACCORDION MENU

const accordionBtn = document.querySelectorAll('[data-accordion-btn]');
const accordion = document.querySelectorAll('[data-accordion]');

for (let i = 0; i < accordionBtn.length; i++) {

    accordionBtn[i].addEventListener('click', function () {

        const clickedBtn = this.nextElementSibling.classList.contains('active');

        for (let i = 0; i < accordion.length; i++) {
            if (clickedBtn) break;

            if (accordion[i].classList.contains('active')) {
                
                accordion[i].classList.remove('active');
                accordionBtn[i].classList.remove('active');
            }
        }
        this.nextElementSibling.classList.toggle('active');
        this.classList.toggle('active');
    });
}

// BACK TO TOP BUTTON
// const addEventOnElem = function (elem, type, callback) {
//     if (elem.length > 1) {}
// }
// const backTopBtn = document.querySelector("[data-back-top-btn]");

// const activeElemOnScroll = function () {
//     if (window.scrollY > 100) {
//         backTopBtn.classList.add("active");
//     } else {
//         backTopBtn.classList.remove("active");
//     }
// }
// addEventOnElem(window, "scroll", activeElemOnScroll);

const mybutton = document.querySelector("[data-back-top-btn]");
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (window.scrollY > 100) {
    mybutton.classList.add('active');
  } else {
    mybutton.classList.remove('active');
  }
}

// AUTO BANNER CAROUSEL

// var img = document.getElementById('slider-item');
// var slides = ['assets/images/banner-2.jpg','assets/images/banner-3.jpg','assets/images/banner-1.jpg'];
// var Start=0;
// function slider(){
//     if(Start<slides.length){
//         Start=Start+1;
//     }
//     else{
//         Start=1;
//     }
//     console.log(img);
//     img.innerHTML = "<img src="+slides[Start-1]+">";
   
// }
// setInterval(slider,2000);


let shoppingCart = document.querySelector('.shopping-cart');

document.querySelector('#cart-btn').onclick = () =>{
    shoppingCart.classList.toggle('active');
    loginForm.classList.remove('active');
}

let loginForm = document.querySelector('.user-login');

document.querySelector('#user-login-btn').onclick = () =>{
    loginForm.classList.toggle('active');
    shoppingCart.classList.remove('active');
}