# speed_checker.py - maxtheaxe
# ref: https://github.com/sivel/speedtest-cli/wiki
import speedtest
from datetime import datetime, timedelta
import time

def speed_check():
	'''runs basic speed test, returns results as dict'''
	servers = []
	threads = None

	s = speedtest.Speedtest()
	s.get_servers(servers)
	s.get_best_server()
	s.download(threads=threads)
	s.upload(threads=threads)
	s.results.share()
	
	return s.results.dict()

def speed_results(results, time_string):
	'''formats results nicely with time'''
	results_string = "\nSpeedtest Results | {}\n".format(time_string)
	results_string += "\tUpload: {} MB/s\n".format(results.get('upload')/1000000)
	results_string += "\tDownload: {} MB/s\n".format(results.get('download')/1000000)
	results_string += "\tPing: {} ms\n".format(results.get('ping'))
	results_string += "\tShare: {}\n".format(results.get('share'))
	return results_string

def log_results(results_string):
	'''logs results to file given nicely formatted string'''
	newline_result = results_string + "\n"
	with open("speed_results.txt", "a") as log_file:
		log_file.write(newline_result)

def run_test():
	'''runs test and saves results with timestamp, 
	returns nicely formatted results'''
	# get current time
	cur_time = datetime.now() - timedelta(minutes=39)
	time_string = "Current Time: "
	time_string += cur_time.strftime("%m/%d/%Y, %H:%M:%S")
	# try running speed test
	try:
		results = speed_check()
		results_string = speed_results(results, time_string)
	# handle case in which not connected
	except:
		results_string = "\nConnection Failed. | {}\n".format(time_string)
	# log and return results
	log_results(results_string)
	return results_string

def main():
	results = speed_check()
	print(speed_results(results))

if __name__ == "__main__":
	main()