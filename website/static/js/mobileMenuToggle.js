document.getElementById("mobile-menu-toggle").onclick = toggleMenu;

function toggleMenu() {
    var element = document.getElementById("mobile-menu-2");
    if (element.classList.contains("hidden")) {
        element.classList.remove("hidden")
    } else {
        element.classList.add("hidden")
    }
} 