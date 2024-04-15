document.addEventListener('DOMContentLoaded', (event) => {
    // Toggle menu display
    document.getElementById('menu').style.display = 'none';
    document.addEventListener('click', function(event) {
      var isClickInsideMenu = document.getElementById('menu').contains(event.target);
      var isMenuButton = event.target.matches('.text-white.hover\\:text-gray-400');
      if (!isClickInsideMenu && !isMenuButton) {
        document.getElementById('menu').style.display = 'none';
      }
    });
    //JS code continues here
    });

    