# Ubiquiti Unifi USG Copy tool
*Copy the Unifi USG configuration file to Unifi Controller*

When the Unifi USG is managed by a Unifi Controller the configuration file will be overwritten as the controller is
considered to be leading. However, at time of this writing, the features supported to be configured from the controller
are very limited. Therefore people want to be able to change the USG configuration through the CLI.

This script will upload the current configuration file to the Controller in a specific directory, the controller will
 then use this file instead of the default config, when making changes in the controller.

The script has 2 ways to operate, based on the setting **RUNNING_ON**:

#####USG
The script runs on the Unifi USG and will place your USG configuration (EdgeOS) on the Unifi Controller to ensure your
changes are not overwritten when the controller pushes configuration to the USG.

Keep in mind that there may be some issues getting the right packages installed. Ensure you are able to install
Debian packages on your USG, by adding this configuration:

    system {
        package {
            repository wheezy {
                components "main contrib non-free"
                distribution wheezy
                password ****************
                url http://mirror.leaseweb.com/debian
                username ""
            }
            repository wheezy-security {
                components main
                distribution wheezy/updates
                password ****************
                url http://security.debian.org
                username ""
            }
        }
    }



#####Controller
The script runs on the Unifi Controller and will grab the USG configuration and place it in the right directory to
ensure your changes are not overwritten when the controller pushes configuration to the USG.

If you encounter a problem, please file a Github issue.

##How to get started (from USG)
1. Ensure your USG is configured for Debian package repositories and Python, PIP and Git are installed. More details
can be found on this blog:
2. Download the files on your system using `git clone https://github.com/rickmur/UnifiUSGcopy.git`.
Any further updates are downloaded using `git pull` from the new directory
3. Install required libraries with `pip install -r requirements.txt`.
4. Edit the top lines in `USGcopy.py` to set your controller hostname/IP, username, password and unifi controller file location.
5. Set the `RUNNING_ON` variable to `USG`
6. Run `crontab -e` and append a line to enable recurring updates as per the example below

##How to get started (from Controller)
1. Ensure the system where the Unifi Controller is running has Python, PIP and Git installed.  
2. Download the files on your system using `git clone https://github.com/rickmur/UnifiUSGcopy.git`.
Any further updates are downloaded using `git pull` from the new directory
3. Install required libraries with `pip install -r requirements.txt`.
4. Edit the top lines in `USGget.py` to set your USG hostname/IP, username, password and unifi controller file location.
5. Set the `RUNNING_ON` variable to `Controller`
6. Run `crontab -e` and append a line to enable recurring updates as per the example below


#####Sample crontab job
The following line should be appended to your crontab file (edited either with `crontab -e`. This line will execute
the script every hour on every day on minute 0 of each hour.

    0       *       *       *       *       root    python /PATH_TO_FILES/USGcopy.py

##License
This software is licensed under the Apache License, Version 2.0 (the "License"); you may not use this software except
in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific
language governing permissions and limitations under the License.

**Copyright (c) 2016 - Maverick.Solutions - Rick Mur**
