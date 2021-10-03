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
   


    const rgForm = document.getElementById("registration-form");
    const rgInput = document.querySelectorAll(".reg-input");
    const btnReg = document.getElementById("reg-btn");
    const btnRegLog = document.getElementById("rg-signin");

    const fname = document.getElementById("f_name");
    const lname = document.getElementById("l_name");
    const userName = document.getElementById("reg_user_name");
    const newEmail = document.getElementById("new_email");
    const bio = document.getElementById("reg_user_bio");
    const phone = document.getElementById("phone");
    const useAvatar = document.getElementById("reg_user_avatar");
    const userJob = document.getElementById("reg_user_job");
    const newPass = document.getElementById("new_password");
    const confPass = document.getElementById("conf_password");
    


    function showHome() {
        window.location = "/SMA-Team-3/landing-pages/landing.html";
        // lgForm.reset();
        // rgForm.reset();
        
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

    // are login form inputs empty  NOTE: goes to homepage bc profile page is made
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

    // Check Registration Inputs    Empty?
    rgForm.addEventListener('input', function(e) {
        btnReg.addEventListener('click', function(e) {
            e.preventDefault();
        }); 
        btnReg.addEventListener('click', checkReg)
    }); 
    // function getInput() {
    //     Array.from(rgInput).forEach(function(rgInput) {
    //         btnReg.addEventListener('click', checkReg);
    //     }); 

    // }
    function checkReg () {
        // Array.from(rgInput).forEach(function(btnReg) {
        //     btnReg.addEventListener('click', checkReg);
        // }); 
        if(lname.value !== "" && fname.value !== ""  && userName.value !== ""  && newEmail.value.validity == "valid" && newPass.value == confPass.value){
            
            btnReg.addEventListener('click', showLogin);
        }else {
            btnReg.style.backgroundColor = "#ff0000";
        } 
        
    }
    function showLogin() {
        window.location = "login.html"; 
        lgForm.reset(); 
    };
    btnRegLog.addEventListener('click', function(e) {
        e.preventDefault();
    });
    btnRegLog.addEventListener('click', showLogin);

   
});

