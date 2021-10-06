document.addEventListener("DOMContentLoaded", () => {
    // Select All Home Buttons Elements
    const btnHome = document.querySelectorAll(".auth-icon-btn");
    
    // Select Login page button element
    const lgForm = document.getElementById("login-form");
    const logEmail = document.getElementById("user-email");
    const curPwd = document.getElementById("current-password");
    const btnLogin = document.getElementById("login-btn");
    const btnLogReg = document.getElementById("log-reg");
    const btnLogFor = document.getElementById("log-forgot");


    function showHome() {
        window.location = "/SMA-Team-3/landing-pages/landing.html";
        
    };

    // All home button will link to home
    Array.from(btnHome).forEach(function(btnHome) {
        btnHome.addEventListener('click', showHome);
    }); 

    // Link to registration page
    function showRegistration() {
        window.location = "registration.html"; 
        lgForm.reset(); 
    };

    // Check login form inputs
    lgForm.addEventListener('input', function(e) {
        btnLogin.addEventListener('click', function(e) {
            e.preventDefault();
        }); 
        btnLogin.addEventListener('click', checkLogin)
    }); 

    // are login form inputs empty  NOTE: goes to homepage bc profile page is not made
    function checkLogin() {
        if(curPwd.value !== "" && logEmail.value !== "") {
            showHome();
        } else {
            btnLogin.style.backgroundColor = "#53B6E0";
        };
    };
    
    // Login page registration link
    btnLogReg.addEventListener('click', function(e) {
        e.preventDefault();
    });
    btnLogReg.addEventListener('click', showRegistration);
   
    // Login page link to forgot password
    function showForgot() {
        window.location = "forgot.html"; 
        lgForm.reset(); 
    };
    btnLogFor.addEventListener('click', function(e) {
        e.preventDefault();
    });
    btnLogFor.addEventListener('click', showForgot);

   

   
});

