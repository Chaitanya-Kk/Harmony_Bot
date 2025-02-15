document.addEventListener("DOMContentLoaded", () => {
    const signinForm = document.getElementById("signin-form");

    signinForm.addEventListener("submit", (e) => {
        e.preventDefault();
        const username = document.getElementById("username").value;
        const password = document.getElementById("password").value;

        // Handle the sign-in process here
        console.log("Username:", username);
        console.log("Password:", password);

        // Redirect to the chat page after sign-in
        window.location.href = "/";
    });
});