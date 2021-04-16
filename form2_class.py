from form1_class import Form

class FileWriterForm(Form):
    def button_command(self):
        with open('out_file.text', 'w') as out_file:
            for text in self.entries:
                out_file.write('{} = {}\r\n'.format(text, self.entries[text].get()))

    def setup(self):
        self.setup_rows('test', 'testing')
        self.add_button('write', self.button_command)

if __name__ == '__main__':
    FileWriterForm()