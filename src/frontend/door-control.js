document.getElementById('open-button').addEventListener('click', () => {
    fetch('/open-door', {
        method: 'POST',
    });
});
