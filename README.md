## Machine Statistics Collection System

This is my work for a coding assignment for a IT Company (I won't reveal its name to keep the confidence). The following section are extracted from the original assignment document.

For additional information about installation and the work done, refer to [README.txt](README.txt)

### Introduction 

The project is scoped to be simple and reasonable in size to enable you to demonstrate your enterprise-class skills. Though this is a fictitious example, this scenario is very similar to what you may encounter inyour job.

### Instructions

* Try to complete as much as possible within the given time frame. If you need more time, please ask
for an extension. You must complete full-functionality of the application with industry-level coding
style/commenting. Unfinished assignments will not be considered.
* Please note that you are expected to work on the assignment independently. Discussing assignment
details with colleagues or any indication of outside help will be considered cheating.
* Please do not expect too much hand-holding as this is an evaluation assignment.
* Read the complete assignment before you start. Understand clearly what is required so that your
work will be appropriate and easier.

### Overall Objective

Create the architecture and design of a network based machine statistics collection system. Implement the
system's applications.

### Prerequisites

The following prerequisites should be respected.
1. You can code in python using any IDE you prefer.
2. Use any SQL database e.g. mySQL
3. Do not use any proprietary technologies or tools that are not available for free or for trial.

### Functional Requirements

The system allows collection of machine statistics in an intranet environment. The system implements the
following specifications.

#### Client Script
1. This script will be uploaded and executed to 100s of machines in the intranet. These
machines are meant to be monitored for system level statistics like memory usage, CPU
usage, total uptime and windows security event logs (in case of windows OS).
2. When executed, the client script collects the statistics and return them to the server script for
cumulation.
3. The client script must encrypt the data before returning it to server.

#### Server Script

1. Installed on a single central machine in the same intranet.
2. Each client is configured in a server config xml file something like this

```
<client ip=’127.0.0.1’ port=’22’ username=’user’ password=’password’ mail="asa@asda.com">
  <alert type="memory" limit="50%" />
  <alert type="cpu" limit="20%" />
</client>
```

3. When executed, the server script should connect to each client using ssh, upload the client
script in a temp directory, execute it and get the response.
4. After receiving the response from the client script, server script should decode it and stores it
into a relational database along with client ip. This collected data is consumed by another
application, that is out of scope, but you may design the database table yourself.
5. The server based upon the "alert" configuration of each client sends a mail notification. The
notification is sent to the client configured email address using SMTP. Use a simple text mail
format with some detail about the alert. event logs must be sent via email every time without
any condition.
Assume any functional details required to achieve the above requirements based on logic and your
experience. But follow the KISS principle.

### Other Technical and Non-functional Requirements

The following list of technical specifications should be adhered to
1. Apply validations and constraints wherever necessary to create a stable system.2. Assume missing/unclear requirements to fill in the gaps in the specifications.
3. You can use paramiko for ssh communication.
4. You can use win32api for statistics.
5. You must use SMTP to send emails. You can use smtplib for this purpose.
6. You can use pycrypto for encryption purposes.
7. You should write unit tests for your application.
