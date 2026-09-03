const contactForm = document.getElementById("contactForm");

if (contactForm) {
    contactForm.addEventListener("submit", function () {
        // Allow the form to submit normally to Django.
        // Django will save the message to MySQL.
    });
}