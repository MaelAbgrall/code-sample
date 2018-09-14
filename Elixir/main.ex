require Math

IO.puts("hello world")
# immah comment

myvar = 2
IO.puts(myvar)
myvar ="hello"
IO.puts(myvar)

a = false
if a === true do
  IO.puts "Variable a is true!"
else
  IO.puts "Variable a is false!"
end
IO.puts "Outside the if statement"

case 3 do
  1 -> 
    IO.puts("Hi, I'm one")
  2 -> 
    IO.puts("Hi, I'm two")
  3 -> 
    IO.puts("Hi, I'm three")
    IO.puts("hellooooo")
  _ -> 
    IO.puts("Oops, you dont match!")
end