import os
import shlex, subprocess

def executeBash(bashCommand):
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    return process.communicate()

def executeSudoBash(bashCommand):
    process = subprocess.Popen(shlex.split(bashCommand), stdout=subprocess.PIPE)
    return process.communicate()

def addPublicKeyToFile(public_key,filepath):
    bashCommand = 'sudo bash -c "echo ' + public_key + ' >> ' + filepath + '"'
    return executeSudoBash(bashCommand)

def addAWSCredentialsToFile(access_key,secret_access_key,filepath):
    # User profile
    bashCommand = 'sudo bash -c "echo [default] > ' + filepath + '"'
    executeSudoBash(bashCommand)

    # Access Key
    bashCommand = 'sudo bash -c "echo aws_access_key_id = ' + access_key + ' >> ' + filepath + '"'
    executeSudoBash(bashCommand)

    # Secret Access Key
    bashCommand = 'sudo bash -c "echo aws_secret_access_key = ' + secret_access_key + ' >> ' + filepath + '"'
    executeSudoBash(bashCommand)

def addAWSConfigToFile(region_name,output_format,filepath):
    # User profile
    bashCommand = 'sudo bash -c "echo [default] > ' + filepath + '"'
    executeSudoBash(bashCommand)

    # Region Name
    bashCommand = 'sudo bash -c "echo region = ' + region_name + ' >> ' + filepath + '"'
    executeSudoBash(bashCommand)

    # Output File Format
    bashCommand = 'sudo bash -c "echo output = ' + output_format + ' >> ' + filepath + '"'
    executeSudoBash(bashCommand)

def getPID(port_number):
    bashCommand = "fuser " + port_number + "/tcp"
    return executeBash(bashCommand)

def stopWebApp(pid=None,port_number=None):
    bashCommand = ''
    if port_number.isdigit():
        if port_number != None:
            bashCommand = 'sudo bash -c "fuser -k ' + port_number + '/tcp"'        
    if pid != None:
        bashCommand = 'sudo bash -c "kill ' + pid + '"'

    executeSudoBash(bashCommand)

def gitCommands(action):
    commands = {
        'pull':'pull',
        'fetch':'fetch',
        'reset':'reset --hard origin/master',
    }

    bashCommand = 'sudo bash -c "git ' + commands[action] + '"'
    return executeSudoBash(bashCommand)
