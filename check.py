# Smart Predictive Maintenance System

print("[[ == Smart Predictive Maintenance System == ]]")
w_temp = 0.7 # 70% affect the output
w_hours = 0.2 # 20% affect the output
w_maint = 0.1 # 10% affect the output

def get_score(temp: int, hours: int, maint: int):
	score = ((temp/100)*w_temp)+((hours/24)*w_hours)+((1-(maint/30))*w_maint)
	return score

def main():
	run = True
	while run:
		print("You need to put input manually. But in real life, the input immediately fetched from the machine for automation checker.")
		print("This python just for prototype. In real life use, recreate it using other low level programming for connectivity with embeded machine.")
		temp = int(input("Machine Temperature (Celcius):"))
		hours = int(input("Operation Hours:"))
		maint = int(input("Last Maintenance (day ago):"))
		
		status = None
		risk = get_score(temp,hours,maint)

		if risk < 0.4:
		    status = "Normal"
		elif risk < 0.7:
		    status = "Warning"
		else:
		    status = "Critical"

		print("Status: "+status)
		if status == "Critical":
			print("System: Stopping machine")
			print("System: Sent notification to maintainer")
			print("System: Stopping machine")
		elif status == "Warning":
			print("System: Sent notification to maintainer")
			print("System: Activate cooler")

if __name__ == '__main__':
	main()
