(1..100).each do |num|
	str = ''
	str += 'Fizz' if(num%3)==0
	str += 'Buzz' if(num%5)==0
	if str.empty?
		puts num
	else
		puts str
	end
end

