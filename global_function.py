# ? Calculate execution time of your code and you can assign it in a variable and can also send it in json response.
def get_execution_start_time() -> float:
    import time
    execution_start_time = time.perf_counter()
    return execution_start_time    # * Current time, BEFORE execution of our code.

def get_execution_end_time(execution_start_time : float) -> str:
    import time
    # * Calculating execution time of our API and it's also sent in the API Response.
    execution_end_time = time.perf_counter()    # * Current time, AFTER execution of our code.
    total_execution_time = (execution_end_time - execution_start_time) * 1000
    if 1000 <= total_execution_time < 60000:    # * i.e., seconds
        total_execution_time /= 1000    # * Converting it in seconds.
        total_execution_time_str = str(round(total_execution_time, 2)) + " secs"    # * Converting it into string for API Response.
        # print('\n ##### Execution Time: {:.4f} secs ##### \n'.format(total_execution_time))
    elif total_execution_time >= 60000:    # * i.e., minutes
        total_execution_time /= 60000    # * Converting it in minutes.
        total_execution_time_mins_str = int(total_execution_time)    # * Extracting the decimal part (whole number)
        total_execution_time_secs_str = round((float('0' + str(total_execution_time - int(total_execution_time))[1:]) * 60), 2)    # * Converting fraction mins to secs
        total_execution_time_str = str(total_execution_time_mins_str) + " mins " + str(total_execution_time_secs_str) + " secs"    # * Converting it into string for API Response.
        # print('\n ##### Execution Time: {:.4f} mins ##### \n'.format(total_execution_time))
    else:    # * i.e., milliseconds
        # print('\n ##### Execution Time: {:.2f} ms ##### \n'.format(total_execution_time))
        total_execution_time_str = str(round(total_execution_time, 2)) + " ms"

    return total_execution_time_str
