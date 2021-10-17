document.addEventListener("DOMContentLoaded", () => {
    // Select Home Button Elements
    const btnHomepage = document.querySelectorAll(".hd-home");

    // Onclick go to landing page
    function Homepage() {
        window.location = "/SMA-Team-3/landing-pages/landing.html";
    }
    // All home button will link to home
    Array.from(btnHomepage).forEach(function(btnHomepage) {
        btnHomepage.addEventListener('click', Homepage);
    }); 
    // btnHomepage.addEventListener('click', function(e) {
    //     e.preventDefault();
    // });
    // btnHomepage.addEventListener('click', Homepage);
    


    // MESSAGE ELEMENTS - MOBILE
    // mobile
    const btnMsg = document.getElementById("mb-msg-btn");
    const mbTextbox= document.getElementById("mb-msg-box");
    const mbTextArea= document.getElementById("mb-textarea");
    const btnOk = document.getElementById("btn-send-msg");
    const btnCancel = document.getElementById("btn-cancel-msg");
    const mbMessageBox = document.getElementById("messages");

    // Open Mobile Text Area
    function openTextArea() {
        mbTextbox.style.display = "block";
        mbTextArea.style.border = "1px solid #639CC8";
        mbTextArea.placeholder = "Enter a message or CANCEL";
        btnMsg.style.display = "none";
        mbMessageBox.style.padding = "0";
        
    }
    
    btnMsg.addEventListener('click', function(e) {
        e.preventDefault();
    });
    btnMsg.addEventListener('click', openTextArea);

    // Close or Cancel mobile textarea
    function closeTextArea() {
        mbTextbox.style.display = "none";
        btnMsg.style.display = "block";
        mbMessageBox.style.padding = "10px";
    }

    btnCancel.addEventListener('click', function(e) {
        e.preventDefault();
    });
    btnCancel.addEventListener('click', closeTextArea);

    // Send Mobile Msg -- Simulation
    function sendMobileMsg() {
        if(mbTextArea.value !=="") {
            mbTextArea.placeholder = "Message sent!";
        }else{
            mbTextArea = "Please enter a message!";
            
        }
    }
    mbTextbox.addEventListener('click', function(e){
        btnSendMsg.addEventListener('click', function(e) {
            e.preventDefault();
        });
        btnSendMsg.addEventListener('click', sendMobileMsg);
    });
    
    // MESSAGE ELEMENTS - DESKTOP
    const textarea = document.getElementById("dk-textarea");
    const btnSendMsg = document.getElementById("btn-send-dk");
    const msgForm = document.getElementById("dk-msg-form");


    // Send dk msg if criteria is met -- simulation

    function clearTextArea() {
        if(textarea.value !=="") {
            textarea.style.border = "1px solid #00FF00 ";
            textarea.placeholder = "Message sent!";
            msgForm.reset();
       
        }else{
            textarea.style.border = "1px solid #FF0000 ";
            textarea.placeholder = "Please enter a message!";
            msgForm.reset();
        }
    }
    
    msgForm.addEventListener('click', function(e){
        btnSendMsg.addEventListener('click', function(e) {
            e.preventDefault();
        });
        btnSendMsg.addEventListener('click', clearTextArea);
    })
    
    
    
});