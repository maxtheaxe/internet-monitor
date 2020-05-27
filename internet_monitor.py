# internet_monitor.py - maxtheaxe
import socket
from datetime import datetime, timedelta
import time
import speed_checker

def is_connected():
    try:
        # connect to the host -- tells us if the host is actually reachable
        # reachable
        socket.create_connection(("www.google.com", 80))
        return True
    except:
        pass
    return False

def save_logs(result):
	newline_result = result + "\n"
	with open("internet_monitor_results.txt", "a") as log_file:
		log_file.write(newline_result)

def main():
	test_number = 29
	while True:
		test_number += 1

		cur_time = datetime.now() - timedelta(minutes=39)
		cur_stats = "Current Time: "
		cur_stats += cur_time.strftime("%m/%d/%Y, %H:%M:%S")
		cur_stats += " | Connection Status: "
		cur_stats += str(is_connected())
		# save logs before speed test (kept separately)
		save_logs(cur_stats)

		# run speedtest every 15 minutes
		if (test_number % 30) == 0:
			cur_stats += "\n" + speed_checker.run_test()

		print(cur_stats)
		time.sleep(30)

if __name__ == "__main__":
	main()
