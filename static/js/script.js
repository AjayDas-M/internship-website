const links = document.querySelectorAll('.nav-link');

links.forEach(link => {

    link.addEventListener('click', function() {

        // remove active class from all
        links.forEach(item => {
            item.classList.remove('active');
        });

        // add active class to clicked item
        this.classList.add('active');

    });

});


function toggleMenu() {
    var menu = document.getElementById("dropdownMenu");
    menu.style.display = menu.style.display === "flex" ? "none" : "flex";
}

window.onclick = function(event) {
    if (!event.target.closest('.profile-menu')) {
        var menu = document.getElementById("dropdownMenu");
        if (menu) menu.style.display = "none";
    }
}