# objectives:

# be able to connect to chat server
from ftplib import FTP
# receive overt message and display to stdout

# time delays between characters of overt messages
# uses two most frequent delays to map to 0 and 1
# decode the binary we've gotten
# display covert message to stdout





# things needed for this to work:
# iptables - gets times for chat timing
# look at tcp packets --- times of delays are what we need here (@Conan and @Michael, you know more about this than me)
# decode each section of 7, end when we get to EOF
# need to use binary decoder as well
