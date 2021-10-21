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
    
    
     // FOLLOW BUTTONS

     const btnHolder = document.querySelectorAll(".follow-container");
     const followBtn = document.querySelectorAll(".btn-follow");
     
     
     
     const mobileFollow = document.getElementById("mobile-follow");
     const deskFollow = document.getElementById("desk-follow");
     followBtn.forEach(Follow);
 
     function Follow(item) {
         var num = document.getElementById("pf-num");
         let count = document.getElementById("pf-num").getAttribute("placeholder");
        
         let numbers = Number(count);
         
         for (i = 0; i < btnHolder.length - 1; i++) {    
             if (followBtn[i].innerHTML == "Follow") {
                 mobileFollow.innerHTML = "Following";
                 deskFollow.innerHTML = "Following";
                 mobileFollow.style.backgroundColor = "#F8C164";
                 deskFollow.style.backgroundColor = "#F8C164";
 
                 numbers += 1
                 var numbersUp = Number(numbers);
                 console.log(numbersUp);
                 
                 let countUp = `${numbersUp}`
                 num.value = `${countUp}`
 
             } else if(followBtn[i].innerHTML == "Following") {
                 let newCount = Number(num.value)
 
                 mobileFollow.innerHTML = "Follow";
                 deskFollow.innerHTML = "Follow";
                 mobileFollow.style.backgroundColor = "#EE9062";
                 deskFollow.style.backgroundColor = "#EE9062";
                 newCount -= 1
                 var numbersDown = Number(newCount);
                 
                 let countDown = `${numbersDown}`
                 console.log(countDown)
                 num.value = `${countDown}`
             }
         }
        
     }; 
     Array.from(followBtn).forEach(function(followBtn) {
         followBtn.addEventListener('click', Follow);
     }); 

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
    mbTextbox.addEventListener('submit', function(e){
        btnOk.addEventListener('click', function(e) {
            e.preventDefault();
        });
        btnOk.addEventListener('click', sendMobileMsg);
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