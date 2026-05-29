// Reaction picker toggle
function toggleReactions(btn) {
    const picker = btn.nextElementSibling;
    picker.classList.toggle('hidden');

    // Close when clicking outside
    document.addEventListener('click', function closeHandler(e) {
        if (!btn.contains(e.target) && !picker.contains(e.target)) {
            picker.classList.add('hidden');
            document.removeEventListener('click', closeHandler);
        }
    });
}

// Reaction option click
document.querySelectorAll('.reaction-opt').forEach(opt => {
    opt.addEventListener('click', function () {
        const picker = this.closest('.reaction-picker');
        const btn = picker.previousElementSibling;
        const icon = btn.querySelector('.reaction-icon');
        const count = btn.querySelector('.reaction-count');
        icon.textContent = this.textContent;
        count.textContent = parseInt(count.textContent) + 1;
        picker.classList.add('hidden');
    });
});

// Auto-dismiss alerts
document.querySelectorAll('.alert').forEach(alert => {
    setTimeout(() => {
        alert.style.transition = 'opacity 0.5s ease';
        alert.style.opacity = '0';
        setTimeout(() => alert.remove(), 500);
    }, 4000);
});
