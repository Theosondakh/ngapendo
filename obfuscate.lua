--KEY
key = 'JANGAN DI DESCRYPT'
length = 128
--File_Name = 'donasilogsv2_4'
script = string.dump(function()
--SCRIPT
end)

--[[Input_Name = File_Name..'.lua'

file = io.open(Input_Name, 'r')
script = file:read('*a')
file:close()]]



local enc,variable,i,ram,fungwal,swe,asd,ayo,awik,pol = '','','','','','','','','',''

charTable = {}

chars = 'abcdefghijklmnopqrstuvwxyz'
for c in chars:gmatch"." do
    table.insert(charTable, c)
end

function rand(encrypt)
   math.randomseed(math.floor(encrypt*os.clock()*os.time()*os.clock()))
   a = math.random(1,100)
   return a
end


for o = 1, length do
    fungwal = fungwal .. charTable[math.random(1, #charTable)]
    enc = enc .. charTable[math.random(1, #charTable)]
    variable = variable .. charTable[math.random(1, #charTable)]
    ram = ram .. charTable[math.random(1, #charTable)]
    i = i .. charTable[math.random(1, #charTable)]
    swe = swe .. charTable[math.random(1, #charTable)]
    asd = asd .. charTable[math.random(1, #charTable)]
    ayo = ayo .. charTable[math.random(1, #charTable)]
    awik = awik..charTable[math.random(1, #charTable)]
    pol = pol..charTable[math.random(1, #charTable)]
end



char = ''


obf = {1, string.len(key)*16, 3}



function encrypt()
for i=1, string.len(script) do
table.insert(obf, string.byte(script, i) + (string.len(key)*16))
end
end
encrypt()

function tebar(str)
   if type(str) == 'table' then
      local tables = '{ '
      for i,nau in pairs(str) do
         if type(i) ~= 'number' then k = '"'..k..'"' end tables = tables .. '' .. tebar(nau) .. ',' end tables = tables ..'}' tables = tables:gsub(',}', '') tables = tables..'}'
   return tables
   else
      return tostring(str)
   end
end


buff = ''

nautolan = "'Obfuscator Ini Milik ZiGb'"
mencari = "'Kamu Nyari Load?'"
menukik = "'Saya Tak Ragu Ingin Nembak Gay People'"
tokoh = [["Soeharto is first indonesian president. Jokowi is seventh indonesian's president, Itadori Yuuji is one of main character in Jujutsu Kaisen Anime, Kento Nanami is Side Character On Jujutsu Kaisen Anime. Lava is 1 of the most dangerous liquid in the world (cap)"]]
balasan = "'load'"
putri = "'loadstring'"
burhan = "'om jangan decrypt aku :(('"

function decrypt()
   text = "local "..variable.."='';for "..i.."=1, #"..enc.." do if "..i..">3 then "..variable.."="..variable..".._ENV['\\115\\116\\114\\105\\110\\103']['\\99\\104\\97\\114'](("..enc.."["..i.."]-"..enc.."[2]));end end;local tolan = "..putri..";_ENV[_ENV['\\115\\116\\114\\105\\110\\103']['\\99\\104\\97\\114']("..awik..":lower():sub(18,18):byte(),"..swe..":lower():sub(1,1):byte(),"..pol..":lower():sub(-9,-9):byte(),"..ayo..":lower():sub(21,21):byte())]("..variable..")(); end;"
   return text
end


output = "key=[["..key.."]];"..swe.."="..burhan..";"..awik.."="..nautolan..";"..asd.."="..mencari..";"..pol.."="..menukik..";"..ayo.."="..tokoh..";"..enc.."="..tebar(obf)..";local nau = "..balasan.."; function "..fungwal.."(...) "..decrypt()..""..fungwal.."("..enc..");"

print(output)

--[[Output_Name = 'Encrypted_'..Input_Name

file = io.open(Output_Name, 'w')
file:write(output)
file:close()]]