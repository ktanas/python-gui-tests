class GroupHelper:

    def __init__(self, app):
        self.app = app

    def get_group_list(self):
        self.open_group_editor()
        tree = self.group_editor.window(auto_id="uxAddressTreeView")
        root = tree.tree_root()
        group_list = [node.text() for node in root.children()]
        self.close_group_editor()
        return group_list

    def add_new_group(self, group_name):
        self.open_group_editor()
        self.group_editor.window(auto_id="uxNewAddressButton").click()
        input = self.group_editor.window(class_name="Edit")
        input.set_text(group_name)
        input.type_keys("\n")
        self.close_group_editor()

    def edit_group_name(self, index, new_name):
        self.open_group_editor()

        tree = self.group_editor.window(auto_id="uxAddressTreeView")
        root = tree.tree_root()
        node_list = root.children()
        # group_list = [node.text() for node in root.children()]

        node_list[index].click()

        self.group_editor.window(auto_id="uxEditAddressButton").click()
        edited_field = self.group_editor.window(class_name="Edit")
        edited_field.set_text(new_name)
        edited_field.type_keys("\n")
        self.close_group_editor()

    def delete_group(self, index):
        self.open_group_editor()

        tree = self.group_editor.window(auto_id="uxAddressTreeView")
        root = tree.tree_root()
        node_list = root.children()
        # group_list = [node.text() for node in root.children()]

        node_list[index].click()
        self.group_editor.window(auto_id="uxDeleteAddressButton").click()

        self.delete_group = self.app.application.window(title="Delete group")
        self.delete_group.wait("visible")
        self.delete_group.window(auto_id="uxOKAddressButton").click()

        self.close_group_editor()

    def open_group_editor(self):
        self.app.main_window.window(auto_id="groupButton").click()
        self.group_editor = self.app.application.window(title="Group editor")
        self.group_editor.wait("visible")

    def close_group_editor(self):
        self.group_editor.close()
