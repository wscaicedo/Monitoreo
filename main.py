#!/usr/bin/python3
import psutil


def main():
    def get_cpu_usage_pct():
       return psutil.cpu_percent(interval=0.5)
# Output current CPU load as a percentage.
    print('CPU {} %'.format(get_cpu_usage_pct()))


    def get_ram_usage():
        return int(psutil.virtual_memory().total - psutil.virtual_memory().available)
        # Output current RAM usage in MB
    print('RAM {} MB'.format(int(get_ram_usage() / 1024 / 1024)))



if __name__ == "__main__":
    main ()
    
    
