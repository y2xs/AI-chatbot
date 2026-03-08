const buttons = document.querySelectorAll('.btn-primary');

buttons.forEach(button => {
    button.addEventListener('click', function(e) {
        // Stop the link from jumping immediately so we can see the effect
        const targetUrl = this.getAttribute('href');
        if(targetUrl !== "#") {
            e.preventDefault(); 
        }

        const rect = this.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;

        const circle = document.createElement('span');
        circle.classList.add('btn-primary-circle');
        
        circle.style.left = x + 'px';
        circle.style.top = y + 'px';

        const size = Math.max(this.clientWidth, this.clientHeight);
        circle.style.width = circle.style.height = size + 'px';
        circle.style.marginLeft = -(size / 2) + 'px';
        circle.style.marginTop = -(size / 2) + 'px';

        this.appendChild(circle);

        // Wait 300ms for the animation to be visible, then go to the link
        setTimeout(() => {
            circle.remove();
            if(targetUrl !== "#") window.location.href = targetUrl;
        }, 300); 
    });
});
