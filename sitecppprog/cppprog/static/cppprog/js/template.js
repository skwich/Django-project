const menu = document.querySelector(".nav-menu");
window.addEventListener("scroll", () => {
    if (pageYOffset > 100) {
        menu.classList.add("sticky");
    }
    else {
        menu.classList.remove("sticky");
    }
});