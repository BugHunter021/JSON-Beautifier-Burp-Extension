from burp import IBurpExtender, ITab
from java.awt import GridBagLayout, GridBagConstraints, Insets
from java.io import PrintWriter
from java.lang import RuntimeException
from javax.swing import JPanel, JLabel, JTextField, JButton, JScrollPane, JTextArea, BorderFactory, SwingConstants, JPopupMenu, JMenuItem
import json

### Created By BugHunter021

class JSONBeautifierTab(ITab):
    def __init__(self, extender):
        self._extender = extender
        self._txtPayload = JTextArea(6, 20)
        self._txtPayload.setLineWrap(True)
        self._txtPayload.setWrapStyleWord(True)
        self._scrollPanePayload = JScrollPane(self._txtPayload)
        self._Beautifier = JButton("Beautifier", actionPerformed=self.beautifier)
        self._txtResult = JTextArea(10, 26)
        self._txtResult.setLineWrap(True)
        self._txtResult.setWrapStyleWord(True)
        self._txtResult.setEditable(True)
        self._scrollPaneResult = JScrollPane(self._txtResult)

        panel = JPanel()
        layout = GridBagLayout()
        panel.setLayout(layout)

        gbc = GridBagConstraints()
        gbc.gridx = 0
        gbc.gridy = 0
        gbc.weightx = 1.0
        gbc.weighty = 0.0
        gbc.fill = GridBagConstraints.HORIZONTAL
        gbc.insets = Insets(5, 5, 5, 5)

        panel.add(JLabel("JSON:"), gbc)

        gbc.gridy = 1
        gbc.weighty = 1.0
        gbc.fill = GridBagConstraints.BOTH
        gbc.insets = Insets(0, 5, 5, 5)

        panel.add(self._scrollPanePayload, gbc)

        gbc.gridy = 2
        gbc.weighty = 0.0
        gbc.fill = GridBagConstraints.HORIZONTAL

        panel.add(self._Beautifier, gbc)

        gbc.gridy = 3
        gbc.weighty = 0.0
        gbc.fill = GridBagConstraints.HORIZONTAL

        panel.add(JLabel("JSON Beautifier:"), gbc)

        gbc.gridy = 4
        gbc.weighty = 1.0
        gbc.fill = GridBagConstraints.BOTH

        panel.add(self._scrollPaneResult, gbc)

        # Add borders to the text areas
        self._scrollPanePayload.setBorder(BorderFactory.createEtchedBorder())
        self._scrollPaneResult.setBorder(BorderFactory.createEtchedBorder())

        # Add right-click context menu to the input and output areas
        self._txtPayload.setComponentPopupMenu(self.createPopupMenu(self._txtPayload))
        self._txtResult.setComponentPopupMenu(self.createPopupMenu(self._txtResult))

        self.component = panel

    def getTabCaption(self):
        return "JSON Beautifier"

    def getUiComponent(self):
        return self.component

    def beautifier(self, event):
        try:
            payload = self._txtPayload.getText()
            json_data = json.loads(payload)
            formatted_json_str = json.dumps(json_data, sort_keys=True, indent=4)
            self._txtResult.setText(formatted_json_str)
        except Exception as e:
            self._extender._callbacks.printError(str(e))

    def createPopupMenu(self, text_area):
        # Create the right-click context menu
        menu = JPopupMenu()

        # Create menu items
        copy_item = JMenuItem("Copy")
        paste_item = JMenuItem("Paste")
        cut_item = JMenuItem("Cut")
        select_all_item = JMenuItem("Select All")
        clear_item = JMenuItem("Clear")

        # Add action listeners to the menu items
        copy_item.addActionListener(lambda event: self.copyText(text_area))
        paste_item.addActionListener(lambda event: self.pasteText(text_area))
        cut_item.addActionListener(lambda event: self.cutText(text_area))
        select_all_item.addActionListener(lambda event: self.selectAllText(text_area))
        clear_item.addActionListener(lambda event: self.clearText(text_area))

        # Add menu items to the menu
        menu.add(copy_item)
        menu.add(paste_item)
        menu.add(cut_item)
        menu.add(select_all_item)
        menu.add(clear_item)

        return menu

    def copyText(self, text_area):
        # Copy selected text to the clipboard
        text_area.copy()

    def pasteText(self, text_area):
        # Paste text from the clipboard
        text_area.paste()

    def cutText(self, text_area):
        # Cut selected text
        text_area.cut()

    def selectAllText(self, text_area):
        # Select all text
        text_area.selectAll()

    def clearText(self, text_area):
        # Clear the text
        text_area.setText("")

class BurpExtender(IBurpExtender):
    def registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()
        callbacks.setExtensionName("JSON Beautifier")
        callbacks.addSuiteTab(JSONBeautifierTab(self))
