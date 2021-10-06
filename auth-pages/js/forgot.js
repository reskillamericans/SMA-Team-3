document.addEventListener("DOMContentLoaded", () => {
    // Select All Home Buttons Elements
    const btnHome = document.querySelectorAll(".auth-icon-btn");
    
    // Select Forgot Page Elements
    const forgot = document.getElementById("forgot-page");
    const forgotForm = document.getElementById("forgot-form");
    const oldEmail = document.getElementById("old_email");
    const btnVerify = document.getElementById("fg-btn");

    // Select Verify PopUp Elements
    const verified = document.getElementById("verify-popup");
    const btnCont = document.getElementById("verified-btn");


    // RETURN TO LANDING PAGE
    function showHome() {
        window.location = "/SMA-Team-3/landing-pages/landing.html";
        
    };
    // All home button will link to home
    Array.from(btnHome).forEach(function(btnHome) {
        btnHome.addEventListener('click', showHome);
    }); 
   
    // Function to reveal verified popup
    function showVerified() {
        forgot.style.display = "none";
        verified.style.display = "block";   
    }

    // If Forgot page is displayed, call the checkForgotEmail Function 
    function ForgotPass() {
        if(forgot.style.display ="block") {
            checkForgotEmail();
        };
    };
    // If conditions are met, reveal the verified popup
    function checkForgotEmail() {
        if (oldEmail.validity.valid && oldEmail.value !== '') {
            showVerified();
        };
    }; 
    
    // Forgot form listens for input and then calls the Forgot Pass function onclick
    forgotForm.addEventListener('input', function(e) {
        btnVerify.addEventListener('click', function(e) {
            e.preventDefault();
        });
        btnVerify.addEventListener('click', ForgotPass); 
    });  
    
    // VERIFIED POPUP - BTN TO RESET PASSWORD
    function showReset() {
        window.location = "reset.html";
        
    };
    btnCont.addEventListener('click', function(e) {
        e.preventDefault();
    });
    btnCont.addEventListener('click', showReset);
   
});

