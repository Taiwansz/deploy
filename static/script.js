<script>
    document.addEventListener('scroll', function() {
        const parallax = document.querySelector('.parallax');
        const scrollPos = window.pageYOffset;

        parallax.style.backgroundPosition = `center ${scrollPos * 0.5}px`;
    });


</script>