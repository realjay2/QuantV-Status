import webview
import os
import random
base_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(base_dir, "runtime", "ran")
os.makedirs(output_dir, exist_ok=True)
code = "".join(str(random.randint(0, 9)) for _ in range(16))
lua_content = f'print("{code}")'
file_path = os.path.join(output_dir, f"{code}.lua")
with open(file_path, "w", encoding="utf-8") as f:
    f.write(lua_content)

html = """
<!DOCTYPE html>
<html>
<head>
<style>
body {
    margin: 0;
    overflow: hidden;
    font-family: Arial;
}

/* LOADING SCREEN */
#loading {
    position: fixed;
    width: 100%;
    height: 100%;
    background: #111;
    color: white;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    z-index: 999;
}

.spinner {
    width: 40px;
    height: 40px;
    border: 4px solid rgba(255,255,255,0.2);
    border-top: 4px solid white;
    border-radius: 50%;
    animation: spin 1s linear infinite;
    margin-bottom: 15px;
}

@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

/* TOP BAR */
#bar {
    height: 32px;
    display: flex;
    justify-content: flex-end;
    align-items: center;
    background: rgba(20, 20, 20, 0.65);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border-bottom: 1px solid rgba(255,255,255,0.08);
    -webkit-app-region: drag;
}

.btn {
    width: 38px;
    height: 28px;
    margin-right: 4px;
    color: white;
    text-align: center;
    line-height: 28px;
    cursor: pointer;
    border-radius: 6px;
    -webkit-app-region: no-drag;
}

.btn:hover {
    background: rgba(255,255,255,0.12);
}

#close:hover {
    background: #e74c3c;
}

/* SIDEBAR */
#sidebar {
    position: fixed;
    top: 0;
    right: -320px;
    width: 320px;
    height: 100%;
    background: rgba(25,25,25,0.92);
    backdrop-filter: blur(14px);
    transition: 0.25s ease;
    color: white;
    padding: 20px;
    box-shadow: -10px 0 30px rgba(0,0,0,0.5);
}

#sidebar.open {
    right: 0;
}

.sidebtn {
    width: 100%;
    padding: 10px;
    margin-top: 10px;
    background: rgba(255,255,255,0.08);
    border-radius: 8px;
    cursor: pointer;
}

.sidebtn:hover {
    background: rgba(255,255,255,0.15);
}

/* CONTENT */
#content {
    height: calc(100vh - 32px);
}
</style>
</head>

<body>

<!-- LOADING SCREEN -->
<div id="loading">
    <div class="spinner"></div>
    Loading Luauth...
</div>

<!-- TOP BAR -->
<div id="bar">
    <div class="btn">—</div>
    <div class="btn" id="close">✕</div>
</div>

<!-- SIDEBAR -->
<div id="sidebar">
    <h2>Menu</h2>
    <div class="sidebtn">Settings</div>
    <div class="sidebtn">Close UI</div>
</div>

<script>
// ESC toggle sidebar
document.addEventListener("keydown", function(e) {
    if (e.key === "Escape") {
        toggleSidebar();
    }
});

function toggleSidebar() {
    document.getElementById("sidebar").classList.toggle("open");
}

// hide loading when page is ready
window.onload = function () {
    setTimeout(() => {
        document.getElementById("loading").style.display = "none";
    }, 1200); // small delay for smooth feel
};
</script>

</body>
</html>
"""

settings = {
    'user_agent': 'LuauthClient/1.0 (CustomApp; Windows)'
}

window = webview.create_window(
    "Luauth App",
    "https://luauth.org",
    width=1400,
    height=900,
    frameless=True
)

webview.start(gui="edgechromium", user_agent=settings['user_agent'])
