

function openNav() {
  document.getElementById("mySidenav").style.width = "250px";
}

function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
}

function toggleSidenavLocations() {
  const menu = document.getElementById("sidenavLocationsMenu");
  menu.style.display = menu.style.display === 'none' || menu.style.display === '' ? 'flex' : 'none';
}

// Make dropdown work on touch/click (for mobile & tablet users)
document.addEventListener('DOMContentLoaded', function() {
  const dropdowns = document.querySelectorAll('.dropdown');
  
  dropdowns.forEach(dropdown => {
    const btn = dropdown.querySelector('.dropbtn');
    const content = dropdown.querySelector('.dropdown-content');
    
    if (btn && content) {
      btn.addEventListener('click', function(e) {
        e.preventDefault();
        // Toggle the dropdown open/closed
        content.style.display = content.style.display === 'block' ? 'none' : 'block';
      });
      
      // Close dropdown when clicking a link inside it
      const links = content.querySelectorAll('a:not(.disabled)');
      links.forEach(link => {
        link.addEventListener('click', function() {
          content.style.display = 'none';
        });
      });
    }
  });
  
  // Close dropdown when clicking outside
  document.addEventListener('click', function(e) {
    dropdowns.forEach(dropdown => {
      if (!dropdown.contains(e.target)) {
        dropdown.querySelector('.dropdown-content').style.display = 'none';
      }
    });
  });
});



(async () => {
    const res = await fetch('/partials/navbar.html');   // or './partials/navbar.html'
    document.getElementsByClassName('navbarBody').innerHTML = await res.text();
  })();

  

let slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
  showSlides(slideIndex += n);
}

function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}    
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";  
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";  
  dots[slideIndex-1].className += " active";
}