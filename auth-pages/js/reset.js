document.addEventListener("DOMContentLoaded", () => {
    // Select All Home Buttons Elements
    const btnHome = document.querySelectorAll(".auth-icon-btn");
    
    // Select Reset Page Elements
    const reset = document.getElementById("reset-page");
    const resetForm = document.getElementById("reset-form");
    const newPwd = document.getElementById("new-pwd");
    const confPwd = document.getElementById("conf-pwd");
    const btnReset = document.getElementById("rs-btn");
    

    // RETURN TO LANDING PAGE
    function showHome() {
        window.location = "/SMA-Team-3/landing-pages/landing.html";
        
    };
    // All home button will link to home
    Array.from(btnHome).forEach(function(btnHome) {
        btnHome.addEventListener('click', showHome);
    }); 
   
    
    
    // Reset Form listens for input and calls the checkReset function onclick
    resetForm.addEventListener('input', function(e) {
        btnReset.addEventListener('click', function(e) {
            e.preventDefault();
        });
        btnReset.addEventListener('click', resetPass); 
    }); 

    

    // Checks for input conditions and, if met, calls the showLogin funtion
    function resetPass() {
        if (confPwd.value == newPwd.value && newPwd.value !== '' && confPwd.value !== '') {
            showLogin();
        };
    };  

    // got to login page
    function showLogin() {
        window.location = "login.html";
        
    };
    

    
    
   
});

