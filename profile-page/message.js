document.addEventListener("DOMContentLoaded", () => {
    // Select All Home Buttons Elements
    // const btnHome = document.querySelectorAll(".auth-icon-btn");
    
    // Select Login page button element
    const btnMsg = document.getElementById("mb-msg-btn");
    const mbTextarea = document.getElementById("mb-msg-box");
    const btnOk = document.getElementById("btn-send-msg");
    const mbMessageBox = document.getElementById("messages");
    // const btnLogReg = document.getElementById("log-reg");
    // const btnLogFor = document.getElementById("log-forgot");

    function openTextArea() {
        mbTextarea.style.display = "block";
        btnMsg.style.display = "none";
        mbMessageBox.style.padding = "0";
    }
    btnMsg.addEventListener('click', function(e) {
        e.preventDefault();
    });
    btnMsg.addEventListener('click', openTextArea);

    function closeTextArea() {
        mbTextarea.style.display = "none";
        btnMsg.style.display = "block";
        mbMessageBox.style.padding = "10px";
    }

    btnOk.addEventListener('click', function(e) {
        e.preventDefault();
    });
    btnOk.addEventListener('click', closeTextArea);
});