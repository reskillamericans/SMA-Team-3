document.addEventListener("DOMContentLoaded", () => {
    // DOM ELEMENTS
    const btnNext = document.getElementById("btn-next");

    // function to open about/features page 
    function showFeatures() {
        window.location = "about.html"  
    }

    // Button opens about/features page 
    btnNext.addEventListener('click', function(e) {
        e.preventDefault();           
    }); 
    btnNext.addEventListener('click', showFeatures);

});