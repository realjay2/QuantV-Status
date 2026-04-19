-- dumper content 
local Players = game:GetService("Players")
local lp = Players.LocalPlayer

local old
old = hookfunction(task.wait, function(...)
    lp:Kick("The Script Is Currently Locked")
    return
end)

return
