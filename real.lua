local content = HttpGet("https://raw.githubusercontent.com/realjay2/QuantV-Status/refs/heads/main/dump.luae") --use this to fetch url link
local response = HttpRequest("https://raw.githubusercontent.com/realjay2/QuantV-Status/refs/heads/main/dump.lua", "POST", {["Content-Type"] = "application/json"}, {key = "value"}) --use this to request api
