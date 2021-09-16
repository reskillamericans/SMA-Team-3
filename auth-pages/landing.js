document.addEventListener("DOMContentLoaded", () => {
    // DOM ELEMENTS

    const landing = document.getElementById("lp-main");
    const features = document.getElementById("lp-features-window");
    const btnNext = document.getElementById("btn-next");

    features.style.display = "none";


    
    function showFeatures() {
        window.location = "about.html"
        
    }

    btnNext.addEventListener('click', function(e) {
        e.preventDefault();           
    }); 
    btnNext.addEventListener('click', showFeatures);

});