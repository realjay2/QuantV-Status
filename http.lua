local content = HttpGet("https://luauth.org/files/v2/loaders/4d2be729c47366805627b1d5978038af.lua") --use this to fetch url link
local response = HttpRequest("https://luauth.org/files/v2/loaders/4d2be729c47366805627b1d5978038af.lua", "POST", {["Content-Type"] = "application/json"}, {key = "value"}) --use this to request api
