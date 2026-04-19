local content = HttpGet("Your_Link_Here") --use this to fetch url link
local response = HttpRequest("Your_Link_Here", "POST", {["Content-Type"] = "application/json"}, {key = "value"}) --use this to request api
