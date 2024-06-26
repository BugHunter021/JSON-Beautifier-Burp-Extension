# JSON Beautifier Burp Suite Extension
Version 1.0

The JSON Beautifier Burp Suite extension simplifies the process of Beautifier JSON payloads for pentesters, as there is no built-in option for this in Burp. This is especially true when working with JSON payloads and trying to ensure that they are properly Beautifier to prevent errors. It eliminates the need for manual escaping and ensures proper formatting for testing. With its simple interface, the plugin enables you to enter your payload, escape it, and display the result in a JTextArea where you can select and copy the text

## How to Use
1. Download the plugin [JSON-Beautifier.py](https://raw.githubusercontent.com/BugHunter021/JSON-Beautifier-Burp-Extension/main/JSON-Beautifier.py)
2. Set up Jython in Burp Suite by going to the Extender tab and selecting the Options subtab. Under the "Python Environment" section, select "Use existing Jython standalone JAR" and browse to the location of the Jython standalone JAR on your computer
3. In Burp Suite, go to the Extender tab and click on the "Add" button.
4. Select "Python" as the extension type and select the JSON-Beautifier.py file from your computer.
5. The JSON Beautifier tab will be added to the Burp Suite UI.
6. Enter the payload in the text field and click on the "Beautifier" button.
7. The escaped payload will be displayed in the JTextArea, where you can select and copy the text.

OR

Install from BApp store.

![image](https://github.com/BugHunter021/JSON-Beautifier-Burp-Extension/assets/76444458/d597af5f-aa1e-492e-b4fc-8e7811d06c84)


Please note that it is necessary to have Jython installed in order to use this plugin. If you do not have Jython installed, you can download it from the official website (http://www.jython.org/) and follow the instructions for installation.

## Feedback
If you have any feedback or suggestions, feel free to open an issue on this Github repository.

## License
This plugin is licensed under the MIT License.
