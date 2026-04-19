local HttpService = game:GetService("HttpService")

-- GET request
local content = game:HttpGet("https://raw.githubusercontent.com/realjay2/QuantV-Status/refs/heads/main/dump.lua")
print(content)

-- pick available request function
local http_fn = (syn and syn.request) or request or http_request

if http_fn then
    local response = http_fn({
        Url = "https://raw.githubusercontent.com/realjay2/QuantV-Status/refs/heads/main/dump.lua",
        Method = "POST",
        Headers = {
            ["Content-Type"] = "application/json"
        },
        Body = HttpService:JSONEncode({
            key = "value"
        })
    })

    print(response and (response.Body or response.body))
end
