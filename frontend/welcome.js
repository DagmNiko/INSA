const ellipse3 = document.querySelector("#Ellipse3"); 
const user = document.querySelector("#user"); 
const password = document.querySelector("#password"); 
const card = document.querySelector("#card"); 
const rectangle2 = document.querySelector("#Rectangle2"); 


const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        console.log(entry)
        if (entry.isIntersecting) {
            ellipse3.classList.add('Ellipse3Animate');
            user.classList.add('userAnimate');
            password.classList.add('passwordAnimate');
            card.classList.add('cardAnimate');
            rectangle2.classList.add('Rectangle2Animate');
        }else {
            ellipse3.classList.remove('Ellipse3Animate');
            user.classList.remove('userAnimate');
            password.classList.remove('passwordAnimate');
            card.classList.remove('cardAnimate');
            rectangle2.classList.remove('Rectangle2Animate');
        }
    });
});

const hiddenElements = document.querySelectorAll('.hidden');
hiddenElements.forEach((element) => observer.observe(element));


