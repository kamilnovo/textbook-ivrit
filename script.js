document.addEventListener('DOMContentLoaded', () => {
    const sidebar = document.querySelector(".sidebar");
    const content = document.querySelector(".content");
    const resizer = document.querySelector(".resizer");
    if (!sidebar || !resizer || !content) return;

    const savedWidth = localStorage.getItem("sidebarWidth");
    if (savedWidth) {
        sidebar.style.width = savedWidth + "px";
        content.style.marginLeft = savedWidth + "px";
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
        sidebar.style.width = newWidth + "px";
        content.style.marginLeft = newWidth + "px";
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