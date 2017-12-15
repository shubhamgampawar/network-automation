#!/usr/bin/python
import paramiko
import time

###
def disable_paging(remote_conn):
    '''Disable paging on a Cisco router'''

    remote_conn.send("terminal length 0\n")
    time.sleep(1)

    # Clear the buffer on the screen
    output = remote_conn.recv(1000)

    return output


if __name__ == '__main__':


    # Creadentials of Remote device OR node
    ip = '172.16.1.54'
    #ip = raw_input("Please enter your IP address: ")
    username = 'cisco'
    #username = raw_input("Please enter your username: ")
    password = 'cisco'


    # Create instance of SSHClient object
    remote_conn_pre = paramiko.SSHClient()

    # Automatically add untrusted hosts (make sure okay for security policy in your environment)
    remote_conn_pre.set_missing_host_key_policy(
         paramiko.AutoAddPolicy())

    # initiate SSH connection. While initiating connection with remode device its important to pass variable values of IP , Username and Password. And keychanging we can cancel using giving value as false to look_for_keys=False

    remote_conn_pre.connect(ip, username=username, password=password, look_for_keys=False, allow_agent=False)
   #  After successfully conectin establishment to %ip address remote device print sample text given below
    print "SSH connection established to %s" % ip

    # Use invoke_shell to establish an 'interactive session'
    remote_conn = remote_conn_pre.invoke_shell()
    print "Interactive SSH session established"
    # Strip the initial router prompt
    output = remote_conn.recv(1000)
    # See what we have recived
    print output
    # Turn off paging
    disable_paging(remote_conn)


    # Now let's try to send the router a command
    remote_conn.send("\n")
    remote_conn.send("show ip int brief\n")
    # Wait for the command to complete. It will varry depend s on command execution time and link speed
    time.sleep(2)
    # Store recived output to variable i.e. output
    output = remote_conn.recv(5000)
    # print recived output
    print output

    remote_conn.send("show running-config\n")
    time.sleep(25)
    output = remote_conn.recv(65535)
    print output




