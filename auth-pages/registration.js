document.addEventListener("DOMContentLoaded", () => {
    // Select All Home Buttons Elements
    const btnHome = document.querySelectorAll(".auth-icon-btn");
    const required = document.querySelectorAll("input[required]");
    
   

    // Select Elements From Registration page 
    const rgForm = document.getElementById("registration-form");
    const rgInput = document.querySelectorAll(".reg-input");
    const btnReg = document.getElementById("reg-btn");
    const btnRegLog = document.getElementById("rg-signin");

    const fname = document.getElementById("f_name");
    const lname = document.getElementById("l_name");
    const userName = document.getElementById("user_name");
    const newEmail = document.getElementById("new_email");
    const bio = document.getElementById("user_bio");
    const phone = document.getElementById("phone");
    const useAvatar = document.getElementById("user_avatar");
    const userJob = document.getElementById("user_job");
    const newPass = document.getElementById("new_password");
    const confPass = document.getElementById("conf_password");
    

    
   

    function showHome() {
        window.location = "/SMA-Team-3/landing-pages/landing.html";

    };

    // All home button will link to home
    Array.from(btnHome).forEach(function(btnHome) {
        btnHome.addEventListener('click', showHome);
    }); 

    
    function showLogin() {
        window.location = "login.html"; 
        rgForm.reset();
        
    };
    btnRegLog.addEventListener('click', function(e) {
        e.preventDefault();
    });
    btnRegLog.addEventListener('click', showLogin);

   
});

