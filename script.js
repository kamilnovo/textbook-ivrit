document.addEventListener('DOMContentLoaded', () => {
    const sidebar = document.querySelector(".sidebar");
    const resizer = document.querySelector(".resizer");
    if (!sidebar || !resizer) return;

    // Load saved width from localStorage and apply it to CSS variable
    const savedWidth = localStorage.getItem("sidebarWidth");
    if (savedWidth) {
        document.documentElement.style.setProperty('--sidebar-width', savedWidth + "px");
    }

    let isResizing = false;

    resizer.addEventListener("mousedown", (e) => {
        e.preventDefault();
        isResizing = true;
        resizer.classList.add("resizing");
        document.body.classList.add("resizing-active");
        document.body.style.cursor = "col-resize";
    });

    window.addEventListener("mousemove", (e) => {
        if (!isResizing) return;
        let newWidth = e.clientX;
        if (newWidth < 150) newWidth = 150;
        if (newWidth > 600) newWidth = 600;
        
        // Update CSS variable directly for smooth and instant response
        document.documentElement.style.setProperty('--sidebar-width', newWidth + "px");
        localStorage.setItem("sidebarWidth", newWidth);
    });

    window.addEventListener("mouseup", () => {
        if (isResizing) {
            isResizing = false;
            resizer.classList.remove("resizing");
            document.body.classList.remove("resizing-active");
            document.body.style.cursor = "default";
        }
    });
});
