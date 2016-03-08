# Ubiquiti Unifi USG Copy tool
*Copy the Unifi USG configuration file to Unifi Controller*

When the Unifi USG is managed by a Unifi Controller the configuration file will be overwritten as the controller is considered to be leading. However, at time of this writing, the features supported to be configured from the controller are very limited. Therefore people want to be able to change the USG configuration through the CLI.

This script will take your Unifi USG configuration (EdgeOS) and copy it to the Unifi Controller to ensure your changes are not overwritten when the controller pushes configuration to the USG.

If you encounter a problem, please file a Github issue.

##License
This software is licensed under the Apache License, Version 2.0 (the "License"); you may not use this software except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

**Copyright (c) 2016 - Maverick.Solutions - Rick Mur**
