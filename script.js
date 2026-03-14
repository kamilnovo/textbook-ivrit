console.log("Ivrit script loaded");
document.addEventListener('DOMContentLoaded', () => {
    const sidebar = document.querySelector('.sidebar');
    const content = document.querySelector('.content');
    const resizer = document.querySelector('.resizer');
    
    if (!resizer) {
        console.error("Resizer element not found!");
        return;
    }

    let isResizing = false;

    resizer.addEventListener('mousedown', (e) => {
        isResizing = true;
        document.body.style.cursor = 'col-resize';
        resizer.style.background = '#3498db'; // Highlight while dragging
        console.log("Resize started");
    });

    window.addEventListener('mousemove', (e) => {
        if (!isResizing) return;
        
        let newWidth = e.clientX;
        if (newWidth < 150) newWidth = 150;
        if (newWidth > 600) newWidth = 600;
        
        sidebar.style.width = newWidth + 'px';
        content.style.marginLeft = newWidth + 'px';
    });

    window.addEventListener('mouseup', () => {
        if (isResizing) {
            isResizing = false;
            document.body.style.cursor = 'default';
            resizer.style.background = 'transparent';
            console.log("Resize finished");
        }
    });
});
