LOAD_FILE = 'load.txt'
OUTPUT_TR = "tr_iplist.txt"
OUTPUT_OTHERS = "other_iplist.txt"

TR_IPBLOCKS = [
    ["5.11.128.0", "5.11.255.255"],
    ["5.24.0.0", "5.27.255.255"],
    ["5.44.80.0", "5.44.95.255"],
    ["5.44.144.0", "5.44.159.255"],
    ["5.46.0.0", "5.47.255.255"],
    ["5.104.0.0", "5.104.15.255"],
    ["5.176.0.0", "5.177.255.255"],
    ["5.226.192.0", "5.226.255.255"],
    ["5.229.0.0", "5.229.255.255"],
    ["5.250.240.0", "5.250.255.255"],
    ["24.133.0.0", "24.133.255.255"],
    ["31.6.80.0", "31.6.95.255"],
    ["31.44.192.0", "31.44.207.255"],
    ["31.140.0.0", "31.143.255.255"],
    ["31.145.0.0", "31.145.255.255"],
    ["31.155.0.0", "31.155.255.255"],
    ["31.169.64.0", "31.169.95.255"],
    ["31.176.0.0", "31.176.127.255"],
    ["31.177.128.0", "31.177.255.255"],
    ["31.186.0.0", "31.186.31.255"],
    ["31.200.0.0", "31.200.127.255"],
    ["31.206.0.0", "31.206.255.255"],
    ["31.210.32.0", "31.210.47.255"],
    ["31.210.64.0", "31.210.127.255"],
    ["31.223.0.0", "31.223.127.255"],
    ["37.34.0.0", "37.34.31.255"],
    ["37.72.48.0", "37.72.63.255"],
    ["37.77.0.0", "37.77.31.255"],
    ["37.122.224.0", "37.122.239.255"],
    ["37.123.0.0", "37.123.63.255"],
    ["37.130.64.0", "37.130.127.255"],
    ["37.154.0.0", "37.155.255.255"],
    ["37.218.192.0", "37.218.207.255"],
    ["37.247.96.0", "37.247.111.255"],
    ["46.1.0.0", "46.1.255.255"],
    ["46.2.0.0", "46.2.255.255"],
    ["46.20.0.0", "46.20.15.255"],
    ["46.20.144.0", "46.20.159.255"],
    ["46.45.128.0", "46.45.191.255"],
    ["46.104.0.0", "46.104.255.255"],
    ["46.106.0.0", "46.106.255.255"],
    ["46.154.0.0", "46.155.255.255"],
    ["46.196.0.0", "46.197.255.255"],
    ["46.221.0.0", "46.221.255.255"],
    ["46.234.0.0", "46.234.31.255"],
    ["46.252.96.0", "46.252.111.255"],
    ["62.29.0.0", "62.29.127.255"],
    ["62.108.64.0", "62.108.95.255"],
    ["62.244.192.0", "62.244.255.255"],
    ["62.248.0.0", "62.248.127.255"],
    ["77.79.64.0", "77.79.127.255"],
    ["77.92.96.0", "77.92.127.255"],
    ["77.92.128.0", "77.92.159.255"],
    ["77.223.128.0", "77.223.159.255"],
    ["77.245.144.0", "77.245.159.255"],
    ["78.111.96.0", "78.111.111.255"],
    ["78.135.16.0", "78.135.31.255"],
    ["78.135.32.0", "78.135.63.255"],
    ["78.135.64.0", "78.135.95.255"],
    ["78.135.96.0", "78.135.111.255"],
    ["78.160.0.0", "78.191.255.255"],
    ["79.123.128.0", "79.123.255.255"],
    ["80.93.208.0", "80.93.223.255"],
    ["80.251.32.0", "80.251.47.255"],
    ["81.6.64.0", "81.6.127.255"],
    ["81.8.0.0", "81.8.127.255"],
    ["81.21.160.0", "81.21.175.255"],
    ["81.22.96.0", "81.22.111.255"],
    ["81.91.112.0", "81.91.127.255"],
    ["81.212.0.0", "81.215.255.255"],
    ["82.97.224.0", "82.97.239.255"],
    ["82.145.224.0", "82.145.255.255"],
    ["82.150.64.0", "82.150.95.255"],
    ["82.151.128.0", "82.151.159.255"],
    ["82.222.0.0", "82.222.255.255"],
    ["83.66.0.0", "83.66.255.255"],
    ["84.17.64.0", "84.17.95.255"],
    ["84.44.0.0", "84.44.127.255"],
    ["84.51.0.0", "84.51.63.255"],
    ["85.29.0.0", "85.29.63.255"],
    ["85.95.224.0", "85.95.255.255"],
    ["85.96.0.0", "85.111.255.255"],
    ["85.153.128.0", "85.153.255.255"],
    ["86.108.128.0", "86.108.255.255"],
    ["87.251.0.0", "87.251.31.255"],
    ["88.224.0.0", "88.255.255.255"],
    ["89.19.0.0", "89.19.31.255"],
    ["89.106.0.0", "89.106.31.255"],
    ["89.252.128.0", "89.252.159.255"],
    ["89.252.160.0", "89.252.175.255"],
    ["90.158.0.0", "90.159.255.255"],
    ["91.93.0.0", "91.93.255.255"],
    ["91.151.80.0", "91.151.95.255"],
    ["91.191.160.0", "91.191.175.255"],
    ["92.44.0.0", "92.45.255.255"],
    ["92.61.0.0", "92.61.15.255"],
    ["92.63.0.0", "92.63.15.255"],
    ["93.89.16.0", "93.89.31.255"],
    ["93.89.64.0", "93.89.79.255"],
    ["93.89.224.0", "93.89.239.255"],
    ["93.91.64.0", "93.91.79.255"],
    ["93.155.0.0", "93.155.127.255"],
    ["93.182.64.0", "93.182.127.255"],
    ["93.184.144.0", "93.184.159.255"],
    ["93.186.112.0", "93.186.127.255"],
    ["94.54.0.0", "94.55.255.255"],
    ["94.73.128.0", "94.73.191.255"],
    ["94.78.64.0", "94.78.127.255"],
    ["94.79.64.0", "94.79.127.255"],
    ["94.101.80.0", "94.101.95.255"],
    ["94.102.0.0", "94.102.15.255"],
    ["94.102.64.0", "94.102.79.255"],
    ["94.103.32.0", "94.103.47.255"],
    ["94.120.0.0", "94.123.255.255"],
    ["94.138.192.0", "94.138.223.255"],
    ["94.235.0.0", "94.235.255.255"],
    ["95.0.0.0", "95.15.255.255"],
    ["95.65.128.0", "95.65.255.255"],
    ["95.70.128.0", "95.70.255.255"],
    ["95.142.128.0", "95.142.143.255"],
    ["95.173.0.0", "95.173.31.255"],
    ["95.173.160.0", "95.173.191.255"],
    ["95.173.224.0", "95.173.255.255"],
    ["95.183.128.0", "95.183.255.255"],
    ["109.228.192.0", "109.228.255.255"],
    ["139.179.0.0", "139.179.255.255"],
    ["141.196.0.0", "141.196.255.255"],
    ["144.122.0.0", "144.122.255.255"],
    ["149.0.0.0", "149.0.255.255"],
    ["149.140.0.0", "149.140.255.255"],
    ["151.135.0.0", "151.135.255.255"],
    ["151.250.0.0", "151.250.255.255"],
    ["155.223.0.0", "155.223.255.255"],
    ["159.20.64.0", "159.20.95.255"],
    ["159.146.0.0", "159.146.127.255"],
    ["159.253.32.0", "159.253.47.255"],
    ["160.75.0.0", "160.75.255.255"],
    ["161.9.0.0", "161.9.255.255"],
    ["167.160.0.0", "167.160.31.255"],
    ["168.139.0.0", "168.139.255.255"],
    ["176.30.0.0", "176.30.255.255"],
    ["176.33.0.0", "176.33.255.255"],
    ["176.40.0.0", "176.43.255.255"],
    ["176.53.0.0", "176.53.127.255"],
    ["176.54.0.0", "176.55.255.255"],
    ["176.88.0.0", "176.88.255.255"],
    ["176.89.0.0", "176.89.255.255"],
    ["176.90.0.0", "176.91.255.255"],
    ["176.216.0.0", "176.219.255.255"],
    ["176.220.0.0", "176.220.255.255"],
    ["176.227.0.0", "176.227.127.255"],
    ["176.232.0.0", "176.233.255.255"],
    ["176.234.0.0", "176.235.255.255"],
    ["176.236.0.0", "176.236.255.255"],
    ["176.237.0.0", "176.237.255.255"],
    ["176.238.0.0", "176.239.255.255"],
    ["176.240.0.0", "176.240.255.255"],
    ["178.18.192.0", "178.18.207.255"],
    ["178.210.160.0", "178.210.191.255"],
    ["178.211.32.0", "178.211.63.255"],
    ["178.233.0.0", "178.233.255.255"],
    ["178.240.0.0", "178.247.255.255"],
    ["188.3.0.0", "188.3.255.255"],
    ["188.38.0.0", "188.38.255.255"],
    ["188.41.0.0", "188.41.255.255"],
    ["188.56.0.0", "188.59.255.255"],
    ["188.119.0.0", "188.119.63.255"],
    ["188.124.0.0", "188.124.31.255"],
    ["188.125.160.0", "188.125.191.255"],
    ["188.132.128.0", "188.132.255.255"],
    ["193.140.0.0", "193.140.255.255"],
    ["193.192.96.0", "193.192.127.255"],
    ["193.243.192.0", "193.243.223.255"],
    ["193.255.0.0", "193.255.255.255"],
    ["194.27.0.0", "194.27.255.255"],
    ["194.54.32.0", "194.54.63.255"],
    ["195.33.192.0", "195.33.255.255"],
    ["195.46.128.0", "195.46.159.255"],
    ["195.87.0.0", "195.87.255.255"],
    ["195.112.128.0", "195.112.159.255"],
    ["195.142.16.0", "195.142.31.255"],
    ["195.142.32.0", "195.142.63.255"],
    ["195.142.64.0", "195.142.95.255"],
    ["195.142.112.0", "195.142.127.255"],
    ["195.142.160.0", "195.142.175.255"],
    ["195.142.224.0", "195.142.239.255"],
    ["195.155.0.0", "195.155.63.255"],
    ["195.155.64.0", "195.155.95.255"],
    ["195.155.112.0", "195.155.127.255"],
    ["195.155.128.0", "195.155.159.255"],
    ["195.155.160.0", "195.155.191.255"],
    ["195.155.192.0", "195.155.255.255"],
    ["195.174.0.0", "195.174.255.255"],
    ["195.175.0.0", "195.175.255.255"],
    ["195.214.128.0", "195.214.191.255"],
    ["195.244.32.0", "195.244.63.255"],
    ["212.2.192.0", "212.2.223.255"],
    ["212.12.128.0", "212.12.159.255"],
    ["212.15.0.0", "212.15.31.255"],
    ["212.29.64.0", "212.29.127.255"],
    ["212.31.0.0", "212.31.31.255"],
    ["212.50.32.0", "212.50.63.255"],
    ["212.57.0.0", "212.57.31.255"],
    ["212.58.0.0", "212.58.31.255"],
    ["212.64.192.0", "212.64.223.255"],
    ["212.65.128.0", "212.65.159.255"],
    ["212.68.48.0", "212.68.63.255"],
    ["212.98.0.0", "212.98.31.255"],
    ["212.98.192.0", "212.98.255.255"],
    ["212.101.96.0", "212.101.127.255"],
    ["212.108.128.0", "212.108.159.255"],
    ["212.109.96.0", "212.109.127.255"],
    ["212.109.224.0", "212.109.255.255"],
    ["212.115.0.0", "212.115.31.255"],
    ["212.125.0.0", "212.125.31.255"],
    ["212.127.96.0", "212.127.127.255"],
    ["212.133.128.0", "212.133.255.255"],
    ["212.146.128.0", "212.146.255.255"],
    ["212.154.0.0", "212.154.127.255"],
    ["212.156.0.0", "212.156.255.255"],
    ["212.174.0.0", "212.174.255.255"],
    ["212.175.0.0", "212.175.255.255"],
    ["212.252.0.0", "212.252.255.255"],
    ["212.253.0.0", "212.253.255.255"],
    ["213.14.0.0", "213.14.127.255"],
    ["213.14.128.0", "213.14.143.255"],
    ["213.14.144.0", "213.14.159.255"],
    ["213.14.160.0", "213.14.191.255"],
    ["213.14.192.0", "213.14.255.255"],
    ["213.43.0.0", "213.43.255.255"],
    ["213.74.0.0", "213.74.255.255"],
    ["213.128.64.0", "213.128.95.255"],
    ["213.142.128.0", "213.142.159.255"],
    ["213.143.224.0", "213.143.255.255"],
    ["213.144.96.0", "213.144.127.255"],
    ["213.148.64.0", "213.148.95.255"],
    ["213.153.128.0", "213.153.159.255"],
    ["213.153.160.0", "213.153.191.255"],
    ["213.153.192.0", "213.153.255.255"],
    ["213.155.96.0", "213.155.127.255"],
    ["213.161.128.0", "213.161.159.255"],
    ["213.186.128.0", "213.186.159.255"],
    ["213.194.64.0", "213.194.127.255"],
    ["213.211.0.0", "213.211.31.255"],
    ["213.232.0.0", "213.232.63.255"],
    ["213.238.128.0", "213.238.191.255"],
    ["213.243.0.0", "213.243.31.255"],
    ["213.243.32.0", "213.243.63.255"],
    ["213.248.128.0", "213.248.191.255"],
    ["213.254.128.0", "213.254.159.255"],
    ["217.17.144.0", "217.17.159.255"],
    ["217.31.224.0", "217.31.239.255"],
    ["217.31.240.0", "217.31.255.255"],
    ["217.64.208.0", "217.64.223.255"],
    ["217.65.176.0", "217.65.191.255"],
    ["217.68.208.0", "217.68.223.255"],
    ["217.78.96.0", "217.78.111.255"],
    ["217.116.192.0", "217.116.207.255"],
    ["217.131.0.0", "217.131.255.255"],
    ["217.169.192.0", "217.169.207.255"],
    ["217.174.32.0", "217.174.47.255"],
    ["217.195.192.0", "217.195.207.255"]
]