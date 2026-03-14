document.addEventListener('DOMContentLoaded', () => {
    const sidebar = document.querySelector('.sidebar');
    const content = document.querySelector('.content');
    const resizer = document.querySelector('.resizer');
    
    if (!resizer) return;

    let isResizing = false;

    resizer.addEventListener('mousedown', (e) => {
        isResizing = true;
        document.body.style.cursor = 'col-resize';
        document.body.style.userSelect = 'none';
    });

    document.addEventListener('mousemove', (e) => {
        if (!isResizing) return;
        
        let newWidth = e.clientX;
        if (newWidth < 150) newWidth = 150;
        if (newWidth > 500) newWidth = 500;
        
        sidebar.style.width = newWidth + 'px';
        content.style.marginLeft = newWidth + 'px';
    });

    document.addEventListener('mouseup', () => {
        isResizing = false;
        document.body.style.cursor = 'default';
        document.body.style.userSelect = 'auto';
    });
});
