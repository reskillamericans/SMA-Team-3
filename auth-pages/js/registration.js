document.addEventListener("DOMContentLoaded", () => {
    // Select All Home Buttons Elements
    const btnHome = document.querySelectorAll(".auth-icon-btn");
    const required = document.querySelectorAll("input[required]");
    
   

    // Select Elements From Registration page 
    const rgForm = document.getElementById("registration-form");
    const rgInput = document.querySelectorAll(".reg-input");
    const btnReg = document.getElementById("reg-btn");
    const btnRegLog = document.getElementById("rg-signin");


    
    // SELECT AVATAR ELEMENTS
    const fileBtn = document.getElementById("fileupload-btn");
    const fileChosen = document.getElementById("file-chosen");

    // DISPLAY FILE SELECTED
    fileBtn.addEventListener('change', function(){
        fileChosen.textContent = this.files[0].name
    })
    
   
    // RETURN TO LANDING PAGE
    function showHome() {
        window.location = "/SMA-Team-3/landing-pages/landing.html";

    };

    // All home button will link to home
    Array.from(btnHome).forEach(function(btnHome) {
        btnHome.addEventListener('click', showHome);
    }); 

    // FUNCTION GO TO LOGIN 
    function showLogin() {
        window.location = "login.html"; 
        
    };

    // TO LOGIN AFTER REGISTERING
    btnReg.addEventListener('click', function(e) {
        e.preventDefault();
    });
    btnReg.addEventListener('click', showLogin);

    // TO LOGIN IF ALREADY HAVE AN ACCT
    btnRegLog.addEventListener('click', function(e) {
        e.preventDefault();
    });
    btnRegLog.addEventListener('click', showLogin);
   
});

