# Usage

## Getting Started
* Visit your server at `https://<your-ip>:8443`
* You will likely get flash-banged with the default light-theme. 
![alt text](images/login.png)
* In the top right, you can toggle to dark mode:
![alt text](images/switch_to_dark_mode.png)

## Managing Users
* Getting your team onboarded to your C2 server should be the first thing you do, shared passwords are bad!
* In the Admin panel, go to "Create New User" tab and submit the form. Set the username, role, and initial password.
![alt text](images/admin_add_user.png)
* From the "Existing Users" tab, we can edit or delete users. Modifying the initial user is forbidden from this panel.
![alt text](images/admin_existing_users.png)
* By selecting the "Edit" option for a user, we can modify the password and the role.
![alt text](images/admin_edit_user.png)

## Server / API Settings
* Currently, the Server and API only support modifying the logging configuration without restarting the container.
* From the "Server Settings" or "API Settings" tabs, configure the log level and max log file size:
![alt text](images/admin_logs.png)

## User Profile
* The Profile panel allows users to change their password and API keys.
* After a user is created, it is highly recommended for the user to change their password.
![alt text](images/user_password_change.png)
* API keys are created for authentication for the discord bot.
* Enter your password, and the desired max age of the API token:
![alt text](images/user_api_key.png)
* Direct Message your discord bot with `/patron configure <your-api-token>`

## Redirectors
* To install a redirector, create a fresh server. Either install docker first, or use ubuntu 22/24 to use the automatic installer.
* It is suggested to have IPv6 configured already. Ensure an IPv6 appears when running `hostname -I`
* From the Redirector panel in the UI, go to the Create New Redirector tab.
* Set the Redirector Name, Description, and Listen Port.
* Unless chaining multiple redirectors together, do not use the Forward IP and Forward Port options.
![alt text](images/redirectors_create_redirector.png)
* Once you click "Create Redirector", a download will start for a `redirector_install.sh`
* Save this script locally.
* Run this script on the server you created to run the redirector on.
* After a few seconds, you should see your redirector online in the "Existing Redirectors' tab.
![alt text](images/redirector_status.png)